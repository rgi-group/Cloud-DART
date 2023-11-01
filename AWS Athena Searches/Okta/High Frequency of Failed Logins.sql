# High Frequency of Failed Logins
SELECT detail.actor.id AS user_id, COUNT(*) AS failed_count
FROM ""your_database"."your_table""
WHERE detail.outcome.result = 'FAILURE'
GROUP BY detail.actor.id
HAVING COUNT(*) > 10;
