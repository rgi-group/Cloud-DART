# Unusal Geo Location 
SELECT detail.client.geographicalcontext.country AS country, COUNT(*) AS count
FROM "your_database"."postman_s3_okta_audit_logs"
GROUP BY detail.client.geographicalcontext.country
HAVING COUNT(*) < 5;

