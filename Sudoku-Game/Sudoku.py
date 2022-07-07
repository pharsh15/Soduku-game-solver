from tkinter import *
from tkinter import messagebox
from solver import solver
from EmptySudoku import empty
from SaveSudoku import SaveWin
from AddRecord import Show

# Creating main window
root = Tk(className=" SUDOKU Game-and-Solver") 
root.geometry("324x650") # dimensions of the main window
root.resizable(False, False) # restricting main window not to be resizable

# Label for instructions. Will modify as you different buttons clicked
label = Label(root, text="Fill numbers for your game and click 'Play'")
label.grid(row=0, column=1, columnspan=10)

# Label shown when not solvable
errLabel = Label(root, text="", fg="red") 
errLabel.grid(row=15, column=1, columnspan=10, pady=5)

# Label shown when solved
solvedLabel = Label(root, text="", fg="green")
solvedLabel.grid(row=15, column=1, columnspan=10, pady=5)

# Stores each cell of the input grid as a (key, value) pair
cells = {}

# Just to store the values entered by user before starting a game, i.e. before clicking 'Play'.
def getValues2():
    board = []
    errLabel.configure(text="")
    solvedLabel.configure(text="")
    for row in range(2,11):
        rows = []
        for col in range(1,10):
            val = cells[(row, col)].get()
            if val == "":
                rows.append(0)
            else:
                rows.append(int(val))
        board.append(rows)
    return board

answer = [] # global list to store answer

# stores answer in 'answer' (declared above).
def StoreAnswer():
    set = getValues2()
    if set == empty:
        label.config(text="Fill some values first.", fg="red")
        messagebox.showerror("Empty", "Fill some values.")
    else:
        global answer 
        answer = solver(set)
        label.config(text="Play. When done, click 'check'. If stuck, press 'Solve'", fg="blue")
     
# To ensure that each entry is of single digit from 0 to 9
def ValidateNumber(P):
    out = ((P in "123456789") or P == "") and len(P)<2
    return out

# To create a reference to the function above
# To register 'ValidateNumber' function as a new TCL command
reg = root.register(ValidateNumber)

# Dividing 9*9 grid into 3*3
def draw3x3Grid(row, column, bgcolor):
    for i in range(3): # Rows
        for j in range(3): # Columns
            e = Entry(root, width=5, bg=bgcolor, justify="center", validate="key", validatecommand=(reg, "%P"))
            e.grid(row=row+i+1, column=column+j+1, sticky="nsew", padx=1, pady=1, ipady=5)
            cells[(row+i+1, column+j+1)] = e

# The basic Board
def draw9x9Grid():
    color = "lightblue"
    for rowNo in range(1,10,3):
        for colNo in range(0,9,3):
            draw3x3Grid(rowNo, colNo, color)
            if color == "lightblue": 
                color = "pink"
            else:
                color = "lightblue"

# To clear the values in the cells
def clearValues():
    errLabel.configure(text="")
    solvedLabel.configure(text="")
    for row in range(2,11):
        for col in range(1,10):
            cell = cells[(row, col)]
            cell.delete(0, "end")

# To extract the values entered & send them for verification or solution purpose
# to initiate the solving process.
def getValues():
    board = []
    errLabel.configure(text="")
    solvedLabel.configure(text="")
    for row in range(2,11):
        rows = []
        for col in range(1,10):
            val = cells[(row, col)].get()
            if val == "":
                rows.append(0)
            else:
                rows.append(int(val))
        board.append(rows)
    updateValues(board)

# Button to make the GUI solve the puzzle
btn = Button(root, command=getValues, text="Solve", width = 15)
btn.grid(row=22, column=1, columnspan=5, pady=5)

# Button to make the GUI clear the values in the cells
btn = Button(root, command=clearValues, text="Clear", width = 15)
btn.grid(row=22, column=5, columnspan=5, pady=5)

# Button to Start playing
btn = Button(root, text="Play", width=15, command=StoreAnswer)
btn.grid(row=20, column=1, columnspan=5, pady=5)

# To check if the solution user has found matches with the actual one.
def check():
    if getValues2() == empty:
        messagebox.showerror("Empty", "Enter some values first!!")
    elif getValues2() == answer:
        solvedLabel.config(text="Correct!!", fg='green')
        messagebox.showinfo("Correct", "You did it!!")
    else:
        errLabel.config(text="Wrong", fg="red")
        messagebox.showinfo("Wrong", "Try Again")

# Button to check if the user solved it correct
btn = Button(root, text="Check", width=15, command=check)
btn.grid(row=20, column=5, columnspan=5, pady=5)

# Fxn for save button
def Save():
    SaveWin(getValues2())

# Button to save your game
btn = Button(root, text="Save Record", width=31, command=Save)
btn.grid(row=24, column=1, columnspan=11, pady=5)

# fxn to show history
def History():
    Show()

# Button to see game history
btn = Button(root, text="History", width=15, command=History)
btn.grid(row=25, column=1, columnspan=11, pady=5)

# Instruction label on how to use clear button
l = Label(root, text="Click 'Clear' to set a new game.")
l.grid(row= 26, column=1, columnspan=11, pady=5)

# To update the empty cells with the valid value they should contain
def updateValues(s):
    sol = solver(s)
    if sol != "no":
        for rows in range(2,11):
            for col in range(1,10):
                cells[(rows, col)].delete(0,"end")
                cells[(rows, col)].insert(0, sol[rows-2][col-1])
        solvedLabel.configure(text="This is the Solution", fg="green")
        messagebox.showinfo("Done", "Solved")

    else:
        errLabel.configure(text="No Solution")
        messagebox.showerror("Error", "Not Solvable")

draw9x9Grid() # **Game Starts from here**
root.mainloop()