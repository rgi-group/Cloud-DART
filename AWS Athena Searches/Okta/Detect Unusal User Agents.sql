# Detect Unusal User Agents
SELECT detail.client.useragent.rawuseragent AS user_agent, COUNT(*) AS count
FROM "your_database"."postman_s3_okta_audit_logs"
GROUP BY detail.client.useragent.rawuseragent
HAVING COUNT(*) < 3;
