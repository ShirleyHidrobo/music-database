from connect import * 

def songs_report():
    # dbCursor.execute("SELECT * FROM songs ORDER BY Artist")
    # dbCursor.execute("SELECT artist, Title FROM songs ORDER BY Artist")
    # dbCursor.execute("SELECT * FROM songs ORDER BY Artist Desc")
    # dbCursor.execute("SELECT artist, Title FROM songs ORDER BY Artist DESC")
    # dbCursor.execute("SELECT * FROM songs where title = 'Imagine'")
    # dbCursor.execute("SELECT * FROM songs where title = 'Imagine' AND Artist = 'Prince'")
    # dbCursor.execute("SELECT * FROM songs WHERE Genre = 'Pop' ")
    # dbCursor.execute("SELECT * FROM songs WHERE Genre LIKE 'Pop' ")
    # dbCursor.execute("SELECT * FROM songs WHERE Artist LIKE 'a%' ")
    # dbCursor.execute("SELECT * FROM songs WHERE Artist LIKE '%e' ")
    # dbCursor.execute("SELECT * FROM songs WHERE Artist LIKE '%e%' ")
    dbCursor.execute("SELECT * FROM songs WHERE TITLE = 'Imagine' OR Artist = 'Prince' ")

    records = dbCursor.fetchall()

    for aRecord in records:
        print(aRecord)

if __name__ == "__main__":
    songs_report()