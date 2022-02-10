from distutils import command
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
class gameButton:
    def __init__(self, button):
        self.button = button
        self.state = 'empty'

    def getButton(self):
        return self.button

    def onClick(self):
        global currentPlayer
        global playerLabel

        if(currentPlayer.get() == 'Player 1'):
            if(self.state == 'empty'):
                self.button.config(image=imageO)
                self.state = 'o'
                currentPlayer.set('Player 2')
        else:
            if(self.state == 'empty'):
                self.button.config(image=imageX)
                self.state = 'x'
                currentPlayer.set('Player 1')

        checkWinCondition()

    def getState(self):
        return self.state

    def setState(self, state):
        self.state = state


# Game Buttons
b1 = gameButton(ttk.Button(frame, image=imageEmpty))
b1.getButton().grid(column=0, row=1)
b1.getButton().config(command=b1.onClick)

b2 = gameButton(ttk.Button(frame, image=imageEmpty))
b2.getButton().grid(column=0, row=2)
b2.getButton().config(command=b2.onClick)

b3 = gameButton(ttk.Button(frame, image=imageEmpty))
b3.getButton().grid(column=0, row=3)
b3.getButton().config(command=b3.onClick)

b4 = gameButton(ttk.Button(frame, image=imageEmpty))
b4.getButton().grid(column=1, row=1)
b4.getButton().config(command=b4.onClick)

b5 = gameButton(ttk.Button(frame, image=imageEmpty))
b5.getButton().grid(column=1, row=2)
b5.getButton().config(command=b5.onClick)

b6 = gameButton(ttk.Button(frame, image=imageEmpty))
b6.getButton().grid(column=1, row=3)
b6.getButton().config(command=b6.onClick)

b7 = gameButton(ttk.Button(frame, image=imageEmpty))
b7.getButton().grid(column=2, row=1)
b7.getButton().config(command=b7.onClick)

b8 = gameButton(ttk.Button(frame, image=imageEmpty))
b8.getButton().grid(column=2, row=2)
b8.getButton().config(command=b8.onClick)

b9 = gameButton(ttk.Button(frame, image=imageEmpty))
b9.getButton().grid(column=2, row=3)
b9.getButton().config(command=b9.onClick)

buttons = (b1, b2, b3, b4, b5, b6, b7, b8, b9)


# Reset Game
def reset():
    currentPlayer.set('Player 1')
    for button in buttons:
        button.setState('empty')
        button.getButton().config(image=imageEmpty)


resetButton = ttk.Button(frame, text='Reset', command=reset).grid(
    column=1, row=4, pady=10)


# Checking Victory Conditions
def checkWinCondition():
    for i in range(0, len(buttons)):
        buttonState = buttons[i].getState()

        # Vertical Victory
        if(i in (1, 4, 7)):
            if(0 <= i-1 < len(buttons) and 0 <= i+1 < len(buttons) and buttonState != 'empty'):
                if(buttons[i-1].getState() == buttonState and buttons[i+1].getState() == buttonState):
                    print('V Victory', i)

        # Diagonal Victory 2
        if(i == 4):
            if(0 <= i-2 < len(buttons) and 0 <= i+2 < len(buttons) and buttonState != 'empty'):
                if(buttons[i-2].getState() == buttonState and buttons[i+2].getState() == buttonState):
                    print('D2 Victory', i)

        # Horizontal Victory
        if(i in (3, 4, 5)):
            if(0 <= i-3 < len(buttons) and 0 <= i+3 < len(buttons) and buttonState != 'empty'):
                if(buttons[i-3].getState() == buttonState and buttons[i+3].getState() == buttonState):
                    print('H Victory', i)

        # Diagonal Victory 1
        if(i == 4):
            if(0 <= i-4 < len(buttons) and 0 <= i+4 < len(buttons) and buttonState != 'empty'):
                if(buttons[i-4].getState() == buttonState and buttons[i+4].getState() == buttonState):
                    print('D1 Victory', i)


# Running Game Loop
root.mainloop()
