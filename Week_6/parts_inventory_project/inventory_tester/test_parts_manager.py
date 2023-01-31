import os
import sys
import ast
import json
import pytest
import logging
import requests


sys.path.insert(0, 'inventory_manager')
from parts_manager_main import create_app


logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

#export FLASK_APP=inventory_manager/parts_manager_main.py

#pytest -v --html=report.html

#https://pypi.org/project/pytest-cov/
#branch coverage too

#coverage run --source=zoo_manager_main.py -m pytest -v 
#pytest -v --html=report.html --cov --cov-report=html
#pytest -v --html=report.html --cov --cov-report=html --cov-branch
#https://stackoverflow.com/questions/34651379/how-to-make-py-test-cov-skip-virtualenv-directory
#pytest --cov=app tests/
#coverage report -m


#pytest inventory_tester/test_parts_manager.py -v --html=report.html --cov=inventory_tester/ --cov-report=html --cov-branch


#tried lots of stuff, trying to get right
#made notes on what tests to run, basic data idea, then wrote main code, didnt need to change after
#order/dependency - not best practice, but played around with it just to know how it works
#testing methodology = white box
#missing a test from add_part

#data test
    #https://i.imgur.com/SSxP2Xz.png

    #https://github.com/mdomke/pytest-mongodb
    #https://stackoverflow.com/questions/56029111/how-do-i-mock-pymongo-for-testing-with-a-flask-app
    



