from flask import Flask, jsonify
from flask_restful import Resource, Api
import os
import psycopg2
import psycopg2.extras


class AllMachines(Resource):

    @staticmethod
    def get():
        query = "SELECT * FROM machines LIMIT 10;"
        entries = _read_db(query)
        return jsonify(entries)


class AllPlayers(Resource):

    @staticmethod
    def get():
        query = "SELECT * FROM players;"
        entries = _read_db(query)
        return jsonify(entries)


class AllLocations(Resource):

    @staticmethod
    def get():
        query = "SELECT * FROM locations;"
        entries = _read_db(query)
        return jsonify(entries)


def _read_db(query):
    """
    Fetch data from the db
    :param query:
    :return:
    """
    # Create connection and cursor
    connection = _connect_db()
    dict_cursor = connection.cursor(cursor_factory=psycopg2.extras.DictCursor)
    # Run the query
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