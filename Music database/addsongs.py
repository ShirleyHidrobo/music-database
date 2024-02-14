from connect import *

# create a subroutine to add records in the songs table 
def insert_songs():
    # songID is a primary autoincrement field, no data input is required
    # create three input statements respectively fot the Title, Artist and Genre fields
    songTitle = input("Enter song Title:")
    songArtist = input("Enter song Artist:")
    songGenre= input("Enter song Genre:")

    # add data from saved in the variables (songTitle,songArtist,songGenre)
    dbCursor.execute("INSERT INTO songs(Title, Artist, Genre)VALUES(?,?,?)",(songTitle,songArtist,songGenre)) #we use (?,?,?) to avoid sql injection so we add songTitle, songArtist, songGenre
    # save the changes permanently in the songs in the db
    dbCon.commit()

    print(f"{songTitle} inserted in the songs table. ")

if __name__ == "__main__":
    insert_songs()