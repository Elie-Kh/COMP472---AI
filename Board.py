from tkinter import *
import tkinter.messagebox
tk = Tk()
tk.title("Nora game")


def disable_button():
    button.configure(state=DISABLED)


for r in range(10):
    for c in range(12):
        button = Button(tk, text=' ', font='Times 20 bold', bg='gray', fg='white', height=2, width=6)
        button.grid(row=r, column=c)

tk.mainloop()
