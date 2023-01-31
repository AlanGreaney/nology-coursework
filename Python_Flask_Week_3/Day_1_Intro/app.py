import sys
import numpy
import random
from flask import Flask, render_template

app = Flask(__name__)
random.seed()

@app.route("/")
def hello_world():
    return "Hello World!"

@app.route("/flip")
def flip():
    outcome = "The coin came up heads."
    chance = random.random()*100
    
    if chance < 0.0001666: #1/6000 chance according to google
        outcome = "The coin landed on it's edge!"
    elif chance < 50:
        outcome = "The coin came up tails."
    return outcome




def flipCoin():
    outcome = "Heads"
    chance = random.random()*100
    
    if chance < 0.0001666: #1/6000 chance according to google
        outcome = "Edge"
    elif chance < 50:
        outcome = "Tails"
    return outcome

@app.route("/fancy_flip", methods=['GET', 'POST'])
def fancy_flip():

    return render_template("fancy_flip.html", 
            coinOutcomes=[flipCoin() for i in range(8)])

    """ old non-repeating method left as example to show how cumbersome it is
    return render_template("fancy_flip.html", 
            coin1outcome=flipCoin(),
            coin2outcome=flipCoin(),
            coin3outcome=flipCoin(),
            coin4outcome=flipCoin(),
            coin5outcome=flipCoin(),
            coin6outcome=flipCoin(),
            coin7outcome=flipCoin(),
            coin8outcome=flipCoin())
    """


#print("hello?", file=sys.stderr)
#print("hello?", file=sys.stderr)
#print("hello?", file=sys.stderr)
#print("hello?", file=sys.stderr)
#print("hello?", file=sys.stderr)
#print("hello?", file=sys.stderr)


#git checkout -b FirstLast_Dev

#make env:
#python -m venv venv

#set source:
#source "C:\Users\frien\Documents\nology\nology-coursework\Python_Flask_Week_3\venv\Scripts\activate"

#"C:\Users\frien.pyenv\pyenv-win\bin\pyenv" install 3.10.5

#"C:\Users\frien.pyenv\pyenv-win\bin\pyenv" local 3.10.5

#"C:\Users\frien.pyenv\pyenv-win\bin\pyenv" local

#will probably need to install flask again
#pip install flask

#export FLASK_APP=app.py
#flask --debug run" or "python -m flask run"

#for output: #print(chance, file=sys.stderr)

#export FLASK_DEBUG=1


#pip install -r requirements.txt

"""
@app.route("/")
def hello_monty():
    return "Hello Monty!"

@app.route("/new")
def hello_new():
    return "Hello Newest Monty!"

@app.route("/math")
def hello_math():
    equation = 15*15*2/1.5
    return str(equation)

@app.route("/fancy")
def html_world():
    return render_template("fancy.html")
"""