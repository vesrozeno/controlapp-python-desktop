from tkinter import Tk, Label, Button, Entry

window = Tk()

window.title("Control App")
window.geometry("350x200")

lbl = Label(window, text="Olá!", font=("Arial Bold", 25))
lbl.grid(column=0, row=0)

txt = Entry(window, width=10)
txt.grid(column=0, row=2)


def clicked():
    res = "Olá, " + txt.get() + "!"
    lbl.configure(text=res)


btn = Button(window, text="Botão", bg="black", fg="white", command=clicked)
btn.grid(column=0, row=3)

window.mainloop()
