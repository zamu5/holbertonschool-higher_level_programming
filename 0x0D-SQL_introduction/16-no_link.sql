-- name and score
-- query to list name and score if name is not NULL
SELECT score, name FROM second_table WHERE NAME IS NOT NULL ORDER BY score DESC;
