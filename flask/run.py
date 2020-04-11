from flask import Flask, jsonify
from flask_restful import Resource, Api
from flask import Flask, jsonify

from playfield import read

app = Flask(__name__)
# Use Flask RESTful API
api = Api(app)

# Add API endpoints
api.add_resource(read.AllMachines, '/api/v1/resources/machine/all_machines')
api.add_resource(read.AllPlayers, '/api/v1/resources/player/all_players')
api.add_resource(read.AllLocations, '/api/v1/resources/location/all_locations')


# Define general non API endpoints
@app.route("/", methods=['GET'])
def index():
    general = [
        {
            'status': 'OK',
            'api_version': 'v1'
        }
    ]

    return jsonify(general)


@app.errorhandler(404)
def page_not_found(e):
    return "<h1>404</h1><p>The resource could not be found.</p>", 404


if __name__ == "__main__":
    app.run(debug=True)
