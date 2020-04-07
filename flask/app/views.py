from app import app
from flask import Flask, jsonify
import os
import psycopg2
import psycopg2.extras

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
    general = [
        {
            'status': 'OK',
            'api_version': 'v1'
        }
    ]

    return jsonify(general)


@app.route("/api/v1/resources/machine/all_machines", methods=['GET'])
def all_machines():
    conn = _connect_db()
    dbcur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    dbcur.execute(
        "select * from machines limit 10;")
    entries = dbcur.fetchall()
    dbcur.close()
    conn.close()
    return jsonify(entries)


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


def _connect_db():
    try:
        conn_string = "dbname=%s user=%s host=%s password=%s" % (os.environ['DB_NAME'],
                                                                 os.environ['DB_USER'],
                                                                 os.environ['DB_HOST'],
                                                                 os.environ['DB_PASS'])

        return psycopg2.connect(conn_string)

    except psycopg2.Error as e:
        print("I am unable to connect to the database: {}".format(e.pgerror))
        exit(1)
