-- full creation
CREATE TABLE if not exists second_table (
id INT,
name VARCHAR(256),
score INT,
);
INSERT INTO (id,name,score) VALUES(1,'John',10);
INSERT INTO (id,name,score) VALUES(2,'Alex',3);
INSERT INTO (id,name,score) VALUES(3,'Bob',14);
INSERT INTO (id,name,score) VALUES(4,'George',8);
