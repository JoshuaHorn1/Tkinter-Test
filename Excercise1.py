from tkinter import *
root = Tk()

root.title("Excercise 1")

computer = Label(root, bg="green", fg="white", text="Computer", font=("Times", 50, "italic"))
computer.pack(fill=BOTH)
science = Label(root, bg="blue", fg="yellow", text="Science is", font=("Times", 50,))
science.pack(fill=BOTH)
awesome = Label(root, bg="orange", fg="red", text="awesome!", font=("Times", 50, "bold"))
awesome.pack(fill=BOTH)

root.mainloop()