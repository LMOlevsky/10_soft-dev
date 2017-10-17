import sqlite3   #enable control of an sqlite database
import csv       #facilitates CSV I/O


f="discobandit.db"

db = sqlite3.connect(f) #open if f exists, otherwise create
c = db.cursor()    #facilitate db ops

#==========================================================

def grade_print():
    for record in  c.execute("SELECT * FROM peeps"):
        print record[1]
    
grade_print()
    
for record in  c.execute("SELECT * FROM peeps"):
   print record


#==========================================================
db.commit() #save changes
db.close()  #close database

