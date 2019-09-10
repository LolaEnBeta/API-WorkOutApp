from flask import Flask, request, abort, make_response, jsonify
import sqlite3
from activity import Activity
import ActivityRepository

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello world!"

@app.route('/activities', methods=["POST"])
def create_activity():
    if not "type" in request.json or not "reps" in request.json:
        abort(400)

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

    new_activity = Activity(None, type, reps, totalTime, weight)
    result = ActivityRepository.create(new_activity)

    return result

@app.route('/activities', methods=["GET"])
def get_all():
    activity_list = ActivityRepository.get_all()
    activities = [activity.to_json() for activity in activity_list]

    response = jsonify(activities)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/activities/<id>', methods=["GET"])
def get_by(id):
    activity = ActivityRepository.get_by(id)
    if not activity:
        abort(404)

    response = jsonify(activity.to_json())
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

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

if __name__ == "__main__":
    app.run(debug=True)
