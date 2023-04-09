from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox

def clickImage(event):
    messagebox.showinfo("마우스", "토끼에서 마우스가 클릭됨")

window = Tk()
window.geometry("400x400")
photo = ImageTk.PhotoImage(Image.open("./rabbit.png"))
label1 = Label(window, image = photo)

label1.bind("<Button>", clickImage)

label1.pack(expand=1, anchor = CENTER)
window.mainloop()