# an outer function
def hello(fullname):

    #define the inner function
    def userdata():
        print(f"Your name is: {fullname}")
    # call the inner function
        userdata()
#call the outer function - will automatically call the inner function
#hello('James Bond')

#an outer function
def hello():
    # define a variable outside of the inner function
    fullname = "Johnny Test" # input("Enter your name")

    #define the inner function
    def userdata():
        print(f"Your name is: {fullname}")

    #call the inner function
        userdata()

    #call the uter function
    hello()