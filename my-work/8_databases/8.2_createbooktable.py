# class 8, lab 2 -using sqlite 
# author: irene celebrin 
# step 1, create database 

# import sqlite
import sqlite3
con = sqlite3.connect("pfda.db")
cur = con.cursor()

# create table
cur.execute("CREATE TABLE book(title, author, ISBN)")
# print success message 
print('database was created')
con.close()


