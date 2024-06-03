# This file will hold the api endpoints using the Flask-Cors library
from flask_cors import CORS
from flask import Flask, request
import datetime
from store_ref_improvement import store_comments, reply

app = Flask(__name__)
CORS(app)

"""This endpoint will get the referee improvement info from the user"""
@app.route("/api/referee-improvement")
def api_login():
    current_date = datetime.datetime.now()
    if store_comments:
        return reply
    return "Bad"