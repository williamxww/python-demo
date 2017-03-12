#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import sys
from imp import reload
reload(sys)
sys.setdefaultencoding('utf-8')

import pymysql
from pprint import pprint


conn = pymysql.connect(host='127.0.0.1', port=3306, user='xww', passwd='123456', db='shiro')
cur = conn.cursor()

cur.execute("call hello('roger')")
for r in cur.fetchall():
    for k in r:
        print(k)

cur.execute("call alltype();")
for r in cur.fetchall():
    for k in r:
        print(k, type(k))

try:
    cur.execute("call myerror;")
except Exception as e:
    print(e)
    print(e.args[0], e.args[1])

cur.close()
conn.close()
