#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# python连接mysql数据库

import mysql.connector as mc

conn = mc.connect(host='localhost', port=3306, user='root', password='felix', database='front', charset='utf8')
cursor = conn.cursor()

cursor.execute('select * from kub_user where userid=%s', ('01351',))
values = cursor.fetchall()
print(values)

cursor.close()
conn.close()
