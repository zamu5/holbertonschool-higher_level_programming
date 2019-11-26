-- group by score
-- query to list group of the same score and count it
SELECT score, COUNT(*) AS number FROM second_table GROUP BY score ORDER BY score DESC;
