CREATE_ENCLOSURES_TABLE = (
    "CREATE TABLE IF NOT EXISTS enclosures (id SERIAL PRIMARY KEY, name TEXT);"
)

CREATE_ANIMALS_TABLE = (
    "CREATE TABLE IF NOT EXISTS animals (animal_id SERIAL PRIMARY KEY, name TEXT, amount INTEGER, enclosure_id INTEGER);"
)

INSERT_ENCLOSURE_RETURN_ID = (
    "INSERT INTO enclosures (name) VALUES (%s) RETURNING id;"
)

INSERT_ANIMAL = (
    "INSERT INTO animals (name, amount, enclosure_id) VALUES (%s, %s, %s);"
)

GET_ENCLOSURE_BY_ID = (
    "SELECT * FROM enclosures WHERE ID = (%s)"
)

GET_ENCLOSURE_BY_NAME = (
    "SELECT * FROM enclosures WHERE name = (%s)"
)

GET_ANIMAL_BY_NAME = (
    "SELECT * FROM animals WHERE name = (%s)"
)

GET_ANIMAL_BY_ID = (
    "SELECT * FROM animals WHERE animal_id = (%s)"
)

UPDATE_ANIMAL_BY_ID = (
    "UPDATE animals SET amount = %s, enclosure_id = %s WHERE animal_id = (%s)"
)

GET_ALL_ENCLOSURES = (
    "SELECT * FROM enclosures"
)

GET_ALL_ANIMALS = (
    "SELECT * FROM animals"
)