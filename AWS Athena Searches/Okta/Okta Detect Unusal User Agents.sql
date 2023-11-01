# Detect Unusal User Agents
SELECT detail.client.useragent.rawuseragent AS user_agent, COUNT(*) AS count
FROM "your_database"."your_table"
GROUP BY detail.client.useragent.rawuseragent
HAVING COUNT(*) < 3;
