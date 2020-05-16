################################
# Final Exam
# ENGI 1006
# Name: Hannah Luo
# UNI: hrl2116
# File app.py contains the routes of the server
################################
"""
Created on Tue Apr 21 14:57:17 2020

@author: hrl2116
"""

#import statements
from flask import Flask, render_template

#Flask app variable
app = Flask(__name__)

#static route
'''for the homepage'''
@app.route("/")
def hello():
    #return "Hello World!"
    return render_template("index.html")

'''for the assignments page'''
@app.route("/assignments")
def test123():
    return render_template("1006.html")

'''for the classes page'''
@app.route("/classes")
def blah():
    return render_template("classes.html")

#start the server
if __name__ == "__main__":
    app.run()