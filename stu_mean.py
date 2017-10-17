import sqlite3   #enable control of an sqlite database
import csv       #facilitates CSV I/O


f="discobandit.db"

db = sqlite3.connect(f) #open if f exists, otherwise create
c = db.cursor()    #facilitate db ops

#==========================================================

def db_to_dict():
    db_dict = {}
    for record in  c.execute("SELECT * FROM peeps"):
        student_info = {}
        student_info["grade"] = record[1]
        student_info["grade"] = record[2]
        db_dict[record[0]] = student_info
    return db_dict
    
grade_print()
    
for record in  c.execute("SELECT * FROM peeps"):
   print record


#==========================================================
db.commit() #save changes
db.close()  #close database

