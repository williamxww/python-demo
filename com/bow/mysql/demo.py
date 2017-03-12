#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pymysql
import os


conn = pymysql.connect(host='127.0.0.1', port=3306, user='xww', passwd='123456', db='shiro')
cur = conn.cursor()
cur.execute("SELECT * FROM sys_user")
for r in cur.fetchall():
    print(r)
# cur.close()
conn.close()
os.system('pause')
