# main_handler.py
import requests
import flask

app = flask.Flask(__name__)

@app.route("/", methods=["GET"])
def welcome():
    return flask.jsonify({"Mensaje": "Bienvenido al Microservicio CRUD"})

@app.route("/user", methods=["POST"])
def create():
    res = requests.post("http://localhost:5001/create", json=flask.request.json)
    return flask.jsonify(res.json()), res.status_code

@app.route("/user", methods=["GET"])
def read():
    res = requests.get("http://localhost:5002/read", params=flask.request.args)
    return flask.jsonify(res.json()), res.status_code

@app.route("/user", methods=["PUT"])
def update():
    res = requests.put("http://localhost:5003/update", json=flask.request.json)
    return flask.jsonify(res.json()), res.status_code

@app.route("/user", methods=["DELETE"])
def delete():
    res = requests.delete("http://localhost:5004/delete", params=flask.request.args)
    return flask.jsonify(res.json()), res.status_code

if __name__ == "__main__":
    app.run(port=5000)
