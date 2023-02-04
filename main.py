from shoeMenu import *

def sayHi():
    print("hi")

def sayHi2():
    print("hi2")

def main():
    print("hi")
    mainMenu = ShoeMenu()
    mainMenu.addOptions([(1, "Option 1", sayHi), (2, "Option 2", sayHi2)])
    print(mainMenu.generateOptions())

def __main__():
    main()