#Detect Suspicious IP Addresses
SELECT detail.client.ipaddress AS suspicious_ip, COUNT(*) AS count
FROM "your_database"."postman_s3_okta_audit_logs"
WHERE detail.outcome.result = 'FAILURE'
GROUP BY detail.client.ipaddress
HAVING COUNT(*) > 5;
