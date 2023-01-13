import os
import sys
import ast
import pytest
import sqlite3
import psycopg2
import requests
from dotenv import load_dotenv

import logging

from zoo_manager_main import create_app
import zoo_manager_sql as zmSql

#export FLASK_APP=zoo_manager_main.py
#export FLASK_DEBUG=1
#flask run

#pytest -v --html=report.html

load_dotenv()
url = os.getenv("DATABASE_URL")

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

class TestZooManager:

    #setUp()
    #tests
    #tearDown()

    #database setup:
    #should probably be @mock.patch / magicmock
    #https://stackoverflow.com/questions/72574761/what-is-the-correct-way-to-mock-psycopg2-with-pytest
    #https://stackoverflow.com/questions/58598825/python-mocking-psycopg2-connection-and-cursor
    #https://gist.github.com/graphaelli/906b624c18f77f50da5cd0cd4211c3c8

    #use module scope to only setup once per Class
    @pytest.fixture(scope="module")
    def setup_database(self):
        logger.info("Commencing Database Setup")
        conn = psycopg2.connect(url)
        cursor = conn.cursor()
        cursor.execute(zmSql.CREATE_ENCLOSURES_TABLE)
        cursor.execute(zmSql.CREATE_ANIMALS_TABLE)
        
        logger.info("Add Sample Enclosure Data")
        sample_data = [
            ('prarie',),
            ('desert',),
            ('island',),
            ('mountains',),
            ('coast',),
            ('savana',)
        ]
        cursor.executemany(zmSql.INSERT_ENCLOSURE_RETURN_ID, sample_data)

        logger.info("Add Sample Enclosure Data")
        sample_data = [
            ('antelope', 15, 13),
            ('armadillo', 4, 13),
            ('anteater', 11, 13),
            ('antelope', 13, 18),
            ('zebra', 6, 18),
            ('tortoise', 3, 18)
        ]
        cursor.executemany(zmSql.INSERT_ANIMAL, sample_data)

        logger.info("Finished Database Setup")

        yield conn, cursor

        if not conn.closed:
            cursor.close()
            conn.close()

    @pytest.fixture()
    def app(self, setup_database):
        connectionDb, cursorDb = setup_database
        app = create_app(connectionDb, cursorDb, True)
        app.config.update({
            "TESTING": True,
        })

        yield app

    @pytest.fixture()
    def client(self, app):
        return app.test_client()


    @pytest.fixture()
    def runner(self, app):
        return app.test_cli_runner()

    def test_database_setup(self, setup_database):
        conn, cursor = setup_database

        logger.info("Running query to retrieve all enclosures")
        cursor.execute(zmSql.GET_ALL_ENCLOSURES)
        result = cursor.fetchall()
        logger.info("Testing Assertion to verify number of enclosures in database")
        assert len(list(result)) == 19

        logger.info("Running query to retrieve all animals")
        cursor.execute(zmSql.GET_ALL_ANIMALS)
        result = cursor.fetchall()
        logger.info("Testing Assertion to verify number of animals in database")
        assert len(list(result)) == 14

    def test_flask_application(self, client):
        logger.info("Running query to test Flask Application Basic Setup")
        response = client.get('/')
        logger.info("Verifying homepage loads")
        assert b"Welcome to the Zoo Management Homepage" in response.data

    def test_add_enclosure(self, client):
        enclosureNew = "testEnclosure"
        enclosureExisting = "prarie"
        testDataNew = {
            'name': enclosureNew
        }
        testDataExisting = {
            'name': enclosureExisting
        }

        logger.info("Running POST to test adding enclosure")
        response = client.post('/api/enclosure', json = testDataNew) 
        response_str = response.data.decode("UTF-8")

        logger.info("Verifying proper response from POST of enclosure addition")
        assert "Enclosure " + enclosureNew + " created." in response_str


        logger.info("Running POST to test adding already existing enclosure")
        response = client.post('/api/enclosure', json = testDataExisting) 
        response_str = response.data.decode("UTF-8")

        logger.info("Verifying proper response from POST of enclosure addition")
        assert "Enclosure " + enclosureExisting + " already exists." in response_str
        

    def test_add_animal(self, client):
        animalName = "elephant"
        animalAmount = "12"
        animalEnclosure = "3"
        testData = {
            'name': animalName,
            'amount': animalAmount,
            'enclosure': animalEnclosure,
        }

        logger.info("Running POST to test adding animal to inventory")
        response = client.post('/api/animal', json = testData) 
        response_str = response.data.decode("UTF-8")

        logger.info("Verifying proper response from POST of animal addition")
        assert "Animal added - " + animalAmount + " " + animalName + " in enclosure: " + animalEnclosure in response_str


    def test_get_enclosure(self, client):
        enclosureByName = "prarie"
        enclosureById = "2"

        logger.info("Running GET to test retrieving Enclosure Information (By Name)")
        response = client.get('/api/get_enclosure/' + enclosureByName) 
        response_str = response.data.decode("UTF-8")
        logger.info("Verifying Output of ID and Name Match for Name: " + enclosureByName)
        assert response_str == "Room ID: 1 has the name of: prarie"

        logger.info("Running GET to test retrieving Enclosure Information (By Id)")
        response = client.get('/api/get_enclosure/' + enclosureById) 
        response_str = response.data.decode("UTF-8")
        logger.info("Verifying Output of ID and Name Match for ID: " + enclosureById)
        assert response_str == "Room ID: 2 has the name of: desert"


    def test_get_animal(self, client):
        logger.info("Running GET to test retrieving Animal Information")
        animalToTest = "tortoise"
        response = client.get('/api/get_animal/' + animalToTest) 
        logger.info("Converting Response to Dictionary Data")
        response_dict = ast.literal_eval(response.data.decode("UTF-8"))
        logger.info("Verifying correct " + animalToTest.capitalize() + " Animal ID corresponds to proper [Amount, Enclosure]")
        assert response_dict["1"] == [3, 1] #[id], [amount, enclosure]
        assert response_dict["7"] == [4, 4]


    def test_edit_animal(self, client):
        testAnimalId_pass = "638"
        testAnimalAmount_pass = "21"
        testAnimalEnclosure_pass = "11"
        testData = {
            'id': testAnimalId_pass,
            'newAmount': testAnimalAmount_pass,
            'newEnclosureId': testAnimalEnclosure_pass,
        }

        logger.info("Running POST to test editing animal")
        response = client.post('/api/edit_animal', json = testData) 
        response_str = response.data.decode("UTF-8")

        logger.info("Verifying proper response from POST of animal editing")
        assert "Animal ID #" + testAnimalId_pass + " - '" + "bonobo" + "' now has - Amount: " + str(testAnimalAmount_pass) + " / Enclosure ID: " + str(testAnimalEnclosure_pass) in response_str


        testAnimalId_fail = "404"
        testAnimalAmount_fail = "404"
        testAnimalEnclosure_fail = "404"
        testData = {
            'id': testAnimalId_fail,
            'newAmount': testAnimalAmount_fail,
            'newEnclosureId': testAnimalEnclosure_fail,
        }

        logger.info("Running POST to test editing animal with invalid ID")
        response = client.post('/api/edit_animal', json = testData) 
        response_str = response.data.decode("UTF-8")

        logger.info("Verifying proper response from POST of animal editing with invalid ID")
        assert "No Animal with the ID of " + testAnimalId_fail + " was found." in response_str


    def test_query_logs(self, client):
        logger.info("Running file check to ensure logging file exists")

        logfile = "./sqlLogs.csv"
        assert os.path.exists(logfile)

        logger.info("Executing lookup query to add onto log file")

        animalToTest = "iguana"
        expectedText = "SQL Query being made: SELECT * FROM animals WHERE name = (%s) - with the parameters: ('" + animalToTest + "',)"
        response = client.get('/api/get_animal/' + animalToTest) 

        logger.info("Opening log file to check if last line is from test query")
        with open(logfile, encoding="utf-8") as fileObj:
            for line in fileObj:
                pass
            last_line = line

            logger.info("Checking if Expected Query Text is in Log File")
            assert expectedText in last_line
