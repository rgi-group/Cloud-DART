# Unusual Times of Activity
SELECT date_parse(time, '%Y-%m-%dT%H:%i:%s.%fZ') AS parsed_time, COUNT(*) AS count
FROM  "your_database"."your_table"
WHERE date_format(date_parse(time, '%Y-%m-%dT%H:%i:%s.%fZ'), '%H') NOT BETWEEN '08' AND '18'
GROUP BY date_parse(time, '%Y-%m-%dT%H:%i:%s.%fZ');
