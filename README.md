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
| player   | player_id    | **GET** /player/player_by_id/<id>                       | Lookup player by id                   |
| player   | player_name  | **GET** /player/player_by_name/<name>                   | Lookup player by name                 |
| player   | player spec  | **PUT** /player/add_player                              | Add new player to database            |
| player   | player spec  | **POST** /player/update_player                          | Update player details                 |
| player   | player_id    | **DELETE** /player/delete_player                        | Delete player from database           |
| location | None         | **GET** /location/all_locations                         | List all locations                    |
| location | location_id  | **GET** /location/location_by_id/<id>                   | List location by id                   |
| location | location_name| **GET** /location/location_by_name/<name>               | List location by specific name        |
| location | location_spec| **PUT** /location/add_location                          | Add new location to database          |
| location | location_spec| **POST** /location/update_location                      | Update location details               |
| location | location_id  | **DELETE** /location/delete_location                    | Delete location from database         |

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