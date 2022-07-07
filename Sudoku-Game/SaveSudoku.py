from tkinter import *
from tkinter import messagebox
from AddRecord import Saving

# result to be displayed.
result = ""

# Save Window Pop-up
def SaveWin(game):
    # Creating Save Window
    # save = Tk(className=" Save Game")
    # save.geometry("243x150")
    # save.resizable(False, False)
    
    # Instruction Label
    # l = Label(save, text="Who was playing ?", justify="center")
    # l.pack()
    
    # Label 
    # l = Label(save, text="Player Name", pady=10)
    # l.pack()
    
    # Entry for Name
    # global un
    # un = StringVar()
    # e = Entry(save, textvariable=un)
    # e.pack()
    global result
    result = False
    for i in range(9):
        for j in range(9):
            if game[i][j]==0:
                result=True
                break
    if result==True:
        result="Uncompleted"
    else:
        result="Completed" 
    Saving(result)
    # Save Button
    # b = Button(save, text="Save", justify="center", pady=15, padx=15, command=SAVE)
    # b.pack()

    # save.mainloop()   