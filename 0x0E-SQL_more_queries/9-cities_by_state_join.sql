-- script that lists all cities contained in the database hbtn_0d_usa
SELECT *
FROM cities, states
WHERE cities.state_id = states.id
ORDER BY cities.id ASC;
