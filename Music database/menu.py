import readsongs, addsongs, updatesongs, updatesongsV2, deletesongs, report
 
# create a function to read the songsMenu.txt file
def menu_file():
    with open("python/Pt9_10DBOps/songsMenu.txt") as songsFile:
        # read data from the songsMenu.txt file and save it in the menuOptions variable
        menuOptions = songsFile.read()
    return menuOptions
# print(menu_file()) - it gives back what's in the file so we can read it in the terminal

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
        if option not in optionsList:
            # execute the code below
            print(f"{option} is not a valid choice! ") # option(assigned to the input function)variable: 0//7/8/9...
    return option
# print(songs_menu()) - hasta aqui para q cuando el user ponga una opcion que no esta en la lista le devuelva q no es valido y que vuelva a seleccionar una opcion

#create a boolean variaable that can be toggled true/false or on/off --- from here, there're more ways to do it (match/dictionary)
mainProgram = True

while mainProgram: #same writing while True
    # initialise the songs_menu() function with mainMenu variable
    mainMenu = songs_menu()
 
    # if option(assigned to the input function) = 1/2/3/4/5/6
    # if "1" == "1"
    if mainMenu == "1":
        # ca// the file then the function from that file
        readsongs.read_songs()
    elif mainMenu == "2":
        addsongs.insert_songs()
    elif mainMenu == "3":
        updatesongs.update_songs()
    elif mainMenu == "4":
        deletesongs.delete_songs()
    elif mainMenu == "5":
        report.songs_report()
    else:# re-assign the value of the mainProgram variable to False
        mainProgram = False
input("Pres the 'Enter' key to quit the songs app")

# if __name__ == "__main__":
