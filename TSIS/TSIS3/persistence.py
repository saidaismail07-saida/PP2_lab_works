import json
import os

SETTINGS = "settings.json"
LEADERBOARD = "leaderboard.json"


def load_settings():
    if not os.path.exists(SETTINGS):
        return {"sound": True, "car_color": "red", "difficulty": 1}
    return json.load(open(SETTINGS))


def save_settings(data):
    json.dump(data, open(SETTINGS, "w"), indent=4)


def load_leaderboard():
    if not os.path.exists(LEADERBOARD):
        return []
    return json.load(open(LEADERBOARD))


def save_leaderboard(data):
    data = sorted(data, key=lambda x: x["score"], reverse=True)[:10]
    json.dump(data, open(LEADERBOARD, "w"), indent=4)