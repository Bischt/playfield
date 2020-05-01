from flask import Flask, jsonify, request
from flask_restful import Resource, Api
from .response import Response
from .data import Data

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
        db_query = Data()
        entries = db_query.read_db(query, None)

        resp = Response(field_names, entries)
        return_json = resp.get_response_json()

        return return_json


class MachineById(Resource):

    @staticmethod
    def get(id):
        query = "SELECT * FROM machines WHERE machine_id=%s"
        data = (id,)
        db_query = Data()
        entries = db_query.read_db(query, data)

        resp = Response(field_names, entries)
        return_json = resp.get_response_json()

        return return_json


class MachineByName(Resource):

    @staticmethod
    def get(name):
        query = "SELECT * FROM machines WHERE name=%s;"
        data = (name,)
        db_query = Data()
        entries = db_query.read_db(query, data)

        resp = Response(field_names, entries)
        return_json = resp.get_response_json()

        return return_json


class MachineByAbbr(Resource):

    @staticmethod
    def get(abbr):
        query = "SELECT * FROM machines WHERE abbr=%s;"
        data = (abbr,)
        db_query = Data()
        entries = db_query.read_db(query, data)

        resp = Response(field_names, entries)
        return_json = resp.get_response_json()

        return return_json


class MachineByManufacturer(Resource):

    @staticmethod
    def get(manufacturer):
        query = "SELECT * FROM machines WHERE manufacturer=%s;"
        data = (manufacturer,)
        db_query = Data()
        entries = db_query.read_db(query, data)

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

        db_query = Data()
        db_query.write_db(query, data)
        return


class UpdateMachine(Resource):

    @staticmethod
    def post():
        machine_id = request.form['machine_id']
        name = request.form['name']
        abbr = request.form['abbr']
        manufacturer = request.form['manufacturer']
        manDate = request.form['manDate']
        players = request.form['players']
        gameType = request.form['gameType']
        theme = request.form['theme']
        ipdbURL = request.form['ipdbURL']

        query = "UPDATE machines SET name=%s, abbr=%s, manufacturer=%s, manDate=%s, players=%s, gameType=%s, " \
                "theme=%s, ipdbURL=%s WHERE machine_id=%s "
        data = (name, abbr, manufacturer, manDate, players, gameType, theme, ipdbURL, machine_id,)
        db_query = Data()
        db_query.write_db(query, data)
        return


class DeleteMachine(Resource):

    @staticmethod
    def delete(machine_id):

        query = "DELETE FROM machines WHERE machine_id=%s;"
        data = (machine_id,)

        db_query = Data()
        db_query.write_db(query, data)

        return


class MachineCount(Resource):

    @staticmethod
    def get():

        query = "SELECT count(*) FROM machines;"
        data = (None,)

        db_query = Data()
        entries = db_query.read_db(query, data)

        resp = Response(["count"], entries)
        return_json = resp.get_response_json()

        return return_json
