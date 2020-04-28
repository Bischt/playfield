from flask import Flask, jsonify, request
from flask_restful import Resource, Api
from .response import Response
from .data import Data

field_names = [
    "tournament_id",
    "location_id",
    "name",
    "tournament_datetime",
    "tournament_format",
    "tournament_seeding",
    "active"
]

field_names_tournament_players = [
    "tournament_id",
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


class AllTournaments(Resource):

    @staticmethod
    def get():
        query = "SELECT * FROM tournaments ORDER BY active, tournament_datetime;"
        db_query = Data()
        entries = db_query.read_db(query, None)

        resp = Response(field_names, entries)
        return_json = resp.get_response_json()

        return return_json


class ActiveTournaments(Resource):

    @staticmethod
    def get():
        query = "SELECT * FROM tournaments WHERE active=true ORDER BY tournament_datetime;"
        db_query = Data()
        entries = db_query.read_db(query, None)

        resp = Response(field_names, entries)
        return_json = resp.get_response_json()

        return return_json


class TournamentById(Resource):

    @staticmethod
    def get(id):
        query = "SELECT * FROM tournaments WHERE tournament_id=%s;"
        data = (id,)
        db_query = Data()
        entries = db_query.read_db(query, data)

        resp = Response(field_names, entries)
        return_json = resp.get_response_json()

        return return_json


class TournamentByName(Resource):

    @staticmethod
    def get(name):
        query = "SELECT * FROM tournaments WHERE name=%s;"
        data = (name,)
        db_query = Data()
        entries = db_query.read_db(query, data)

        resp = Response(field_names, entries)
        return_json = resp.get_response_json()

        return return_json


class TournamentByLocation(Resource):

    @staticmethod
    def get(id):
        query = "SELECT * FROM tournaments WHERE location_id=%s;"
        data = (id,)
        db_query = Data()
        entries = db_query.read_db(query, data)

        resp = Response(field_names, entries)
        return_json = resp.get_response_json()

        return return_json


class TournamentPlayers(Resource):

    @staticmethod
    def get(id):
        print("LIST ALL PLAYERS FOR TOURNAMENT: {}".format(id))
        query = "SELECT tournament_players.tournament_id, players.player_id, players.nick, players.name, " \
                "players.email, players.phone, players.location, players.ifpanumber, players.pinside, players.notes, " \
                "players.status, players.active FROM players INNER JOIN tournament_players ON " \
                "players.player_id=tournament_players.player_id WHERE tournament_players.tournament_id=%s;"
        data = (id,)
        db_query = Data()
        entries = db_query.read_db(query, data)

        resp = Response(field_names_tournament_players, entries)
        return_json = resp.get_response_json()

        return return_json


class AddTournament(Resource):

    @staticmethod
    def post():
        location_id = request.form['location_id']
        name = request.form['name']
        tournament_datetime = request.form['tournament_datetime']
        tournament_format = request.form['tournament_format']
        tournament_seeding = request.form['tournament_seeding']
        active = request.form['active']

        query = "INSERT INTO tournaments (location_id, name, tournament_datetime, tournament_format, " \
                "tournament_seeding, active) VALUES (%s, %s, %s, %s, %s, %s); "
        data = (location_id, name, tournament_datetime, tournament_format, tournament_seeding, active,)

        db_query = Data()
        db_query.write_db(query, data)
        return


class UpdateTournament(Resource):

    @staticmethod
    def post():
        tournament_id = request.form['tournament_id']
        location_id = request.form['location_id']
        name = request.form['name']
        tournament_datetime = request.form['tournament_datetime']
        tournament_format = request.form['tournament_format']
        tournament_seeding = request.form['tournament_seeding']
        active = request.form['active']

        query = "UPDATE tournaments SET location_id=%s, name=%s, tournament_datetime=%s, tournament_format=%s, " \
                "tournament_seeding=%s, active=%s WHERE tournament_id=%s; "
        data = (location_id, name, tournament_datetime, tournament_format, tournament_seeding, active, tournament_id,)

        db_query = Data()
        db_query.write_db(query, data)
        return


class DeleteTournament(Resource):

    @staticmethod
    def delete(tournament_id):
        query = "DELETE FROM tournaments WHERE tournament_id=%s;"
        data = (tournament_id,)

        db_query = Data()
        db_query.write_db(query, data)
        return


class SetTournamentActive(Resource):

    @staticmethod
    def get(tournament_id, active):
        query = "UPDATE tournaments SET active=%s WHERE tournament_id=%s;"
        data = (active, tournament_id,)
        db_query = Data()
        db_query.write_db(query, data)

        return


class AddTournamentPlayer(Resource):

    @staticmethod
    def post():
        tournament_id = request.form['tournament_id']
        player_id = request.form['player_id']

        query = "INSERT INTO tournament_players (tournament_id, player_id) VALUES (%s, %s);"
        data = (tournament_id, player_id,)

        db_query = Data()
        db_query.write_db(query, data)

        return


class DeleteTournamentPlayer(Resource):

    @staticmethod
    def post():
        tournament_id = request.form['tournament_id']
        player_id = request.form['player_id']

        query = "DELETE FROM tournament_players WHERE tournament_id=%s AND player_id=%s;"
        data = (tournament_id, player_id,)

        db_query = Data()
        db_query.write_db(query, data)

        return
