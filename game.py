from tkinter import *

turn = 'X'


def nextTurn():
    global turn
    turn = 'X' if turn == 'O' else turn == 'O'


def click(label, x, y):
    print(x, y)
    label['text'] = turn
    nextTurn()


def addLabel(frame, text, x, y):
    label = Label(frame, text=text, font=("Helvetica", 32),
                  borderwidth=2, relief="ridge", width=2, background="green")
    label.grid(row=y, column=x, padx=10, pady=10)
    label.bind("<Button-1>", lambda event: click(label, x, y))


root = Tk()
root.wm_title("TicTacToe")
frame = Frame(root, width=300, height=500)

for x in range(0, 3):
    for y in range(0, 3):
        addLabel(frame, "", x, y)

frame.pack()
frame.mainloop()
