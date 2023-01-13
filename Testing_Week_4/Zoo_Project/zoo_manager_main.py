import os
import sys
import psycopg2
from dotenv import load_dotenv
from flask import Flask, render_template, request

import zoo_manager_logging
sqlLogger = zoo_manager_logging.setup_logger("loggingCsv", "sqlLogs.csv", zoo_manager_logging.csvFormatter())

import zoo_manager_sql as zmSql

load_dotenv()

def create_app(connection=None, cursor=None, testing=False):
    app = Flask(__name__)
    
    if connection == None:
        sqlLogger.info("SQL: Using connection in main file")
        connection = psycopg2.connect(url)
        cursor = connection.cursor()
    else:
        sqlLogger.info("SQL: Using test connection")
    
    #app.teardown_appcontext(close_db)

    """@app.teardown_appcontext
    def close_db(exception):
        if connection is not None:
            cursor.close()
            connection.close()"""

    #for routes, use blueprints for funcs different files

    @app.get("/")
    def homepage():
        return "Welcome to the Zoo Management Homepage."


    @app.post("/api/enclosure")
    def create_enclosure():
        data = request.get_json()
        name = data["name"]

        sqlLoggingWrapper(cursor, zmSql.CREATE_ENCLOSURES_TABLE)
        sqlLoggingWrapper(cursor, zmSql.GET_ENCLOSURE_BY_NAME, (name,))
        result = cursor.fetchone()
        if  result == None:
            sqlLoggingWrapper(cursor, zmSql.INSERT_ENCLOSURE_RETURN_ID, (name,))
            enclosure_id = cursor.fetchone()[0]
            return {"id": enclosure_id, "message": "Enclosure " + name + " created."}, 201
        else:
            enclosure_id = result[0]
            return {"id": enclosure_id, "message": "Enclosure " + name + " already exists."}, 201



    @app.post("/api/animal")
    def add_animal():
        data = request.get_json()
        name = data["name"]
        amount = data["amount"]
        enclosure_id = data["enclosure"]

        sqlLoggingWrapper(cursor, zmSql.CREATE_ANIMALS_TABLE)
        sqlLoggingWrapper(cursor, zmSql.INSERT_ANIMAL, (name, amount, enclosure_id))

        #possible addition: check if animal already exists in enclosure?

        return {"message": "Animal added - " + amount + " " + name + " in enclosure: " + enclosure_id}, 201



    @app.get("/api/get_enclosure/<enclosure_info>")
    def get_enclosure(enclosure_info):
        if enclosure_info.isdigit():
            sqlLoggingWrapper(cursor, zmSql.GET_ENCLOSURE_BY_ID, (enclosure_info,))
            result = cursor.fetchone()
            if not result == None:
                return "Room ID: " + str(result[0]) + " has the name of: " + result[1], 200 

        sqlLoggingWrapper(cursor, zmSql.GET_ENCLOSURE_BY_NAME, (enclosure_info,))
        result = cursor.fetchone()
        if not result == None:
            return "Room ID: " + str(result[0]) + " has the name of: " + result[1], 200 

        return "Room by that ID or Name not found.", 200

        
    @app.get("/api/get_animal/<animal_name>")
    def get_animal(animal_name):

        animals = {}

        sqlLoggingWrapper(cursor, zmSql.GET_ANIMAL_BY_NAME, (animal_name,))
        for result in cursor:
            animals[result[0]] = (result[2], result[3])

        return animals, 200

    def sqlLoggingWrapper(cursor, query, params=None):
 
        if params == None:
            sqlLogger.info("SQL Query being made: " + query + " - with no parameters.")
            cursor.execute(query)
        else:
            sqlLogger.info("SQL Query being made: " + query + " - with the parameters: " + str(params))
            cursor.execute(query, params)

        if not testing:
            sqlLogger.info("Committing SLQ")
            connection.commit()



    @app.post("/api/edit_animal")
    def edit_animal():
        data = request.get_json()
        animalId = data["id"]
        
        sqlLoggingWrapper(cursor, zmSql.GET_ANIMAL_BY_ID, (animalId,))
        result = cursor.fetchall()
        if len(result) > 0:
            newAmount = data["newAmount"] if "newAmount" in data else result[0][2]
            newEnclosureId = data["newEnclosureId"] if "newEnclosureId" in data else result[0][3]
            animalName = result[0][1]
        else:
            return "No Animal with the ID of " + animalId + " was found.", 412

        sqlLoggingWrapper(cursor, zmSql.UPDATE_ANIMAL_BY_ID, (newAmount, newEnclosureId, animalId))

        return {"message": "Animal ID #" + animalId + " - '" + animalName + "' now has - Amount: " + str(newAmount) + " / Enclosure ID: " + str(newEnclosureId)}, 200



    return app

url = os.getenv("DATABASE_URL")

app = create_app()