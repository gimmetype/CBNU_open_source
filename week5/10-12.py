from tkinter import *
from PIL import ImageTk, Image
from time import *


##전역 변수 선언 부분##
fnameList = ["jeju1.gif", "jeju2.gif", "jeju3.gif", "jeju4.gif", "jeju5.gif", "jeju6.gif", "jeju7.gif", "jeju8.gif", "jeju9.gif"]

photoList = [None] * 9
num = 0


##함수 선언 부분##
def clickNext():
    global num
    num += 1
    if num > 8:
        num = 0
    photo = PhotoImage(file = "gif/" + fnameList[num])
    plabel.configure(image = photo)
    plabel.image = photo

def clickPrev():
    global num
    num -= 1
    if num < 0:
        num = 8
    photo = PhotoImage(file = "gif/" + fnameList[num])
    plabel.configure(image = photo)
    plabel.image = photo


##메인 코드 부분##
window = Tk()
window.geometry("700x800")
window.title("사진 앨범 보기")

btnPrev = Button(window, text= "<<이전", command = clickPrev)
btnNext = Button(window, text= "다음>>", command = clickNext)

photo = PhotoImage(file = "gif/" + fnameList[0])
plabel = Label(window, image = photo)

btnPrev.place(x = 250, y = 10)
btnNext.place(x = 400, y = 10)
plabel.place(x = 15, y = 50)

window.mainloop()