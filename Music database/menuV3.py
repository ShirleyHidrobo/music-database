import readsongs, addsongs, updatesongs, updatesongsV2, deletesongs, report

# create a function to read the songsMenu.txt file 
def menu_file():
    with open("python/Pt9_10DBOps/menu.py") as songsFile:
        # read data from the songsMenu.txt file and save it in the menuOptions variable
        menuOptions = songsFile.read()
    return menuOptions

# create the menu function 
def songs_menu():
    option = 0 # initialise the option variable with an integer value
    optionsList = ["1","2","3","4","5","6"] # initiliased a list data structure with optionsLis variable

    # initialised/assigned the variable 'menuChoices' to the menu_file()function 
    menuChoices = menu_file() 

    # create a while loop to repeat the code within the body of the while loop 
    while option not in optionsList:
        # call/invoke the menu_file()function assigned to the 'menuChoices' variable to display the menu options
        print(menuChoices)

        # re-assign the option variable to an input function to ask to enter user choice 
        option = input("Enter an option from the songs main menu: ")

        #check if the user input from the option(assigned to the input function)variable
        # matches any of the menu options(menuChoices)
        
        match option:
            case option if option not in optionsList:
                # execute the code below
                print(f"{option} is not a valid choice! ") # option(assigned to the input function)variable: 0//7/8/9...
    return option
# print(songs_menu())


def songs():
    # create a boolean variable that can be toggled true/false or on/off
    mainProgram = True

    while mainProgram: #same writing while True

        # initialise the songs_menu() function with mainMenu variable 
        mainMenu = songs_menu()
        match mainMenu:
             # match option(assigned to the input function) = 1/2/3/4/5/6
             # match "1" == "1"
            case "1":
                # call the file then the function from that file
                readsongs.read_songs()

            case "2":
                # call the file then the function from that file
                addsongs.insert_songs()

            case "3":
                updatesongs.update_songs()
            
            case "4":
                deletesongs.delete_songs()
            
            case "5":
                report.songs_report()
            
            case _:
                #re-assign the value of the mainProgram variable to False
                mainProgram = False
                         
    input("Pres the 'Enter' key to quit the songs app")
if __name__ == "__main__":
    songs()


