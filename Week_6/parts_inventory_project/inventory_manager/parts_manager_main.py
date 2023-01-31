import os
import sys
import json
import datetime
from flask import Flask, render_template, request
from pymongo import MongoClient
from mongopass import mongopass
from bson import json_util
from bson.objectid import ObjectId


import parts_manager_logging
sqlLogger = parts_manager_logging.setup_logger("loggingCsv", "NoSqlLogs.csv", parts_manager_logging.csvFormatter())

#class Part(): #Part(**args) call like this
#    def __init__(self, **kwargs):
#        self.__dict__.update((k, v) for k, v in kwargs.items() if k in requiredFields)

requiredFields = {
    "name", #string
    "partNum", #int
    "quantity", #int
    "desiredReserve", #int
    "cost", #in USD
    "manufacturer", #string name
    "weight", #in kg
    "dimensions", #in mm
    "stockedDate", #date YYYY-MM-DD
    "shelfLife", #int in days
    "systems" #array of strings
}

def create_app(collection=None):#connection=None, cursor=None, testing=False):
    app = Flask(__name__)

    subDatabaseName = "parts_main"

    if collection == None:
        client = MongoClient(mongopass)
        db = client["parts_inventory"]
        collection = db[subDatabaseName]
    else:
        collection = collection[subDatabaseName]

    @app.get("/")
    def homepage():
        data = []
        for d in collection.find():
            data.append(d)

        return json.dumps(data, indent=4, default=json_util.default), 200


    @app.route("/get_part/<part_id>")
    def get_part(part_id):
        if ObjectId.is_valid(part_id):
            itemByDBid = collection.find_one({"_id": ObjectId(part_id)})

            if itemByDBid:
                return json_util.dumps(itemByDBid), 200      
        
        if part_id.isnumeric():
            itemByPartNum = collection.find_one({"partNum": int(part_id)})
            if itemByPartNum:
                return json_util.dumps(itemByPartNum), 200
        
        return json_util.dumps({"error": "Item with Part Number or Databse ID of '" + part_id + "' was not found"}), 404


    @app.route("/add_part", methods=["POST"])
    def add_part():
        item = request.get_json()
        for field in requiredFields:
            if field not in item.keys():
                return "Part not added. The following data-point is missing: " + field, 406


        itemByPartNum = collection.find_one({"partNum": item["partNum"]})
        if itemByPartNum:
            return json_util.dumps({"Item with that part number already exists": itemByPartNum}), 406

        result = collection.insert_one(item)
        return json_util.dumps({"Item added": {"_id": str(result.inserted_id)}}), 201


    @app.route("/part/<part_id>", methods=["PUT"])
    def update_part(part_id):
        part = request.get_json()
        if len(part) == 0:
            return "No Items were included to update", 406

        for field in part.keys():
            if field not in requiredFields:
                return "Part not added. The following data-point is not a tracked part inventory detail: " + field, 406

        result = collection.update_one({"_id": ObjectId(part_id)}, {"$set": part})
        if result.matched_count > 0:
            return json_util.dumps({"status": "Item " + part_id + " has been updated"}), 200
        else:
            return json_util.dumps({"error": "Part with Databse ID of '" + part_id + "' was not found"}), 404


    @app.route("/part/<part_id>", methods=["DELETE"])
    def delete_item(part_id):
        result = collection.delete_one({"_id": ObjectId(part_id)})
        if result.deleted_count > 0:
            return json_util.dumps({"status:": "Succsessfully deleted Part with Database ID: " + part_id}), 200
        else:
            return json_util.dumps({"error": "Part with Databse ID of '" + part_id + "' was not found"}), 404


    @app.route("/check_stock", methods=["GET"])
    def check_stock():
        lowStock = []
        for d in collection.find():
            if d["quantity"] < d["desiredReserve"]:
                lowStock.append({"name": d["name"], "partNum": d["partNum"], "quantity": d["quantity"], "desiredReserve": d["desiredReserve"]})

        return json.dumps(lowStock, indent=4, default=json_util.default), 200


    @app.route("/check_expired", methods=["GET"])
    def check_expired():
        expiredParts = []
        for d in collection.find():
            currentDate = datetime.datetime.now()
            daysSinceStocked = (currentDate - d["stockedDate"]).days
            if daysSinceStocked > d["shelfLife"]:
                expiredParts.append({
                    "name": d["name"], 
                    "partNum": d["partNum"], 
                    "stockedDate": d["stockedDate"], 
                    "shelfLife": d["shelfLife"],
                    "stockedTotal": daysSinceStocked
                })

        return json.dumps(expiredParts, indent=4, default=json_util.default), 200
    
    
    return app

app = create_app()