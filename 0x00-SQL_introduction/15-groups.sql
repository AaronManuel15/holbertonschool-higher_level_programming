-- lists the number of records with the same score in the table second_table
SELECT score 'score', COUNT(score) 'number' FROM second_table
GROUP BY score
ORDER BY COUNT(score) DESC;
