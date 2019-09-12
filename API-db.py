from flask import Flask, request, abort, make_response, jsonify
from flask_cors import CORS
import sqlite3
from datetime import datetime

from activity import Activity
import ActivityRepository

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return "Hello world!"

@app.route('/activities', methods=["POST"])
def create_activity():
    if not "type" in request.json or not "reps" in request.json:
        abort(400)

    date = request.json.get("date")
    type = request.json.get("type")
    reps = request.json.get("reps")
    totalTime = request.json.get("totalTime", 0)
    weight = request.json.get("weight", 0)

    try:
        reps = int(reps)
        totalTime = int(totalTime)
        weight = int(weight)
    except:
        return make_response(jsonify("It is not a number"), 400)

    try:
        timestamp = date_string_to_timestamp(date)
        new_activity = Activity(None, timestamp, type, reps, totalTime, weight)
        ActivityRepository.create(new_activity)
        return "activity created"
    except:
        abort(500)

@app.route('/activities', methods=["GET"])
def get_all():
    activity_list = ActivityRepository.get_all()
    for activity in activities:
        activity.date = timestamp_to_date_string(activity.date)
    activities = [activity.to_json() for activity in activity_list]

    return jsonify(activities)

@app.route('/activities/<id>', methods=["GET"])
def get_by(id):
    activity = ActivityRepository.get_by(id)
    if not activity:
        abort(404)

    activity.date = timestamp_to_date_string(activity.date)

    return jsonify(activity.to_json())

@app.route('/activities/<id>', methods=["DELETE"])
def remove_by(id):
    activity = ActivityRepository.get_by(id)
    if not activity:
        abort(404)

    try:
        ActivityRepository.remove(activity)
        return "activity deleted"
    except:
        abort(500)

@app.route('/activities/<id>', methods=["PUT"])
def modify_by(id):
    if "id_act" in request.json:
        return make_response(jsonify("can't modify this"), 400)

    activity = ActivityRepository.get_by(id)
    if not activity:
        abort(404)

    try:
        activity.type = request.json.get("type", activity.type)
        activity.reps = int(request.json.get("reps", activity.reps))
        activity.totalTime = int(request.json.get("totalTime", activity.totalTime))
        activity.weight = int(request.json.get("weight", activity.weight))
    except:
        abort(400)

    try:
        ActivityRepository.edit(activity)
        return jsonify(activity.to_json())
    except:
        abort(500)

@app.errorhandler(400)
def bad_request(error):
    return make_response("bad request", 400)

@app.errorhandler(404)
def not_found(error):
    return make_response("not found", 404)

@app.errorhandler(500)
def internal_server_error(error):
    return make_response("internal server error", 500)

def date_string_to_timestamp(date):
    datetime_object = datetime.strptime(date, '%Y/%m/%d')
    timestamp = int(datetime.timestamp(datetime_object))

    return timestamp

def timestamp_to_date_string(timestamp):
    datetime_object = datetime.fromtimestamp(timestamp)

    year = datetime_object.strftime("%Y")
    month = datetime_object.strftime("%m")
    day = datetime_object.strftime("%d")
    date = datetime_object.strftime("%Y/%m/%d")

    return date

if __name__ == "__main__":
    app.run(debug=True)
