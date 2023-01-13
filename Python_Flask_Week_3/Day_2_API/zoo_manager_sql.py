CREATE_ENCLOSURES_TABLE = (
    "CREATE TABLE IF NOT EXISTS enclosures (id SERIAL PRIMARY KEY, name TEXT);"
)

CREATE_ANIMALS_TABLE = (
    "CREATE TABLE IF NOT EXISTS animals (name TEXT, amount INTEGER, FOREIGN KEY(enclosure_id) REFERENCES enclosures(id) ON DELETE CASCADE);"
)

INSERT_ENCLOSURE_RETURN_ID = (
    "INSERT INTO rooms (name) VALUES (%s) RETURNING id;"
)

INSERT_ANIMAL = (
    "INSERT INTO animals (name, amount, enclosure_id) VALUES (%s, %s, %s);"
)

GET_ENCLOSURE_BY_ID = (
    "SELECT * FROM enclosures WHERE ID = (%s)"
)

GLOBAL_NUMBER_OF_DAYS = (
    "SELECT COUNT(DISTINCT DATE(date)) AS days FROM temperatures;"
)



GET_AVG_OF_ROOM = (
    "SELECT AVG(temperature) as average FROM temperatures WHERE room_id = (%s);"
)

GLOBAL_AVG = (
    "SELECT AVG(temperature) as average FROM temperatures;"
)