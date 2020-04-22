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
        query = "SELECT * FROM players;"
        db_query = Data()
        entries = db_query.read_db(query, None)

        resp = Response(field_names, entries)
        return_json = resp.get_response_json()

        return return_json


class PlayerById(Resource):

    @staticmethod
    def get(id):
        query = "SELECT * FROM players WHERE player_id=%s;"
        data = (id, )
        db_query = Data()
        entries = db_query.read_db(query, data)

        resp = Response(field_names, entries)
        return_json = resp.get_response_json()

        return return_json


class PlayerByName(Resource):

    @staticmethod
    def get(name):
        query = "SELECT * FROM players WHERE name=%s;"
        data = (name, )
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
        currentrank = request.form['currentrank']
        currentwpprvalue = request.form['currentwpprvalue']
        bestfinish = request.form['bestfinish']
        activeevents = request.form['activeevents']

        query = "INSERT INTO players (nick, name, email, phone, location, ifpanumber, pinside, notes, status, active, " \
                "currentrank, currentwpprvalue, bestfinish, activeevents) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, " \
                "%s, %s, %s, %s, %s); "
        data = (nick, name, email, phone, location, ifpanumber, pinside, notes, status, active, currentrank, currentwpprvalue, bestfinish, activeevents, )

        db_query = Data()
        db_query.write_db(query, data)
        return
