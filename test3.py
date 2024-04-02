from tkinter import *

root = Tk()
root.title("Using a label to place image")

amogus_image = PhotoImage(file="among-us-sus.gif")

image_label = Label(root, image=amogus_image)
image_label.pack()

text_label = Label(root, text="Amogus FR", bg="black", fg="white", font=("Courier", 50, "bold"))
text_label.pack()

root.mainloop()
