'''
Created on 14 Jan, 2021

@author: Cuteepoo
'''
import mysql.connector

con=mysql.connector.connect(host="localhost",user="root",password="newroot",database="pythondata")

mycursor=con.cursor()

mycursor.execute("select * from student")

result=mycursor.fetchall()

for i in result:
    print(i)