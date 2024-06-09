# This file will hold the api endpoints using the Flask-Cors library
from flask_cors import CORS
from flask import Flask, request,json,jsonify
import datetime
from store_ref_improvement import store_comments
from replies import reply

app = Flask(__name__)
CORS(app)

"""This endpoint will get the referee improvement info from the user"""
@app.route("/api/referee-improvement")
def api_login():
    current_date = datetime.datetime.now()
    comment = request.args.get("comment")
    field_num = request.args.get('field_num')
    home_team = request.args.get('home_team')
    away_team = request.args.get('away_team')
    if store_comments(current_date,comment,field_num,home_team,away_team):
        response = app.response_class(
            response = json.dumps(reply(comment)),
            status=200,
            mimetype='application/json'
        )
        return response
    response = app.response_class(
        response =json.dumps("Error when storing comment! Please come back later."),
        status=500,
        mimetype='application/json'
    )
    return response