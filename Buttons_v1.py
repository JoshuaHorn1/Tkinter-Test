from tkinter import *


def say_hi():
        Label(root, bg="yellow", fg="red", text="Hi User!", font=("Times", 50, "bold")).pack()


root = Tk()
root.title("My first button")
root.minsize(200, 400)

button1 = Button(root, text="Say Hi!", command=say_hi)
button1.pack()

root.mainloop()