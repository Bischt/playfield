drop table if exists player;
create table player (
  player_id SERIAL primary key not null,
  nick varchar(255),
  name varchar(255),
  email varchar(255),
  phone varchar(25),
  location varchar(255),
  ifpanumber varchar(10),
  pinside varchar(30),
  notes text,
  status integer,
  active boolean not null,
  currentrank integer,
  currentwpprvalue double precision,
  bestfinish integer,
  activeevents integer
);

drop table if exists machines;
create table machines (
  machine_id SERIAL primary key not null,
  name varchar(255) not null,
  abbr varchar(50),
  manufacturer varchar(150),
  manDate varchar(100),
  players varchar(2),
  gameType varchar(5),
  theme varchar(150),
  ipdbURL varchar(150)
);

drop table if exists locations;
create table locations (
  location_id SERIAL primary key not null,
  name varchar(255) not null,
  address varchar(255),
  addressPrivate boolean,
  notes text,
  locType integer,
  active boolean
);

drop table if exists locations_machines;
create table locations_machines (
  game_id SERIAL primary key not null,
  location_id integer not null,
  machine_id integer not null,
  name varchar(255) not null,
  condition text,
  notes text,
  active boolean
);

drop table if exists league;
create table league (
  league_id SERIAL primary key not null,
  name varchar(255)
);

drop table if exists league_players;
create table league_players (
  league_id integer not null,
  player_id integer not null
);

drop table if exists season;
create table season (
  season_id SERIAL primary key not null,
  league_id integer not null,
  series_id integer,
  name varchar(255)
);

drop table if exists tournament;
create table tournament (
  tournament_id SERIAL primary key not null,
  location_id integer,
  name varchar(255)
);

drop table if exists tournament_players;
create table tournament_players (
  tournament_id integer not null,
  player_id integer not null
);

drop table if exists tournament_series;
create table tournament_series (
  tournament_id integer not null,
  series_id integer not null
);

drop table if exists match;
create table match (
  match_id SERIAL primary key not null,
  tournament_id integer not null,
  machine_id integer not null,
  name varchar(255)
);

drop table if exists match_players;
create table match_players (
  match_id integer not null,
  player_id integer not null,
  score varchar(255)
);