playfield
=========
A pinball API

Description:
------------
A self contained RESTful API for running pinball tournaments and pinball league seasons.  Intended to be a back end 
microservice that apps could be developed against.

Design:
-------
Flask app fronted by Nginx (uWSGI) and a database to store information.
Intended to be deployed via Docker Compose

API
---
|Class       | Parameters | HTTP Request   | Description  |
| :--------- |:---------| :------------- | :----------: |
| machine  | None         | **GET** /machine/all_machines                           | List all machines currently added     |
| machine  | machine_id   | **GET** /machine/machine_by_id/<id>                      | Get machines with provided id         |
| machine  | machine_name | **GET** /machine/machine_by_name/<name>                 | Get machines with provided name       |
| machine  | abbreviation | **GET** /machine/machine_by_abbr/<abbr>                 | Get machines with specific abbr       |
| machine  | manufacturer | **GET** /machine/machine_by_manufacturer/<manufacturer> | Get machines by provided manufacturer |
| machine  | machine spec | **PUT** /machine/add_machine                            | Add new machine to database           |
| machine  | machine spec | **POST** /machine/update_machine                        | Update machine details                |
| machine  | machine_id   | **DELETE** /machine/delete_machine                      | Remove machine from database          |
| player   | None         | **GET** /player/all_players                             | List all players currently added      |
| player   |              | **GET** /player/active_players                          | List all players that are active      |
| player   | player_id    | **GET** /player/player_by_id/<id>                       | Lookup player by id                   |
| player   | player_name  | **GET** /player/player_by_name/<name>                   | Lookup player by name                 |
| player   | player spec  | **PUT** /player/add_player                              | Add new player to database            |
| player   | player spec  | **POST** /player/update_player                          | Update player details                 |
| player   | player_id    | **DELETE** /player/delete_player                        | Delete player from database           |
| player   |              | **GET** /player/set_status/<player_id>/<status>         | Update player status                  |
| player   |              | **GET** /player/set_active/<player_id>/<active>         | Update player active                  |
| location | None         | **GET** /location/all_locations                         | List all locations                    |
| location |              | **GET** /location/playable_locations                    | List active locations and number of active games at location |
| location | location_id  | **GET** /location/location_by_id/<id>                   | List location by id                   |
| location | location_name| **GET** /location/location_by_name/<name>               | List location by specific name        |
| location | location_spec| **PUT** /location/add_location                          | Add new location to database          |
| location | location_spec| **POST** /location/update_location                      | Update location details               |
| location | location_id  | **DELETE** /location/delete_location                    | Delete location from database         |
| location |              | **GET** /location/set_active/<location_id>/<active>     | Set active on location                |
| location |              | **GET** /location/all_machines_for_location/<location_id> | Get all machines at a location      |
| location |              | **GET** /location/active_machines_for_location/<location_id> | Get all active machines at a location |
| location |              | **POST** /location/add_game_to_location                 | Add game to a location                |
| location |              | **POST** /location/update_game_on_location              | Update game at a location             |
| location |              | **DELETE** /location/delete_game_from_location          | Delete game from a location           |
| location |              | **GET** /location/set_game_active/<game_id><active>     | Set active on game at a location      |

JSON Format:
------------
```
{
  "meta": 
  {
  	"apiVersion": "v1",
	"request_timestamp": "now!"
  },
  "data": [
    {
      "machine_id": "1",
      "name": "Tales of the Arabian Nights",
      "abbr": "TOTAN",
      "manufacturer": "Williams",
      "manDate": "1996",
      "players": "4",
      "gameType": "SS",
      "theme": "Lore",
      "ipdbURL": "http://ipdb.org/machine.cgi?gid=3367"
	},
	{
      "machine_id": "2",
      "name": "Attack From Mars",
      "abbr": "AFM",
      "manufacturer": "Bally",
      "manDate": "1998",
      "players": "4",
      "gameType": "SS",
      "theme": "Aliens",
      "ipdbURL": "http://ipdb.org/machine.cgi?gid=3788"
	}
  ]
}
```


Data:
-----
1.  Machines:  Basic pinball machine data
2.  Players:  Details of people available to participate in league or tournament
3.  Locations:  Details of physical space to play.  Linked to machines present.  Machine state data (details about specific machine at location)

Operations:
-----------
1.  Tournament:  Configuration of a tournament
2.  League:  Configuration of a league
3.  League Season:  A series of tournaments

Diagrams:
---------
Diagrams (*.gz) in the diagrams/ directory are GraphViz format and can be converted into png by running `dot -Tpng -O bin_tree.dot`

Run Locally:
------------
1.  cd to flask directory
2.  `export FLASK_APP=run.py`
    `export FLASK_ENV=development`
3.  Run the app: `flask run`
4.  In browser go to: `http://127.0.0.1:5000/`

Run via Docker:
--------------
1.  In directory with docker-compose.yml: `docker-compose build`
2.  Create & start containers: `docker-compose up`
3.  In browser go to: `http://127.0.0.1`

Shortcut: `docker-compose up --build`