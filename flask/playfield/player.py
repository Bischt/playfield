from flask import Flask, jsonify, request
from flask_restful import Resource, Api
from .response import Response
from .data import Data

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
        query = "SELECT * FROM players ORDER BY name;"
        db_query = Data()
        entries = db_query.read_db(query, None)

        resp = Response(field_names, entries)
        return_json = resp.get_response_json()

        return return_json


class ActivePlayers(Resource):

    @staticmethod
    def get():
        query = "SELECT * FROM players WHERE active=True;"
        db_query = Data()
        entries = db_query.read_db(query, None)

        resp = Response(field_names, entries)
        return_json = resp.get_response_json()

        return return_json


class PlayerById(Resource):

    @staticmethod
    def get(id):
        query = "SELECT * FROM players WHERE player_id=%s;"
        data = (id,)
        db_query = Data()
        entries = db_query.read_db(query, data)

        resp = Response(field_names, entries)
        return_json = resp.get_response_json()

        return return_json


class PlayerByName(Resource):

    @staticmethod
    def get(name):
        query = "SELECT * FROM players WHERE name=%s;"
        data = (name,)
        db_query = Data()
        entries = db_query.read_db(query, data)

        resp = Response(field_names, entries)
        return_json = resp.get_response_json()

        return return_json


class AddPlayer(Resource):

    @staticmethod
    def post():
        name = request.form['name']
        nick = request.form['nick']
        email = request.form['email']
        phone = request.form['phone']
        location = request.form['location']
        ifpanumber = request.form['ifpanumber']
        pinside = request.form['pinside']
        notes = request.form['notes']
        status = request.form['status']
        active = request.form['active']

        query = "INSERT INTO players (nick, name, email, phone, location, ifpanumber, pinside, notes, status, " \
                "active) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s); "
        data = (nick, name, email, phone, location, ifpanumber, pinside, notes, status, active,)

        db_query = Data()
        db_query.write_db(query, data)
        return


class UpdatePlayer(Resource):

    @staticmethod
    def post():
        player_id = request.form['player_id']
        name = request.form['name']
        nick = request.form['nick']
        email = request.form['email']
        phone = request.form['phone']
        location = request.form['location']
        ifpanumber = request.form['ifpanumber']
        pinside = request.form['pinside']
        notes = request.form['notes']
        status = request.form['status']
        active = request.form['active']

        query = "UPDATE players SET name=%s, nick=%s, email=%s, phone=%s, location=%s, ifpanumber=%s, pinside=%s, " \
                "notes=%s, status=%s, active=%s WHERE player_id=%s; "
        data = (name, nick, email, phone, location, ifpanumber, pinside, notes, status, active, player_id,)
        db_query = Data()
        db_query.write_db(query, data)

        return


class DeletePlayer(Resource):

    @staticmethod
    def delete(player_id):

        query = "DELETE FROM players WHERE player_id=%s;"
        data = (player_id,)

        db_query = Data()
        db_query.write_db(query, data)

        return


class SetStatus(Resource):

    @staticmethod
    def get(player_id, status):
        query = "UPDATE players SET status=%s WHERE player_id=%s;"
        data = (status, player_id,)
        db_query = Data()
        db_query.write_db(query, data)

        return


class SetPlayerActive(Resource):

    @staticmethod
    def get(player_id, active):
        query = "UPDATE players SET active=%s WHERE player_id=%s;"
        data = (active, player_id,)
        db_query = Data()
        db_query.write_db(query, data)

        return


class PlayerCount(Resource):

    @staticmethod
    def get():
        query = "SELECT count(*) FROM players;"
        data = (None,)

        db_query = Data()
        entries = db_query.read_db(query, data)

        resp = Response(["count"], entries)
        return_json = resp.get_response_json()

        return return_json
