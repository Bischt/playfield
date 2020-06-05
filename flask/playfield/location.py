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

field_names_games = [
    "location_id",
    "name",
    "address",
    "addressPrivate",
    "notes",
    "locType",
    "gamecount"
]

field_names_location_machines = [
    "game_id",
    "machine_id",
    "condition",
    "notes",
    "name",
    "abbr",
    "manufacturer",
    "manDate",
    "players",
    "gameType",
    "theme",
    "ipdbURL"
]


class AllLocations(Resource):

    @staticmethod
    def get():
        query = "SELECT * FROM locations ORDER BY active;"
        db_query = Data()
        entries = db_query.read_db(query, None)

        resp = Response(field_names, entries)
        return_json = resp.get_response_json()

        return return_json


class PlayableLocations(Resource):

    @staticmethod
    def get():
        query = "SELECT locations.location_id, locations.name, locations.address, locations.addressPrivate, " \
                "locations.notes, locations.locType, count(*) as gamecount FROM locations INNER JOIN " \
                "locations_machines on locations.location_id=locations_machines.location_id WHERE " \
                "locations.active=true AND locations_machines.active=true GROUP BY locations.location_id; "
        db_query = Data()
        entries = db_query.read_db(query, None)

        resp = Response(field_names_games, entries)
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


class AllMachinesForLocation(Resource):

    @staticmethod
    def get(id):
        query = "SELECT locations_machines.game_id, locations_machines.machine_id, locations_machines.condition, " \
                "locations_machines.notes, machines.name, machines.abbr, machines.manufacturer, machines.manDate, " \
                "machines.players, machines.gameType, machines.theme, machines.ipdbURL FROM locations_machines INNER " \
                "JOIN machines on locations_machines.machine_id=machines.machine_id WHERE " \
                "locations_machines.location_id=%s; "
        data = (id, )
        db_query = Data()
        entries = db_query.read_db(query, data)

        resp = Response(field_names_location_machines, entries)
        return_json = resp.get_response_json()

        return return_json


class ActiveMachinesForLocation(Resource):

    @staticmethod
    def get(id):
        query = "SELECT locations_machines.game_id, locations_machines.machine_id, locations_machines.condition, " \
                "locations_machines.notes, machines.name, machines.abbr, machines.manufacturer, machines.manDate, " \
                "machines.players, machines.gameType, machines.theme, machines.ipdbURL FROM locations_machines INNER " \
                "JOIN machines on locations_machines.machine_id=machines.machine_id WHERE " \
                "locations_machines.location_id=%s AND locations_machines.active=true; "
        data = (id, )
        db_query = Data()
        entries = db_query.read_db(query, data)

        resp = Response(field_names_location_machines, entries)
        return_json = resp.get_response_json()

        return return_json


class AddGameToLocation(Resource):

    @staticmethod
    def post():
        location_id = request.form['location_id']
        machine_id = request.form['machine_id']
        name = request.form['name']
        condition = request.form['condition']
        notes = request.form['notes']
        active = request.form['active']

        query = "INSERT INTO locations_machines (location_id, machine_id, name, condition, notes, active) VALUES (%s, " \
                "%s, %s, %s, %s, %s); "
        data = (location_id, machine_id, name, condition, notes, active,)

        db_query = Data()
        db_query.write_db(query, data)
        return


class UpdateGameOnLocation(Resource):

    @staticmethod
    def post():
        game_id = request.form['game_id']
        location_id = request.form['location_id']
        machine_id = request.form['machine_id']
        name = request.form['name']
        condition = request.form['condition']
        notes = request.form['notes']
        active = request.form['active']

        query = "UPDATE locations_machines SET location_id=%s, machine_id=%s, name=%s, condition=%s, notes=%s, " \
                "active=%s WHERE game_id=%s; "
        data = (location_id, machine_id, name, condition, notes, active, game_id)

        db_query = Data()
        db_query.write_db(query, data)
        return


class DeleteGameFromLocation(Resource):

    @staticmethod
    def delete(game_id):

        query = "DELETE FROM locations_machines WHERE game_id=%s;"
        data = (game_id,)

        db_query = Data()
        db_query.write_db(query, data)

        return


class SetGameActive(Resource):

    @staticmethod
    def get(game_id, active):
        query = "UPDATE locations_machines SET active=%s WHERE game_id=%s;"
        data = (active, game_id,)
        db_query = Data()
        db_query.write_db(query, data)

        return


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
        loc_type = request.form['loc_type']
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
        address_private = request.form['addressPrivate']
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
    def delete(location_id):

        query = "DELETE FROM locations WHERE location_id=%s;"
        data = (location_id,)

        db_query = Data()
        db_query.write_db(query, data)
        return


class SetLocationActive(Resource):

    @staticmethod
    def get(location_id, active):
        query = "UPDATE locations SET active=%s WHERE location_id=%s;"
        data = (active, location_id,)
        db_query = Data()
        db_query.write_db(query, data)

        return


class LocationCount(Resource):

    @staticmethod
    def get():
        query = "SELECT count(*) FROM locations;"
        data = (None,)

        db_query = Data()
        entries = db_query.read_db(query, data)

        resp = Response(["count"], entries)
        return_json = resp.get_response_json()

        return return_json
