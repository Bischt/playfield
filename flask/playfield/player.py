from flask import Flask, jsonify
from flask_restful import Resource, Api
import os
import psycopg2
import psycopg2.extras
from .response import Response

field_names = [
    "player_id",
    "nick",
    "name",
    "email",
    "phone",
    "location",
    "ifpanumber",
    "pinside",
    "notes",
    "status",
    "active",
    "currentrank",
    "currentwpprvalue",
    "bestfinish",
    "activeevents"
]


class AllPlayers(Resource):

    @staticmethod
    def get():
        query = "SELECT * FROM players;"
        entries = _read_db(query, None)

        resp = Response(field_names, entries)
        return_json = resp.get_response_json()

        return return_json


class PlayerById(Resource):

    @staticmethod
    def get(id):
        query = "SELECT * FROM players WHERE player_id=%s;"
        data = (id, )
        entries = _read_db(query, data)
        return jsonify(entries)


class PlayerByName(Resource):

    @staticmethod
    def get(name):
        query = "SELECT * FROM players WHERE name=%s;"
        data = (name, )
        entries = _read_db(query, data)
        return jsonify(entries)


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