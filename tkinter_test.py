from tkinter import *
window = Tk()

def clicked():
    btn.configure(text="I was Clicked!", bg="red", fg="black", command=reset)
    
def reset():
    btn.configure(text="Click Me", bg="green", fg="white", command=clicked)

window.title("Button Test")
window.geometry('480x800')
btn = Button(window, text="Click Me", bg="green", fg="white", command=clicked)
btn.grid(column=0, row=0)

window.mainloop()
