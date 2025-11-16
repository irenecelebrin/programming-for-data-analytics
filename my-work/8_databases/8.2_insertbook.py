# class 8, lab 2 -using sqlite 
# author: irene celebrin 
# step 2, add to database. Insert some data in the database and check if it's there 

import sqlite3
con = sqlite3.connect("pfda.db")
cur = con.cursor()

# check there is nothing in the database 
result = cur.execute("select * from book")
# result will be "None"
print(result.fetchone())

# insert a book 
sql = """
    INSERT INTO book VALUES 
        ('Pride & Pottery', 'Jane Auster', '11223'),
        ('Mark Gain', 'Weight Watchers', '33221')
"""
# BAD --> this can lead to SQL injections 
# add to database 
cur.execute(sql)
# always commit
con.commit()
# get elements 
result = cur.execute("select * from book")
print (result.fetchall())

