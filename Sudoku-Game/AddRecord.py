import mysql.connector
from DT import DTnow
from tkinter import *
from tkinter import messagebox

def Saving(res):
    # Create Connection with database
    Sudoku = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "********",
        database = "sudoku"
    )

    mycursor = Sudoku.cursor()
    mycursor.execute("SHOW DATABASES")

    # x[0] gives DB name
    # x gives the tuple with DB name as first element
    # **DB name completely lowercase <-- done automatically
    y=0
    for x in mycursor:
        if x[0] == 'sudoku':
            y=1
        else:
            continue

    # if DB 'sudoku' doesn't exist then create one.
    if y==0:
        mycursor.execute("CREATE DATABASE sudoku")



    mycursor.execute("SHOW TABLES")


    y=0 
    for x in mycursor:
        if x[0] == 'games':
            y=1
        else:
            continue

    if y==0:
        mycursor.execute("CREATE TABLE Games\
                        (id INT AUTO_INCREMENT PRIMARY KEY,\
                        Pname VARCHAR (255), DT VARCHAR(255),\
                        Result VARCHAR(255))")
                        
    sql = "INSERT INTO Games(DT, Result) VALUES(%s, %s)"
    val = [(DTnow(), res)]

    mycursor.executemany(sql, val)
    Sudoku.commit()
    messagebox.showinfo("Done", "Results Saved")

def Show():
    Sudoku = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "********",
        database = "sudoku"
    )

    mycursor = Sudoku.cursor()
    mycursor.execute("SHOW DATABASES")
    y=0
    for x in mycursor:
        if x[0] == 'sudoku':
            y=1
        else:
            continue
    if y==0:
        mycursor.execute("CREATE DATABASE sudoku")



    mycursor.execute("SHOW TABLES")


    y=0 
    for x in mycursor:
        if x[0] == 'games':
            y=1
        else:
            continue

    if y==0:
        mycursor.execute("CREATE TABLE Games\
                        (id INT AUTO_INCREMENT PRIMARY KEY,\
                        Pname VARCHAR (255), DT VARCHAR(255),\
                        Result VARCHAR(255))")
    
    mycursor.execute("SELECT id, DT, Result FROM Games ORDER BY id")
    myresult=mycursor.fetchall()


    his = Tk(className="History")
    his.geometry("243x200")
    his.resizable(False, False)

    l = Listbox(his, width=40, justify="center", font=("Arial", 18))
    for x in myresult:
        for i in range(len(x)):
            l.insert(i, x[i])
        l.insert(i+1, "\n")
    l.pack()

    his.mainloop()