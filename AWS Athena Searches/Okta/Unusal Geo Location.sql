# Unusal Geo Location 
SELECT detail.client.geographicalcontext.country AS country, COUNT(*) AS count
FROM  "your_database"."your_table"
GROUP BY detail.client.geographicalcontext.country
HAVING COUNT(*) < 5;

