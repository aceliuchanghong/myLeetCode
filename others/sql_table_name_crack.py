import re


def tables_in_query2(sql_str):
    # remove the /* */ comments (先移除块注释)
    q = re.sub(r"/\*[^*]*\*+(?:[^*/][^*]*\*+)*/", "", sql_str)

    # remove whole line -- and # comments (再移除整行注释)
    lines = [line for line in q.splitlines() if not re.match("^\s*(--|#)", line)]

    # remove trailing -- and # comments (再移除行尾注释)
    q = " ".join([re.split("--|#", line)[0] for line in lines])

    # split on blanks, parens and semicolons (用「空白符、括号、分号」作为分隔符进行切分)
    tokens = re.split(r"[\s)(;`]+", q)

    # scan the tokens. if we see a FROM or JOIN, we set the get_next
    # flag, and grab the next one (unless it's SELECT).
    # 扫描经过上述分词的列表，当看到 FROM/JOIN 关键字时，获取下一个非「空/select」的作为表名

    result = set()
    get_next = False
    for tok in tokens:
        if get_next:
            if tok.lower() not in ["", "select"]:
                result.add(tok)
            get_next = False
        get_next = tok.lower() in ["from", "join"]

    return result


if __name__ == '__main__':
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
    print(tables_in_query2(sql))
