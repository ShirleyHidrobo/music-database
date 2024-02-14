from connect import *
 
#create a subroutine to read records from the songs table
def read_songs():
    # select all songs from the songs table
    dbCursor.execute("SELECT * FROM songs")
 
    # fetch all selected records using the fetchall method
    allRecords = dbCursor.fetchall()
 
    # loop though all the fetch records from the songs table
    for aRecord in allRecords:
        # display each record
        print(aRecord)
 
if __name__ == "__main__":
    read_songs()