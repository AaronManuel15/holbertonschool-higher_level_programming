-- lists all the cities of California that can be found in the database hbtn_0d_usa
SELECT cities.id, cities.name WHERE cities.name = 'California'
ORDER BY cities.id
