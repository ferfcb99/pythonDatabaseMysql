# tkinter
from tkinter import *

window = Tk()

# crear boton 

btn = Button(window, text="Submit", fg='black', bg='white')

btn.place(x = 165, y=300)

window.title('Primer interfaz')

window.geometry("350x400+50+200")


window.mainloop()