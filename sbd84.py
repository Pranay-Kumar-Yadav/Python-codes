#pdbc create connection to mysql

import mysql.connector

try:
    conn = mysql.connector.connect(
        user='root',
        password='shhahah12',
        host='localhost',
        port=3309

    )
except Exception as obj:
    print("cannot connect")
else:
    print("connected")            