from flask import Flask, jsonify, request
from flask_restful import Resource, Api
import os
import psycopg2
import psycopg2.extras
from .response import Response

field_names = [
    "machine_id",
    "name",
    "abbr",
    "manufacturer",
    "manDate",
    "players",
    "gameType",
    "theme",
    "ipdbURL",
]


class AllMachines(Resource):

    @staticmethod
    def get():
        query = "SELECT * FROM machines LIMIT 10;"
        entries = _read_db(query, None)

        resp = Response(field_names, entries)
        return_json = resp.get_response_json()

        return return_json


class MachineById(Resource):

    @staticmethod
    def get(id):
        query = "SELECT * FROM machines WHERE machine_id=%s"
        data = (id,)
        entries = _read_db(query, data)

        resp = Response(field_names, entries)
        return_json = resp.get_response_json()

        return return_json


class MachineByName(Resource):

    @staticmethod
    def get(name):
        query = "SELECT * FROM machines WHERE name=%s;"
        data = (name,)
        entries = _read_db(query, data)

        resp = Response(field_names, entries)
        return_json = resp.get_response_json()

        return return_json


class MachineByAbbr(Resource):

    @staticmethod
    def get(abbr):
        query = "SELECT * FROM machines WHERE abbr=%s;"
        data = (abbr,)
        entries = _read_db(query, data)

        resp = Response(field_names, entries)
        return_json = resp.get_response_json()

        return return_json


class MachineByManufacturer(Resource):

    @staticmethod
    def get(manufacturer):
        query = "SELECT * FROM machines WHERE manufacturer=%s;"
        data = (manufacturer,)
        entries = _read_db(query, data)

        resp = Response(field_names, entries)
        return_json = resp.get_response_json()

        return return_json


class AddMachine(Resource):

    @staticmethod
    def post():
        name = request.form['name']
        abbr = request.form['abbr']
        manufacturer = request.form['manufacturer']
        manDate = request.form['manDate']
        players = request.form['players']
        gameType = request.form['gameType']
        theme = request.form['theme']
        ipdbURL = request.form['ipdbURL']

        query = "INSERT INTO machines (name, abbr, manufacturer, manDate, players, gameType, theme, ipdbURL) VALUES (" \
                "%s, %s, %s, %s, %s, %s, %s, %s); "
        data = (name, abbr, manufacturer, manDate, players, gameType, theme, ipdbURL, )

        _write_db(query, data)
        return


def _read_db(query, data):
    """
    Fetch data from the db
    :param query:
    :return:
    """
    # Create connection and cursor
    connection = _connect_db()
    dict_cursor = connection.cursor(cursor_factory=psycopg2.extras.DictCursor)
    # Run the query
    if data is not None:
        dict_cursor.execute(query, data)
    else:
        dict_cursor.execute(query)
    # Get all results
    entries = dict_cursor.fetchall()
    # Clean up DB connection
    dict_cursor.close()
    connection.close()

    return entries


def _write_db(query, data):
    """
    Perform db modifications (create, update, delete)
    :param query:
    :param data:
    :return:
    """
    # Create connection and cursor
    connection = _connect_db()
    dict_cursor = connection.cursor(cursor_factory=psycopg2.extras.DictCursor)
    # Run the query
    if data is not None:
        dict_cursor.execute(query, data)
    else:
        dict_cursor.execute(query)
    # commit changes
    connection.commit()
    # Clean up DB connection
    dict_cursor.close()
    connection.close()

    return


def _connect_db():
    """
    Establish db connection for read operations
    :return:
    """
    try:
        conn_string = "dbname=%s user=%s host=%s password=%s" % (os.environ['DB_NAME'],
                                                                 os.environ['DB_USER'],
                                                                 os.environ['DB_HOST'],
                                                                 os.environ['DB_PASS'])

        # Return DB connection handle
        return psycopg2.connect(conn_string)

    except psycopg2.Error as e:
        print("I am unable to connect to the database: {}".format(e.pgerror))
        exit(1)
