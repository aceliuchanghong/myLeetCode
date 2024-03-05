sql = """SELECT a.time_updated_server/1000,
content,
nick,
name
FROM table1 a
JOIN table2 b ON a.sender_id = b.user_id
JOIN table3 c ON a.channel_id = c.channel_id
JOIN table4 d ON c.store_id = d.store_id
WHERE sender_id NOT IN
(SELECT user_id
FROM table5
WHERE store_id IN ('agent_store:1', 'ask:1'))
AND to_timestamp(a.time_updated_server/1000)::date >= '2014-05-01'
GROUP BY 1,2,3,4
HAVING sum(1) > 500
ORDER BY 1 ASC
"""

# 定义 SQL 查询语句
sql_query = """
select qaq,qbq,
qcq,-- qcq
substr(qdq,2),--qdq
qeq
from 
qq;
"""
