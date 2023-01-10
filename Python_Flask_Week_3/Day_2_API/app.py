import os
import random
import psycopg2
from dotenv import load_dotenv
from datetime import datetime, timezone, timedelta
from flask import Flask, render_template, request

#must be above app dec
load_dotenv()

app = Flask(__name__)

#must be below app dec
url = os.getenv("DATABASE_URL")
connection = psycopg2.connect(url)


CREATE_ROOMS_TABLE = (
    "CREATE TABLE IF NOT EXISTS rooms (id SERIAL PRIMARY KEY, name TEXT);"
)

CREATE_TEMPS_TABLE = (
    "CREATE TABLE IF NOT EXISTS temperatures (room_id INTEGER, temperature REAL, date TIMESTAMP, FOREIGN KEY(room_id) REFERENCES rooms(id) ON DELETE CASCADE);"
)

INSERT_ROOM_RETURN_ID = "INSERT INTO rooms (name) VALUES (%s) RETURNING id;"
INSERT_TEMP = (
    "INSERT INTO temperatures (room_id, temperature, date) VALUES (%s, %s, %s);"
)

GLOBAL_NUMBER_OF_DAYS = (
    "SELECT COUNT(DISTINCT DATE(date)) AS days FROM temperatures;"
)

GET_ROOM_BY_ID = (
    "SELECT * FROM rooms WHERE ID = (%s)"
)

GET_AVG_OF_ROOM = "SELECT AVG(temperature) as average FROM temperatures WHERE room_id = (%s);"

GLOBAL_AVG = "SELECT AVG(temperature) as average FROM temperatures;"




@app.get("/")
def hello_world():
    return "Hello Worlds!"


@app.post("/api/room")
def create_room():
    data = request.get_json()
    name = data["name"]

    with connection:
        with connection.cursor() as cursor:
            cursor.execute(CREATE_ROOMS_TABLE)
            cursor.execute(INSERT_ROOM_RETURN_ID, (name,))
            room_id = cursor.fetchone()[0]
    
    return {"id": room_id, "message": "Room " + name + " created."}, 201


GET_NUMER_OF_ROOMS = "SELECT COUNT(*) FROM rooms"

@app.post("/api/add_random_data")
def add_random_data():
    data = request.get_json()
    amount_to_add = data["amount"] #how many datapoints to add

    try:
        date = datetime.strptime(data["data"], "%m-%d-%Y %H:%M:%S")
    except KeyError:
        date = datetime.now(timezone.utc)

    with connection:
        with connection.cursor() as cursor:
            cursor.execute(GET_NUMER_OF_ROOMS) #get number of rooms in database
            numberOfRooms = cursor.fetchone()[0]

            cursor.execute(CREATE_TEMPS_TABLE)

            for i in range(0, int(amount_to_add)):
                tempTemp = random.randint(50, 100) #random tempature value
                room_id = random.randint(1, numberOfRooms) #select random room

                dataDifference = timedelta(random.randint(1, 30)) #subtract 1 to 30 days from current date
                tempDate = date - dataDifference

                cursor.execute(INSERT_TEMP, (room_id, tempTemp, tempDate))

    return {"message": amount_to_add + " Temperature Datapoints added."}, 201

@app.post("/api/temperature")
def add_temp():
    data = request.get_json()
    temperature = data["temperature"]
    room_id = data["room"]

    try:
        #date string time info https://strftime.org/
        date = datetime.strptime(data["data"], "%m-%d-%Y %H:%M:%S")
    except KeyError:
        date = datetime.now(timezone.utc)

    with connection:
        with connection.cursor() as cursor:
            cursor.execute(CREATE_TEMPS_TABLE)
            cursor.execute(INSERT_TEMP, (room_id, temperature, date))

    return {"message": "Temperature added."}, 201



@app.get("/api/get_room/<room_id>")
def get_room(room_id):
    with connection:
        with connection.cursor() as cursor:
            cursor.execute(GET_ROOM_BY_ID, (room_id,))
            room_name = cursor.fetchone()[1]

    return "Room ID: " + room_id + " has the name of: "  + room_name, 200
    


@app.get("/api/get_room_average/<room_id>")
def get_room_average(room_id):

    with connection:
        with connection.cursor() as cursor:
            cursor.execute(GET_ROOM_BY_ID, (room_id,))
            room_name = cursor.fetchone()[1]
            cursor.execute(GET_AVG_OF_ROOM, (room_id,))
            average = cursor.fetchone()[0]

    return "Average Tempature for #" + str(room_id) + " '" + room_name + "': " + str(average), 200



@app.get("/api/compare_rooms")
def compare_rooms():

    room1Id = request.args.get('room1')
    room2Id = request.args.get('room2')

    with connection:
        with connection.cursor() as cursor:
            cursor.execute(GET_ROOM_BY_ID, (room1Id,))
            room1Name = cursor.fetchone()[1].capitalize()
            cursor.execute(GET_ROOM_BY_ID, (room2Id,))
            room2Name = cursor.fetchone()[1].capitalize()

            cursor.execute(GET_AVG_OF_ROOM, (room1Id,))
            averageRoom1 = cursor.fetchone()[0]
            cursor.execute(GET_AVG_OF_ROOM, (room2Id,))
            averageRoom2 = cursor.fetchone()[0]

    warmer = room1Name if averageRoom1 > averageRoom2 else room2Name
    return "Average Tempature for #" + str(room1Id) + " '" + room1Name + "': " + str(round(averageRoom1, 2)) + " --- Average Tempature for #" + str(room2Id) + " '" + room2Name + "': " + str(round(averageRoom2, 2)) + " --- " + warmer + " tends to be the warmer room.", 200





@app.get("/api/get_averages")
def get_averages():

    with connection:
        with connection.cursor() as cursor:
            cursor.execute(GLOBAL_AVG)
            average = cursor.fetchone()[0]

    return "Average Tempature of all rooms: " + str(average), 200


@app.get("/api/get_days")
def get_days():

    with connection:
        with connection.cursor() as cursor:
            cursor.execute(GLOBAL_NUMBER_OF_DAYS)
            average = cursor.fetchone()[0]

    return "Number of days of recording: " + str(average), 200

#https://devhints.io/http-status










"""
@app.get("/api/get_room")
def get_room():
    data = request.get_json()
    room_id = data["room"]

    with connection:
        with connection.cursor() as cursor:
            cursor.execute(GET_ROOM_BY_ID, (room_id,))
            room_name = cursor.fetchone()[1]

    return {"name": room_name, "message": "Room ID: " + room_id + " has the name of: "  + room_name}, 200
"""