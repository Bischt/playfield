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
| machine  | None         | **GET** /machine/all_machines             | List all machines currently added     |
| machine  | machine_name | **GET** /machine/machine_by_name          | Get machines with provided name       |
| machine  | abbreviation | **GET** /machine/machine_by_abbr          | Get machines with specific abbr       |
| machine  | manufacturer | **GET** /machine/machine_by_manufacturer  | Get machines by provided manufacturer |
| machine  | machine spec | **PUT** /machine/create_machine           | Add new machine to database           |
| machine  | machine spec | **POST** /machine/update_machine          | Update machine details                |
| machine  | machine_id   | **DELETE** /machine/delete_machine        | Remove machine from database          |
| player   | None         | **GET** /player/all_players               | List all players currently added      |
| player   | player_name  | **GET** /player/player_by_name            | Lookup player by name                 |
| player   | player spec  | **PUT** /player/create_player             | Add new player to database            |
| player   | player spec  | **POST** /player/update_player            | Update player details                 |
| player   | player_id    | **DELETE** /player/delete_player          | Delete player from database           |
| location | None         | **GET** /location/all_locations           | List all locations                    |

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