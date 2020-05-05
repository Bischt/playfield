from flask import Flask, jsonify, request
from flask_restful import Resource, Api
from .response import Response
from .data import Data


class GetObjectCounts(Resource):

    @staticmethod
    def get():
        query = "SELECT (SELECT count(*) FROM machines) AS machine_count, (SELECT count(*) FROM locations) AS " \
                "location_count, (SELECT count(*) FROM players) AS player_count; "
        data = (None,)

        db_query = Data()
        entries = db_query.read_db(query, None)

        resp = Response(["machine_count", "location_count", "player_count"], entries)
        return_json = resp.get_response_json()

        return return_json
