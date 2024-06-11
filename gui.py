from tkinter import *
from tkinter.ttk import *

from logic import Solve

values = ['circle','square','triangle']

def buttoncommand():
    if leftcirclevar == 1 and leftsquarevar == 1 and lefttrianglevar == 1:
        pass
    elif leftcirclevar == 1 and leftsquarevar == 1:
        leftWall = ['circle','square']
    elif leftsquarevar == 1 and lefttrianglevar == 1:
        leftWall = ['square','triangle']
    elif leftcirclevar == 1 and lefttrianglevar == 1:
        leftWall = ['circle','triangle']
    elif leftcirclevar == 1: 
        leftWall = ['circle','circle']
    elif leftsquarevar == 1: 
        leftWall = ['square','square']
    else:
        leftWall = ['triangle','triangle']
   
    if midcirclevar == 1 and midsquarevar == 1 and midtrianglevar == 1:
        pass
    elif midcirclevar == 1 and midsquarevar == 1:
        midWall = ['circle','square']
    elif midsquarevar == 1 and midtrianglevar == 1:
        midWall = ['square','triangle']
    elif midcirclevar == 1 and midtrianglevar == 1:
        midWall = ['circle','triangle']
    elif midcirclevar == 1: 
        midWall = ['circle','circle']
    elif midsquarevar == 1: 
        midWall = ['square','square']
    else:
        midWall = ['triangle','triangle']

    if rightcirclevar == 1 and rightsquarevar == 1 and righttrianglevar == 1:
        pass
    elif rightcirclevar == 1 and rightsquarevar == 1:
        rightWall = ['circle','square']
    elif rightsquarevar == 1 and righttrianglevar == 1:
        rightWall = ['square','triangle']
    elif rightcirclevar == 1 and righttrianglevar == 1:
        rightWall = ['circle','triangle']
    elif rightcirclevar == 1: 
        rightWall = ['circle','circle']
    elif rightsquarevar == 1: 
        rightWall = ['square','square']
    else:
        rightWall = ['triangle','triangle']

    callout = [calloutOne.get(), calloutTwo.get(), calloutThree.get()]

    Solve(leftWall,midWall,rightWall,callout)

root = Tk()

# set images
circle = PhotoImage(file = 'assets/Circle.png')
circleimage = circle.subsample(6,6)

square = PhotoImage(file = 'assets/Square.png')
squareimage = square.subsample(6,6)

triangle = PhotoImage(file = 'assets/Triangle.png')
triangleimage = triangle.subsample(6,6)


# window setup
root.geometry("800x500")
root.title("Salvation's Edge Verity Solver")

# columns
root.grid_columnconfigure(0,weight=1)
root.grid_columnconfigure(1,weight=1)
root.grid_columnconfigure(2,weight=1)

# rows
root.grid_rowconfigure(0,weight=2)
root.grid_rowconfigure(1,weight=1)
root.grid_rowconfigure(2,weight=1)
root.grid_rowconfigure(3,weight=3)
root.grid_rowconfigure(4,weight=3)
root.grid_rowconfigure(5,weight=3)
root.grid_rowconfigure(6,weight=1)


# Statue Titles
leftframetitle = Label(root, text="Left Guardian", font="Arial, 14")
leftframetitle.grid(row=0,column=0)

midframetitle = Label(root, text="Mid Guardian", font="Arial, 14")
midframetitle.grid(row=0,column=1)

rightframetitle = Label(root, text="Right Guardian", font="Arial, 14")
rightframetitle.grid(row=0,column=2)


# callout prompts
calloutTitleOne = Label(root, text="Statue Symbol")
calloutTitleTwo = Label(root, text="Statue Symbol")
calloutTitleThree = Label(root, text="Statue Symbol")
calloutTitleOne.grid(row=1,column=0)
calloutTitleTwo.grid(row=1,column=1)
calloutTitleThree.grid(row=1,column=2)

calloutOne = Combobox(root,values=values, state="readonly")
calloutOne.grid(row=2,column=0)

calloutTwo = Combobox(root,values=values, state="readonly")
calloutTwo.grid(row=2,column=1)

calloutThree = Combobox(root,values=values, state="readonly")
calloutThree.grid(row=2,column=2)

# checkbutton vars
leftcirclevar = IntVar()
leftsquarevar = IntVar()
lefttrianglevar = IntVar()

midcirclevar = IntVar()
midsquarevar = IntVar()
midtrianglevar = IntVar()

rightcirclevar = IntVar()
rightsquarevar = IntVar()
righttrianglevar = IntVar()

# left buttons
leftcircle = Checkbutton(root, image = circleimage, variable=leftcirclevar)
leftcircle.grid(row=3,column=0)
leftsquare = Checkbutton(root, image = squareimage, variable=leftsquarevar)
leftsquare.grid(row=4,column=0)
lefttriangle = Checkbutton(root, image = triangleimage, variable=lefttrianglevar)
lefttriangle.grid(row=5,column=0)

# mid buttons
midcircle = Checkbutton(root, image = circleimage, variable=midcirclevar)
midcircle.grid(row=3,column=1)
midsquare = Checkbutton(root, image = squareimage, variable=midsquarevar)
midsquare.grid(row=4,column=1)
midtriangle = Checkbutton(root, image = triangleimage, variable=midtrianglevar)
midtriangle.grid(row=5,column=1)

# right buttons
rightcircle = Checkbutton(root, image = circleimage, variable=rightcirclevar)
rightcircle.grid(row=3,column=2)
rightsquare = Checkbutton(root, image = squareimage, variable=rightsquarevar)
rightsquare.grid(row=4,column=2)
righttriangle = Checkbutton(root, image = triangleimage, variable=righttrianglevar)
righttriangle.grid(row=5,column=2)

# solve
solvebutton = Button(root,text="Solve!", command = buttoncommand)
solvebutton.grid(row=6, column=0, columnspan=(3))



root.mainloop()