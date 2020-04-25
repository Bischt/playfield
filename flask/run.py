from flask_restful import Resource, Api
from flask import Flask, jsonify

from playfield import machine
from playfield import player
from playfield import location

app = Flask(__name__)
# Use Flask RESTful API
api = Api(app)

# Add API endpoints
api.add_resource(machine.AllMachines, '/api/v1/resources/machine/all_machines')
api.add_resource(machine.MachineById, '/api/v1/resources/machine/machine_by_id/<int:id>')
api.add_resource(machine.MachineByName, '/api/v1/resources/machine/machine_by_name/<string:name>')
api.add_resource(machine.MachineByAbbr, '/api/v1/resources/machine/machine_by_abbr/<string:abbr>')
api.add_resource(machine.MachineByManufacturer, '/api/v1/resources/machine/machine_by_manufacturer/<string'
                                                ':manufacturer>')
api.add_resource(machine.AddMachine, '/api/v1/resources/machine/add_machine')
api.add_resource(machine.UpdateMachine, '/api/v1/resources/machine/update_machine')
api.add_resource(machine.DeleteMachine, '/api/v1/resources/machine/delete_machine')

api.add_resource(player.AllPlayers, '/api/v1/resources/player/all_players')
api.add_resource(player.ActivePlayers, '/api/v1/resources/player/active_players')
api.add_resource(player.PlayerById, '/api/v1/resources/player/player_by_id/<int:id>')
api.add_resource(player.PlayerByName, '/api/v1/resources/player/player_by_name/<string:name>')
api.add_resource(player.AddPlayer, '/api/v1/resources/player/add_player')
api.add_resource(player.UpdatePlayer, '/api/v1/resources/player/update_player')
api.add_resource(player.DeletePlayer, '/api/v1/resources/player/delete_player')
api.add_resource(player.SetStatus, '/api/v1/resources/player/set_status/<int:player_id>/<int:status>')
api.add_resource(player.SetPlayerActive, '/api/v1/resources/player/set_active/<int:player_id>/<string:active>')

api.add_resource(location.AllLocations, '/api/v1/resources/location/all_locations')
api.add_resource(location.PlayableLocations, '/api/v1/resources/location/playable_locations')
api.add_resource(location.LocationById, '/api/v1/resources/location/location_by_id/<int:id>')
api.add_resource(location.LocationByName, '/api/v1/resources/location/location_by_name/<string:name>')
api.add_resource(location.AddLocation, '/api/v1/resources/location/add_location')
api.add_resource(location.UpdateLocation, '/api/v1/resources/location/update_location')
api.add_resource(location.DeleteLocation, '/api/v1/resources/location/delete_location')
api.add_resource(location.SetLocationActive, '/api/v1/resources/location/set_active/<int:location_id>/<string:active>')

api.add_resource(location.AllMachinesForLocation, '/api/v1/resources/location/all_machines_for_location/<int:id>')
api.add_resource(location.ActiveMachinesForLocation, '/api/v1/resources/location/active_machines_for_location/<int:id>')
api.add_resource(location.AddGameToLocation, '/api/v1/resources/location/add_game_to_location')
api.add_resource(location.UpdateGameOnLocation, '/api/v1/resources/location/update_game_on_location')
api.add_resource(location.DeleteGameFromLocation, '/api/v1/resources/location/delete_game_from_location')
api.add_resource(location.SetGameActive, '/api/v1/resources/location/set_game_active/<int:game_id><string:active>')

# Define general non API endpoints
deployed_version = "v1"


@app.route("/", methods=['GET'])
def index():
    info = [
        {
            'live': check_live(),
            'ready': check_ready(),
            'api_version': deployed_version,
            'app_name': 'Playfield',
            'github': 'https://github.com/Bischt/playfield'
        }
    ]

    return jsonify(info)


@app.route("/version", methods=['GET'])
def version():
    return jsonify({'api_version': deployed_version})


@app.route("/ready", methods=['GET'])
def ready():
    return jsonify({'ready': check_ready()})


@app.route("/live", methods=['GET'])
def live():
    return jsonify({'live': check_live()})


@app.errorhandler(404)
def page_not_found(e):
    return "<h1>404</h1><p>The resource could not be found.</p>", 404


def check_live():
    return "OK"


def check_ready():
    return "OK"


if __name__ == "__main__":
    app.run(debug=True)
