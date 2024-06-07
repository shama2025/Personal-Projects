import pytest
import requests

url = "http://127.0.0.1:5000"

"""Tests the request json objects request to the API"""
def test_referee_improvement():
    ref_improve_obj = {
        "field_num" :5,
        "home_team" : "Team 1",
        "away_team" : "Team 2",
        "comment" : "These referees were terrible and cannot call basic penalties!"
    }
    res = requests.post(f"{url}/api/referee-improvement")
    if res.status_code == 200:
        return True
    return False
