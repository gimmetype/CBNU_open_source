from tkinter import *
from PIL import ImageTk, Image


window = Tk()

photo = ImageTk.PhotoImage(Image.open("./dog.png"))

label1 = Label(window, image = photo)

label1.pack()

window.mainloop()
