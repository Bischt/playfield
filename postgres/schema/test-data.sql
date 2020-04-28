INSERT INTO locations (name, address, addressPrivate, notes, locType, active) VALUES ('Pinball Alley', '645 Multiball Rd', false, '', 1, true);

INSERT INTO locations (name, address, addressPrivate, notes, locType, active) VALUES ('Pinbar', '2 Right Orbit Rd', false, '', 1, true);

INSERT INTO locations (name, address, addressPrivate, notes, locType, active) VALUES ('Space Force One', '4 Left Orbit Rd', false, '', 1, true);

INSERT INTO locations (name, address, addressPrivate, notes, locType, active) VALUES ('John''s House', '123 Any Street', true, '', 1, true);

INSERT INTO locations (name, address, addressPrivate, notes, locType, active) VALUES ('1up', '6556 Kickback Dr', false, '', 1, true);

INSERT INTO locations (name, address, addressPrivate, notes, locType, active) VALUES ('2up', '3 Drop Target Rd', false, '', 1, true);

INSERT INTO locations (name, address, addressPrivate, notes, locType, active) VALUES ('Mini Boss', '889 Center Drain Ln', false, '', 1, true);

INSERT INTO locations (name, address, addressPrivate, notes, locType, active) VALUES ('Lvl Up', '3432 Shooter Ln', false, '', 1, true);

INSERT INTO locations (name, address, addressPrivate, notes, locType, active) VALUES ('Pinball Classic', '56 Standup Target Rd', false, '', 1, true);

INSERT INTO locations (name, address, addressPrivate, notes, locType, active) VALUES ('Barcade', '5 Pop Bumper Ct', false, '', 1, true);

INSERT INTO locations (name, address, addressPrivate, notes, locType, active) VALUES ('Giant Barcade', '435 Silverball Ln', false, '', 1, true);


INSERT INTO locations_machines (location_id, machine_id, name, condition, notes, active) VALUES (1, 261, 'Attack From Mars Remake', 'OK', '', true);



INSERT INTO players (nick, name, email, phone, location, ifpanumber, pinside, notes, status, active, currentrank, currentwpprvalue, bestfinish, activeevents) VALUES ('', 'John', 'john@someemail.com', '4564534566', 'San Jose, CA', '', '', '', 0, true, 0, 0.00, 0, 0);

INSERT INTO players (nick, name, email, phone, location, ifpanumber, pinside, notes, status, active, currentrank, currentwpprvalue, bestfinish, activeevents) VALUES ('', 'Peter', 'peter@someemail.com', '7654345677', 'Boston, MA', '', '', '', 0, true, 0, 0.00, 0, 0);

INSERT INTO players (nick, name, email, phone, location, ifpanumber, pinside, notes, status, active, currentrank, currentwpprvalue, bestfinish, activeevents) VALUES ('', 'Amanda', 'amanda@someemail.com', '', 'Washington, DC', '', '', '', 0, true, 0, 0.00, 0, 0);

INSERT INTO players (nick, name, email, phone, location, ifpanumber, pinside, notes, status, active, currentrank, currentwpprvalue, bestfinish, activeevents) VALUES ('', 'Mike', 'mike@someemail.com', '1232345432', 'Seattle, WA', '', '', '', 0, true, 0, 0.00, 0, 0);

INSERT INTO players (nick, name, email, phone, location, ifpanumber, pinside, notes, status, active, currentrank, currentwpprvalue, bestfinish, activeevents) VALUES ('', 'Eve', 'eve@someemail.com', '9685748345', 'Chicago, IL', '', '', '', 0, true, 0, 0.00, 0, 0);

INSERT INTO players (nick, name, email, phone, location, ifpanumber, pinside, notes, status, active, currentrank, currentwpprvalue, bestfinish, activeevents) VALUES ('', 'Samantha', 'samantha@someemail.com', '', 'Baltimore, MD', '', '', '', 0, true, 0, 0.00, 0, 0);

INSERT INTO players (nick, name, email, phone, location, ifpanumber, pinside, notes, status, active, currentrank, currentwpprvalue, bestfinish, activeevents) VALUES ('', 'Jane', 'jane@someemail.com', '3456787654', 'Boise, ID', '', '', '', 0, true, 0, 0.00, 0, 0);

INSERT INTO players (nick, name, email, phone, location, ifpanumber, pinside, notes, status, active, currentrank, currentwpprvalue, bestfinish, activeevents) VALUES ('', 'Daniel', 'daniel@someemail.com', '9786856754', 'Orlando, FL', '', '', '', 0, true, 0, 0.00, 0, 0);

INSERT INTO players (nick, name, email, phone, location, ifpanumber, pinside, notes, status, active, currentrank, currentwpprvalue, bestfinish, activeevents) VALUES ('', 'Greg', 'greg@someemail.com', '4345654433', 'Nashville, TN', '', '', '', 0, true, 0, 0.00, 0, 0);

INSERT INTO players (nick, name, email, phone, location, ifpanumber, pinside, notes, status, active, currentrank, currentwpprvalue, bestfinish, activeevents) VALUES ('', 'Ann', 'ann@someemail.com', '', 'San Diego, CA', '', '', '', 0, true, 0, 0.00, 0, 0);



INSERT INTO tournaments (location_id, name, tournament_datetime, tournament_format, tournament_seeding, active) VALUES (1, 'Test1', '2020-10-12T00:00:00.000', 0, 0, true);

INSERT INTO tournaments (location_id, name, tournament_datetime, tournament_format, tournament_seeding, active) VALUES (1, 'Test2', '2020-04-09T00:00:00.000', 0, 0, true);

INSERT INTO tournaments (location_id, name, tournament_datetime, tournament_format, tournament_seeding, active) VALUES (1, 'Test3', '2020-12-10T00:00:00.000', 0, 0, true);

INSERT INTO tournaments (location_id, name, tournament_datetime, tournament_format, tournament_seeding, active) VALUES (1, 'Test4', '2020-11-23T00:00:00.000', 0, 0, true);

INSERT INTO tournaments (location_id, name, tournament_datetime, tournament_format, tournament_seeding, active) VALUES (1, 'Test5', '2021-08-18T00:00:00.000', 0, 0, true);

INSERT INTO tournaments (location_id, name, tournament_datetime, tournament_format, tournament_seeding, active) VALUES (1, 'Test6', '2021-02-22T00:00:00.000', 0, 0, true);



INSERT INTO tournament_players (tournament_id, player_id) VALUES (1, 1);

INSERT INTO tournament_players (tournament_id, player_id) VALUES (1, 2);

INSERT INTO tournament_players (tournament_id, player_id) VALUES (1, 3);
