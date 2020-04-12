from flask import Flask, jsonify
from flask_restful import Resource, Api
import os
import psycopg2
import psycopg2.extras


class AllLocations(Resource):

    @staticmethod
    def get():
        query = "SELECT * FROM locations;"
        entries = _read_db(query, None)
        return jsonify(entries)


class LocationById(Resource):

    @staticmethod
    def get(name):
        query = "SELECT * FROM locations WHERE location_id=%s;"
        data = (id, )
        entries = _read_db(query, data)
        return jsonify(entries)


class LocationByName(Resource):

    @staticmethod
    def get(name):
        query = "SELECT * FROM locations WHERE name=%s;"
        data = (name, )
        entries = _read_db(query, data)
        return jsonify(entries)


class AddLocation(Resource):

    @staticmethod
    def put():

        return "PUT METHOD WORKS!"


class UpdateLocation(Resource):

    @staticmethod
    def post():

        return "POST METHOD WORKS!"


class DeleteLocation(Resource):

    @staticmethod
    def delete():
        
        return "DELETE METHOD WORKS!"


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