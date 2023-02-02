import sqlite3

def connectToDB(name):
    return sqlite3.connect(name)

def createTable():
    print("hi")