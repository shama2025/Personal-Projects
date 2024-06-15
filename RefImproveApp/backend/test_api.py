# File will hold the api tests for this application
import pytest
import requests

url = "http://127.0.0.1:5000"

"""Tests the request json objects request to the API"""


def test_referee_improvement():
    ref_improve_obj = {
        "field_num": 5,
        "home_team": "Team 1",
        "away_team": "Team 2",
        "comment": "These referees were terrible and cannot call basic penalties!",
    }
    res = requests.get(f"{url}/api/referee-improvement", params=ref_improve_obj)
    print(type(res.status_code))
    if res.status_code == 200:
        assert True
    else:
        assert False
