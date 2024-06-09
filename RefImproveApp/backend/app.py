# This file will hold the api endpoints using the Flask-Cors library
from flask_cors import CORS
from flask import Flask, request,json
import datetime
from store_ref_improvement import store_comments
from replies import reply

app = Flask(__name__)
CORS(app)

"""This endpoint will get the referee improvement info from the user"""
@app.route("/api/referee-improvement")
def api_login():
    current_date = datetime.datetime.now()
    field_num = 0
    home_team = ""
    away_team = ""
    comment = ""
    if store_comments(current_date,comment,field_num,home_team,away_team):
        response = app.response_class(
            response = json.dumps(reply(comment)),
            status=200,
            mimetype='application/json'
        )
        return response #return as json
    response = app.response_class(
        response =json.dumps("Error when storing comment! Please come back later."),
        status=500,
        mimetype='application/json'
    )
    return 