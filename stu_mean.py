import sqlite3   #enable control of an sqlite database
import csv       #facilitates CSV I/O


f="discobandit.db"

db = sqlite3.connect(f) #open if f exists, otherwise create
c = db.cursor()    #facilitate db ops

#==========================================================

#index values for courses
code = 0
mark = 1

#index values for peeps
#edit: don't use these variables, they became very confusing after a bugfix
name = 0
age = 1

#index of id for both tables
id = 2

def courses_to_list(): #turns the table courses into [code,mark,id]
	list = []
	for data in c.execute("SELECT * FROM courses").fetchall():
		list.append(data)
	return list

def peeps_to_dic(): #turns the table peeps into a dic, with names as keys
	dic = {}
	for data in c.execute("SELECT * FROM peeps").fetchall():
		dic[data[name]] = (data[age],data[id],)
	return dic

def average_grades(courses_list): #returns a dic with [average of all marks, number of courses taken] with ids as keys
	dic = {}
	#allocates space
	for course in courses_list:
		dic[course[id]] = [0,0]
	#adds everything up
	for course in courses_list:
		dic[course[id]][0] += course[mark]
		dic[course[id]][1] += 1
	#divides to get average
	for _id in dic:
		dic[_id][0] /= dic[_id][1]
	return dic
def name_id_average_dic(_peeps,_averages): #returns a dic with [id,average] with names as keys
	dic = {}
	for student in _peeps:
		dic[student] = [_peeps[student][1],_averages[_peeps[student][1]][0]]
	return dic
courses = courses_to_list()
peeps = peeps_to_dic()
averages = average_grades(courses)
print name_id_average_dic(peeps,averages)
#==========================================================
db.commit() #save changes
db.close()  #close database

