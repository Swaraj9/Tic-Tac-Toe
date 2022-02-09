from tkinter import *
from tkinter import ttk

# Root Window
root = Tk()
root.title('Tic Tac Toe')

frame = ttk.Frame(root, padding=10)
frame.grid()

# Button image paths and resizing
imageO = PhotoImage(file='./O.png').subsample(3, 3)
imageX = PhotoImage(file='./X.png').subsample(3, 3)
imageEmpty = PhotoImage(file='./Empty.png').subsample(3, 3)

currentPlayer = StringVar()
currentPlayer.set('Player 1')

# Player Label
playerLabel = ttk.Label(frame, textvariable=currentPlayer, font=('Arial', 25),
                        padding=(0, 0, 0, 10)).grid(column=1, row=0)


# Game Button Behaviour
def onClickGameButton():
    global currentPlayer
    global playerLabel

    if(currentPlayer.get() == 'Player 1'):
        currentPlayer.set('Player 2')
    else:
        currentPlayer.set('Player 1')


# Game Buttons
ttk.Button(frame, image=imageEmpty,
           command=onClickGameButton).grid(column=0, row=1)
ttk.Button(frame, image=imageEmpty,
           command=onClickGameButton).grid(column=0, row=2)
ttk.Button(frame, image=imageEmpty,
           command=onClickGameButton).grid(column=0, row=3)
ttk.Button(frame, image=imageEmpty,
           command=onClickGameButton).grid(column=1, row=1)
ttk.Button(frame, image=imageEmpty,
           command=onClickGameButton).grid(column=1, row=2)
ttk.Button(frame, image=imageEmpty,
           command=onClickGameButton).grid(column=1, row=3)
ttk.Button(frame, image=imageEmpty,
           command=onClickGameButton).grid(column=2, row=1)
ttk.Button(frame, image=imageEmpty,
           command=onClickGameButton).grid(column=2, row=2)
ttk.Button(frame, image=imageEmpty,
           command=onClickGameButton).grid(column=2, row=3)


# Running Game Loop
root.mainloop()
