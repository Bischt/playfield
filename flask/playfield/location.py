from flask import Flask, jsonify, request
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
    def post():
        name = request.form['name']
        address = request.form['address']
        address_private = request.form['address_private']
        notes = request.form['notes']
        loc_type = request.form['locType']
        active = request.form['active']

        query = "INSERT INTO location (name, address, address_private, notes, loc_type, active) VALUES (%s, %s, %s, " \
                "%s, %s, %s); "
        data = (name, address, address_private, notes, loc_type, active, )

        entries = _write_db(query, data)
        return jsonify(entries)


class UpdateLocation(Resource):

    @staticmethod
    def post():
        location_id = request.form['location_id']
        name = request.form['name']
        address = request.form['address']
        address_private = request.form['address_private']
        notes = request.form['notes']
        loc_type = request.form['locType']
        active = request.form['active']

        query = "UPDATE location SET name=%s, address=%s, address_private=%s, notes=%s, loc_type=%s, active=%s WHERE " \
                "location_id=%s; "
        data = (name, address, address_private, notes, loc_type, active, location_id, )

        entries = _write_db(query, data)
        return jsonify(entries)


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