from app import app
import os
from flask import Flask, jsonify, request

machines = [
    {'id': 0,
     'title': 'Tales of the Arabian Nights',
     'manufacturer': 'Williams',
     'type': 'Solid State',
     'year_published': '1996'},
    {'id': 1,
     'title': 'Lethal Weapon 3',
     'manufacturer': 'Data East',
     'type': 'Solid State',
     'published': '1973'},
    {'id': 2,
     'title': 'Harlem Globetrotters',
     'manufacturer': 'Bally',
     'type': 'Early Solid State',
     'published': '1992'}
]

players = [
    {'id': 0,
     'name': 'bob',
     'ifpa': '1234'},
    {'id': 1,
     'name': 'sue',
     'ifpa': '4321'}
]


@app.route("/", methods=['GET'])
def index():
    data = "OK"

    return jsonify({'data': data})


@app.route("/api/v1/resources/machine/all_machines", methods=['GET'])
def all_machines():
    return jsonify(machines)


@app.route("/api/v1/resources/machine/machine_by_name", methods=['POST'])
def machine_by_name():
    return jsonify(machines)


@app.route("/api/v1/resources/player/all_players", methods=['GET'])
def all_players():
    return jsonify(players)


@app.route("/api/v1/resources/player/player_by_name", methods=['POST'])
def player_by_name():
    return jsonify(players)


@app.errorhandler(404)
def page_not_found(e):
    return "<h1>404</h1><p>The resource could not be found.</p>", 404
