from tkinter import *


window = Tk()
window.title("Chat bot")

inputfield = Entry(window, width=10)
inputfield.pack(side=LEFT)
inputfield.focus()


def send():
    message = inputfield.get()
    textbox.insert(INSERT, message)
    textbox.insert(INSERT, "\n")
    if message == "Hello":
        textbox.insert(INSERT, "Greetings, human.\n", 'robot')
    inputfield.delete(0, END)


btn = Button(window, text="Send", command=send)
btn.pack(side=LEFT)

textbox = Text(window, width=20, height=30)
textbox.pack(side=TOP)
textbox.tag_config('robot', background="blue", foreground="white")

window.mainloop()