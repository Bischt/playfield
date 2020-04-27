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


class AllTournaments(Resource):

    @staticmethod
    def get():
        print("ALL TOURNAMENTS!")


class ActiveTournaments(Resource):

    @staticmethod
    def get():
        print("ACTIVE TOURNAMENTS!")


class TournamentById(Resource):

    @staticmethod
    def get(tournament_id):
        print("TOURNAMENT BY: {}".format(tournament_id))


class TournamentByName(Resource):

    @staticmethod
    def get(tournament_name):
        print("TOURNAMENT BY: {}".format(tournament_name))


class TournamentByLocation(Resource):

    @staticmethod
    def get(location_id):
        print("ALL TOURNAMENTS AT LOCATION: {}".format(location_id))


class TournamentPlayers(Resource):

    @staticmethod
    def get(tournament_id):
        print("LIST ALL PLAYERS FOR TOURNAMENT: {}".format(tournament_id))


class AddTournament(Resource):

    @staticmethod
    def post():
        print("ADDING NEW TOURNAMENT")


class UpdateTournament(Resource):

    @staticmethod
    def post():
        print("UPDATING EXISTING TOURNAMENT")


class DeleteTournament(Resource):

    @staticmethod
    def delete():
        print("DELETING EXISTING TOURNAMENT")


class SetTournamentActive(Resource):

    @staticmethod
    def get(tournament_id, active):
        print("SETTING {} active={}".format(tournament_id, active))


class AddTournamentPlayer(Resource):

    @staticmethod
    def post():
        print("ADDING PLAYER TO TOURNAMENT")


class DeleteTournamentPlayer(Resource):

    @staticmethod
    def post():
        print("REMOVING PLAYER FROM TOURNAMENT")
