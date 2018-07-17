#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import pymysql


conn = pymysql.connect(host='localhost', port=3306, user='root', password='felix', database='front', charset='utf8')
cursor = conn.cursor()
cursor.execute("USE front")

cursor.execute('select * from kub_user where userid=%s', ('01351',))

print(cursor.fetchall())

cursor.close()
conn.close()
