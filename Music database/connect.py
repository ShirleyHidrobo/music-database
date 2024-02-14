import sqlite3 as sql # import sqlite module and assing it an alias 'sql' 
# module collection of classes, functions and methods, module is on top of class , a lab can have multiple modules

# to connect to the sqlite db
dbCon = sql.connect("python/Pt9_10DBOps/dfe4w4songs.db") # 1st conector
# once a connection/DB is created 
# create a cursor object, call its execute method to run sql queries/statments -- 2nd conector
dbCursor = dbCon.cursor()  # if we have not the connection (line 4) we should use dbCursor = sql.connect().cursor()