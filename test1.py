from tkinter import *
root = Tk()

root.geometry("600x200")
root.maxsize(800, 400)

root.title("My first window")
greeting = Label(text='Hello Tkinter')
greeting.pack()

root.mainloop()