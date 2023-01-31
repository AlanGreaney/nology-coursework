from flask import Flask, request
from pymongo import MongoClient
from mongopass import mongopass
from bson import json_util
from bson.objectid import ObjectId
import json

app = Flask(__name__)

client = MongoClient(mongopass)
db = client["Cluster0"]
collection = db["addColl"]

@app.route("/")
def index():
    data = []
    for d in collection.find():
        data.append(d)

    return json.dumps(data, indent=4, default=json_util.default), 200


@app.route("/item/<item_id>")
def get_item(item_id):
    item = collection.find_one({"_id": ObjectId(item_id)})
    if item:
        return json_util.dumps(item), 200
    else:
        return json_util.dumps({"error": "Item was not found"}), 404


@app.route("/add_item", methods=["POST"])
def add_item():
    item = request.get_json()
    result = collection.insert_one(item)
    return json_util.dumps({"_id": str(result.inserted_id)}), 201



@app.route("/item/<item_id>", methods=["PUT"])
def update_item(item_id):
    item = request.get_json()
    result = collection.update_one({"_id": ObjectId(item_id)}, {"$set": item})
    if result.matched_count > 0:
        return json_util.dumps({"status": "success"})
    else:
        return json_util.dumps({"error": "Item to edit not found"}), 404 


@app.route("/item/<item_id>", methods=["DELETE"])
def delete_item(item_id):
    result = collection.delete_one({"_id": ObjectId(item_id)})
    if result.deleted_count > 0:
        return json_util.dumps({"status:": "successfully deleted"})
    else:
        return json_util.dumps({"error": "Item to delete not found"}), 404 

#crud = create read update delete

if __name__ == '__main__':
    app.run()