import os
import sys

sys.path.insert(1, './code')
from main import Point

import pytest
import sqlite3
import requests

#pytest
#pyest -v
#pytest -v -s

#pytest -k "subtraction"
#pytest -v -s -k "simple"


#pytest-html
#pytest --html-report.html

#tuple set
@pytest.mark.parametrize("inputs, expected_output", [
    ([2, 3], 5),
    ([-2, 3], 1),
    ([2, -3], -1),
    ([0, 0], 0)
]) 
def test_addition(inputs, expected_output):
    print("\nAddition Iteration - Test Start")
    assert add(inputs[0], inputs[1]) == expected_output
    print("\nAddition Iteration - Test End")


def add(a, b):
    return a + b







"""
#often use for checking connections. can also do temp folders.
@pytest.fixture #decorator
def setup_database():
    conn = sqlite3.connect(":memory:")
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE stocks (date text, trans text, symbol text, qty real, price real)")
    sample_data = [
        ('2020-01-01', "BUY", "IBM", 1000, 45.0),
        ('2020-01-02', "SELL", "TSLA", 352, 200.0)
    ]
    cursor.executemany("INSERT INTO stocks VALUES(?, ?, ?, ?, ?)", sample_data)
    yield conn


def test_connection(setup_database):
    cursor = setup_database
    assert len(list(cursor.execute("SELECT * FROM stocks"))) == 2

"""





"""
def test_make_point():
    point = Point("Texas", 34, 36)
    assert point.get_lat_long() == (34, 36)
"""





"""
def test_file_exists():
    assert os.path.exists("./static/file.txt")


def test_file_contents():
    with open("./static/file.txt", 'r') as f:
        contents = f.read()

    assert contents == "The contents of this file"
    assert len(contents) > 5


def test_file_creation():
    path = "./static/new_file.txt"
    create_file(path)
    assert os.path.exists(path)


def create_file(path):
    with open(path, 'w') as f:
        f.write("The contents of this file")


def test_new_file_contents():
    path = "./static/new_file.txt"
    with open(path, 'r') as f:
        contents = f.read()

    assert contents == "The contents of this file"
    assert len(contents) > 5
    
"""


"""
def test_addtion():
    print("\nAddition Test - Begin")
    assert add(2, 3) == 5
    assert add(2, 4) == 6
    assert add(5, 10) == 15
    print("Addition Test - Complete")

def add(a ,b):
    print("Addition Assertion Iteration - Complete")
    return a + b

def test_subtraction():
    print("\nSubtraction Test - Begin")
    assert subtraction(2, 3) == -1
    assert subtraction(2, 4) == -2
    assert subtraction(5, 10) == -5
    print("Subtraction Test - Complete")

def subtraction(a ,b):
    print("Subtraction Assertion Iteration - Complete")
    return a - b
"""



"""
class TestCalulator:
    
    @pytest.mark.simple
    def test_addition(self):
        calc = Calculator()
        assert calc.add(2, 3) == 5
        assert calc.add(2, 4) == 6
        assert calc.add(5, 10) == 15

    @pytest.mark.simple
    def test_subtraction(self):
        calc = Calculator()
        assert calc.subtract(2, 3) == -1
        assert calc.subtract(2, 4) == -2
        assert calc.subtract(5, 10) == -5

    @pytest.mark.simple
    def test_multiply(self):
        calc = Calculator()
        assert calc.multiply(2, 3) == 6
        assert calc.multiply(2, 4) == 8
        assert calc.multiply(5, 10) == 50

    @pytest.mark.simple
    def test_division(self):
        calc = Calculator()
        assert calc.division(4, 2) == 2
        assert calc.division(8, 4) == 2
        assert calc.division(10, 5) == 2
        assert calc.division(10, 3) == pytest.approx(3.33, 0.01)
        assert calc.division(10, 0) == "Can't divide by 0"
        #with pytest.raises(ZeroDivisionError): #, match="division by zero"):
            #calc.division(10, 0)

    @pytest.mark.complex
    def test_overall(self):
        calc = Calculator()
        assert calc.multiply(calc.add(2, 3), calc.subtract(2, 3)) == -5
        assert calc.division(calc.add(2, 3), calc.subtract(2, 3)) == -5
        assert calc.division(calc.add(2, 3), calc.subtract(2, 2)) == "Can't divide by 0"

        with pytest.raises(TypeError):
            calc.division(calc.add(2, 3), calc.division(2, 0))


    @pytest.mark.complex
    def test_negatives(self):
        calc = Calculator()
        assert not calc.add(2, 2) == 3
        assert not calc.subtract(4, 2) == 3
        assert not calc.multiply(4, 2) == 3
        assert not calc.division(10, 5) == 3
        assert not calc.division(10, 5) == "Can't divide by 0"




class Calculator:

    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def division(self, a, b):
        #if b == 0:
            #return "Can't divide by 0"
        try:
            return a / b
        except ZeroDivisionError:
            return "Can't divide by 0"
"""
