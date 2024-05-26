from tkinter import *
from tkinter import ttk

rot = Tk()
rot.title("Delivery Foods")
rot.config(bg= "darkgray")
rot.geometry('300x150')

frame = Frame(rot, width=300, height=500, bg='#fcc08b')
frame.pack()

food = LabelFrame(frame,text='Menu',bd=5)
food.grid(row=0, column=0, sticky=W, padx=20, pady=20)

Checkbutton(food,text='Omelette').pack(anchor=W)
Checkbutton(food,text='Salad').pack(anchor=W)
Checkbutton(food,text='Spaghetti').pack(anchor=W)
Checkbutton(food,text='Fried chicken').pack(anchor=W)

drinks = LabelFrame(frame,text='Drinks',bd=5)
drinks.grid(row=0, column=1, sticky=E, padx=20, pady=20)

Checkbutton(drinks,text='Cola').pack(anchor=W)
Checkbutton(drinks,text='Tea').pack(anchor=W)
Checkbutton(drinks,text='Juice').pack(anchor=W)
Checkbutton(drinks,text='Smoothie').pack(anchor=W)

rot.mainloop()