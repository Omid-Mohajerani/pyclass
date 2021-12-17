#!/usr/bin/python3
import mysql.connector
import fileinput
import re

mydb = mysql.connector.connect(
  host="localhost",
  user="newuser",
  password="password",
  database="ipban"
)

for line in fileinput.input():
    ip = re.findall( r'[0-9]+(?:\.[0-9]+){3}', line )
    if ip:
        for i in ip:
            mycursor = mydb.cursor()
            ip = str(i)
            print(ip)

            sql = f"INSERT INTO badips (ip) VALUES ('{ip}')"
            print(sql)
            #val = ("1234")
            mycursor.execute(sql)
            mydb.commit()
