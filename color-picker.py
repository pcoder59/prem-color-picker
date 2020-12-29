from tkinter import *
from tkinter import colorchooser

root = Tk()
root.title("Prem's Color Picker")
root.geometry("400x400")
root.iconbitmap("icon.ico")

def copy(color):
    root.clipboard_clear()
    root.clipboard_append(color)
    root.update()

def chooseColor():
    chosenColor = colorchooser.askcolor()
    colorRgb = (int(chosenColor[0][0]), int(chosenColor[0][1]), int(chosenColor[0][2]))
    colorLabel = Label(root, bg=chosenColor[1]).place(x=25, y=75)
    colorTextrgb = Text(root, width=23, height=1)
    colorTextrgb.insert(INSERT, colorRgb)
    colorTextrgb.place(x=50, y=75)
    copyRGB = Button(root, text="Copy", command=lambda: copy(colorRgb)).place(x=250, y=70)
    colorTexthex = Text(root, width=23, height=1)
    colorTexthex.insert(INSERT, chosenColor[1])
    colorTexthex.place(x=50, y=125)
    copyHEX = Button(root, text="Copy", command=lambda: copy(chosenColor[1])).place(x=250, y=120)

Button(root, text="Custom Color", command=chooseColor).place(x=25, y=25)

root.mainloop()