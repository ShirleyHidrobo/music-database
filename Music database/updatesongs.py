from connect import *
 
#create a subroutine to update records in the songs table
def update_songs():
    #Fields: Title, Artist, Genre
    # (1, 'Dance', 'MJ', 'Pop')
    # use the primary key to update a record
    idField= input("Enter the SongID of the record to be updated: ")
 
    # ask for the field to be updated
    #Fields: Title, Artist, Genre
    fieldName = input("Enter the Title or Artist or Genre as field name: ")
 
    # ask for the field value to be updated
    fieldValue = input(f"Enter the value for {fieldName} field")
 
    # add single quotes to match the value as it is, in the table in the db
    fieldValue = "'"+fieldValue+"'"
 
    # update the record in the table using the idField value
    "UPDATE songs SET Title/Artist/Genre = Title value /Artist  value /Genre value"
    dbCursor.execute(f"UPDATE songs SET {fieldName} = {fieldValue} WHERE SongID ={idField}")
    dbCon.commit() # Makes the change/update permanent in the table
 
    print(f"Record {idField} updated in the songs table")
 
if __name__ == "__main__":
    update_songs()

