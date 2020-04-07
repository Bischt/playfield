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
| Field          | Description  |
| :------------- | :----------: |
| /machine/all_machines    | List all machines currently added |
| /machine/machine_by_name | List details of specific machine  |
| /player/all_players      | List all players currently added  |
| /player/player_by_name   | Lookup player by name             |

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