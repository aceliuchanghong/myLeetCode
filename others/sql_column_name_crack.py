from moz_sql_parser import parse
import json

from others import *
"""
之后自己参照写一个解析库吧
"""
json.dumps(parse(sql_query))
