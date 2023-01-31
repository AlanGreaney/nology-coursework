CREATE TABLE zoo_animal_food (
    id SERIAL PRIMARY KEY,
    food VARCHAR(255),
    food_type VARCHAR(255)
);
INSERT INTO zoo_animal_food (food, food_type)
VALUES ('grass', 'grains'), ('hay', 'grains'), ('legumes', 'legumes'), ('banana', 'fruit'),
    ('apple', 'fruit'), ('oragne', 'fruit'), ('broccoli', 'vegetable'), ('mice', 'rodent'), ('rat', 'rodent'),
    ('snails', 'insects'), ('centipedes', 'insects'), ('carrot', 'vegetable'), ('mushroom', 'fungus'), ('leafs', 'greens');
	

SELECT * FROM zoo_animal_food;


ALTER TABLE animals
ADD COLUMN food text[];

UPDATE animals AS main SET
	food = foodData.food
FROM (values
	('antelope', ARRAY['grass', 'hay', 'apple']),
	('ostrich', ARRAY['grass', 'hay', 'leafs']),
	('iguana', ARRAY['mice', 'broccoli']),
	('komodo dragon', ARRAY['mice', 'rat']),
	('kiwi', ARRAY['snails', 'centipedes', 'apple']),
	('tortoise', ARRAY['leafs', 'carrot', 'mushroom']),
	('bonobo', ARRAY['carrot', 'apple', 'banana'])
) AS foodData(animal, food)
WHERE foodData.animal = main.name


SELECT * FROM animals;