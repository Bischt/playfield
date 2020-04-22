from flask import Flask, jsonify, request
from flask_restful import Resource, Api
from .response import Response
from .data import Data

field_names = [
    "location_id",
    "name",
    "address",
    "addressPrivate",
    "notes",
    "locType",
    "active"
]


class AllLocations(Resource):

    @staticmethod
    def get():
        query = "SELECT * FROM locations;"
        db_query = Data()
        entries = db_query.read_db(query, None)

        resp = Response(field_names, entries)
        return_json = resp.get_response_json()

        return return_json


class LocationById(Resource):

    @staticmethod
    def get(id):
        query = "SELECT * FROM locations WHERE location_id=%s;"
        data = (id, )
        db_query = Data()
        entries = db_query.read_db(query, data)

        resp = Response(field_names, entries)
        return_json = resp.get_response_json()

        return return_json


class LocationByName(Resource):

    @staticmethod
    def get(name):
        query = "SELECT * FROM locations WHERE name=%s;"
        data = (name, )
        db_query = Data()
        entries = db_query.read_db(query, data)

        resp = Response(field_names, entries)
        return_json = resp.get_response_json()

        return return_json


class AddLocation(Resource):

    @staticmethod
    def post():
        name = request.form['name']
        address = request.form['address']
        address_private = request.form['address_private']
        notes = request.form['notes']
        loc_type = request.form['locType']
        active = request.form['active']

        query = "INSERT INTO locations (name, address, addressPrivate, notes, locType, active) VALUES (%s, %s, %s, " \
                "%s, %s, %s); "
        data = (name, address, address_private, notes, loc_type, active, )

        db_query = Data()
        db_query.write_db(query, data)
        return


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

        query = "UPDATE locations SET name=%s, address=%s, addressPrivate=%s, notes=%s, locType=%s, active=%s WHERE " \
                "location_id=%s; "
        data = (name, address, address_private, notes, loc_type, active, location_id, )

        db_query = Data()
        db_query.write_db(query, data)
        return


class DeleteLocation(Resource):

    @staticmethod
    def delete():

        return "DELETE METHOD WORKS!"