class TestPartsManager:
    @pytest.fixture()
    def app(self, mongodb):
        app = create_app(mongodb)

        yield app

    @pytest.fixture()
    def client(self, app):
        return app.test_client()

    @pytest.mark.order(1)
    def test_flask_application(self, client):
        logger.info("Running test on Flask Application Basic Setup with Mocked Database")
        response = client.get('/')
        logger.info("Verifying default GET page loads")
        assert response.status_code == 200
        logger.info("Verifying Mock Database Returned Correct Initial Data")
        jsonData = json.loads(response.data.decode("UTF-8"))
        assert jsonData[0]['name'] == "Square Head Bolt"
        assert jsonData[0]['partNum'] == 39

    @pytest.mark.order(2)
    @pytest.mark.parametrize("input, output", [
        (({"name": "50mm Gear",
        "partNum": 493,
        "quantity": 32,
        "desiredReserve": 30,
        "cost": 4.24,
        "manufacturer": "sandvik",
        "weight": 0.2,
        "dimensions": "50d 10h",
        "stockedDate": "1669852800000",
        "shelfLife": 900,
        "systems": ["scanner", "twinscan", "euv"]}), (201, "Item added")),
        (({"name": "Medium Power Laser",
        "partNum": 6343,
        "desiredReserve": 10,
        "cost": 1499.99,
        "manufacturer": "iPG Photonics",
        "weight": 34,
        "dimensions": "500d 100h 350w",
        "stockedDate": "1669852800000",
        "shelfLife": 30,
        "systems": ["euv"]}), (406, "Part not added. The following data-point is missing: quantity")),
        (({"name": "Medium Power Laser",
        "partNum": 6343,
        "quantity": 3,
        "desiredReserve": 10,
        "cost": 1499.99,
        "manufacturer": "iPG Photonics",
        "weight": 34,
        "dimensions": "500d 100h 350w",
        "stockedDate": "1669852800000",
        "shelfLife": 30,
        "systems": ["euv"]}), (201, "Item added")),
        (({"name": "Square Head Bolt",
        "partNum": 39,
        "quantity": 530,
        "desiredReserve": 600,
        "cost": 0.5,
        "manufacturer": "uxcell",
        "weight": 0.068,
        "dimensions": "12.7d 50.8l",
        "stockedDate": "1669852800000",
        "shelfLife": 365,
        "systems": ["euv"]}), (406, "Item with that part number already exists"))]) 
    def test_add_part(self, client, input, output):
        logger.info("Testing part addition for item named: " + input["name"])
        response = client.post('/add_part', json = input) 
        logger.info("Verifying response is code: " + str(output[0]) + " with message: '" + output[1] + "'")
        response_str = response.data.decode("UTF-8")
        assert response.status_code == output[0]
        assert output[1] in response_str


    @pytest.mark.order(3)
    @pytest.mark.parametrize("input, output", [
        (("63d2b6260697aff60c8fcf9a"), (200, "Square Head Bolt")),
        (("63d2a6260697aff60c8fcf9a"), (404, "Item with Part Number or Databse ID of '63d2a6260697aff60c8fcf9a' was not found")),
        (("39"), (200, "Square Head Bolt")),
        (("1234"), (404, "Item with Part Number or Databse ID of '1234' was not found"))
    ])
    def test_get_part(self, client, input, output):
        logger.info("Testing part retrieval for item with ID: " + input)
        response = client.get('/get_part/' + input)
        assert response.status_code == output[0]
        match response.status_code:
            case 200:
                logger.info("Verifying response is code: " + str(output[0]) + " with item named: '" + output[1] + "'")
                jsonData = json.loads(response.data.decode("UTF-8"))
                assert jsonData['name'] == output[1]
            case 404:
                logger.info("Testing part response could not find non-existant part id: " + input)
                response_str = response.data.decode("UTF-8")
                assert output[1] in response_str
                


    @pytest.mark.order(4)
    @pytest.mark.parametrize("input, output", [
        (("63d2b6260697aff60c8fcf9a",
        {"partNum": 39,
        "quantity": 549,
        "cost": 1.5,}), (200, "Item 63d2b6260697aff60c8fcf9a has been updated")),
        (("63d2b6260697aff60c8fcf9a", {}), (406, "No Items were included to update")),
        (("63d2b6260697aff60c8fcf9a",
        {"partNum": 39,
        "quantity": 530,
        "color": "hot pink"}), (406, "Part not added. The following data-point is not a tracked part inventory detail: " + "color")),
        (("63d2b6260697aff60c8fcf9b",
        {"partNum": 39,
        "quantity": 530,
        "desiredReserve": 600,
        "cost": 0.5,
        "manufacturer": "uxcell",
        "weight": 0.068,
        "dimensions": "12.7d 50.8l",
        "stockedDate": "1669852800000",
        "shelfLife": 365,
        "systems": ["euv"]}), (404, "Part with Databse ID of '63d2b6260697aff60c8fcf9b' was not found"))]) 
    def test_update_part(self, client, input, output):
        logger.info("Testing part addition for item with ID: " + input[0] + " and the following data:")
        logger.info(input[1])

        response = client.put('/part/' + input[0], json = input[1]) 
        response_str = response.data.decode("UTF-8")

        logger.info("Verifying response code of: "  + str(output[0]))
        assert response.status_code == output[0]
        logger.info("Verifying response status of: "  + output[1])
        assert output[1] in response_str



    @pytest.mark.order(5)
    @pytest.mark.parametrize("input, output", [
        (("63d2b6260697aff60c8fcf9a"), (200, "Succsessfully deleted Part with Database ID: 63d2b6260697aff60c8fcf9a")),
        (("63d2b6260697aff60c8fcf9b"), (404, "Part with Databse ID of '63d2b6260697aff60c8fcf9b' was not found"))
    ])
    def test_delete_part(self, client, input, output):
        logger.info("Testing part deletion for item with ID: " + input)
        response = client.delete('/part/' + input) 
        response_str = response.data.decode("UTF-8")

        logger.info("Verifying response code of: "  + str(output[0]))
        assert response.status_code == output[0]
        logger.info("Verifying response status of: "  + output[1])
        assert output[1] in response_str


    @pytest.mark.order(6)
    def test_check_stock(self, client):
        logger.info("Retrieving Low Stock GET check using test database")
        response = client.get('/check_stock')
        assert response.status_code == 200
        jsonData = json.loads(response.data.decode("UTF-8"))
        expectedProducts = {
            "Square Head Bolt",
            "High Power Laser",
            "Electro-Pneumatic Control Box"
        }
        resultProducts = [ subList['name'] for subList in jsonData ]

        for product in expectedProducts:
            logger.info("Checking that product with low stock in results: " + product)
            assert product in resultProducts

    
    @pytest.mark.order(7)
    def test_check_expired(self, client):
        logger.info("Retrieving Expired GET check using test database")
        response = client.get('/check_expired')
        assert response.status_code == 200
        jsonData = json.loads(response.data.decode("UTF-8"))
        
        expectedProducts = {
            "High Power Laser",
            "Electro-Pneumatic Control Box"
        }
        resultProducts = [ subList['name'] for subList in jsonData ]

        for product in expectedProducts:
            logger.info("Checking that product is expired in results: " + product)
            assert product in resultProducts