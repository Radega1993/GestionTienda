from tkinter import *

from tkinter import messagebox

from tkinter import Menu

from tkinter import ttk

from tkinter.ttk import *

from tkinter.ttk import Progressbar


window = Tk()

window.title("GestPro")

menu = Menu(window)

new_item = Menu(menu)

new_item.add_command(label='New')

new_item.add_separator()

new_item.add_command(label='Edit')

menu.add_cascade(label='File', menu=new_item)

window.config(menu=menu)

window.geometry('350x200')

chk_state = BooleanVar()

chk_state.set(True) #set check state

chk = Checkbutton(window, text='Choose', var=chk_state)

chk.grid(column=0, row=0)

combo = Combobox(window)

combo['values']= (1, 2, 3, 4, 5, "Text")

combo.current(1) #set the selected item

combo.grid(column=1, row=0)


lbl = Label(window, text="Hola", font=("Arial Bold", 50))

lbl.grid(column=1, row=0)

txt = Entry(window,width=10, state='disabled')

txt.focus()

txt.grid(column=2, row=0)

def clicked():
    '''
    res = "Welcome to " + txt.get()

    lbl.configure(text= res)
'''
    messagebox.showinfo('Message title','Message content')

var =IntVar()

var.set(36)

spin = Spinbox(window, from_=0, to=100, width=5, textvariable=var)

spin.grid(column=5,row=0)

btn = Button(window,text='Click here', command=clicked)

btn.grid(column=3,row=0)

bar = Progressbar(window, length=200, style='black.Horizontal.TProgressbar')

bar['value'] = 70

bar.grid(column=0, row=3)

window.mainloop()
