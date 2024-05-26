import tkinter as tk
from tkinter import ttk
root = tk.Tk()
root.title("Area Calcuator")
root.config(bg= "darkgray")

#recipe
def recipe():
  lenght = float(L_entry.get())
  width = float(W_entry.get())
  area = lenght * width
  result_lable.config(text=f'Area: {area} square units')

data=tk.Frame(root)
data.pack()
# Creating Lable
L = tk.Label(data, text="Enter Length: ")
L.grid(row=0, column=0)
L_entry = tk.Entry(data)
L_entry.grid(row=0, column=1)
W = tk.Label(data, text="Enter Width: ")
W.grid(row=1, column=0)
W_entry = tk.Entry(data)
W_entry.grid(row=1, column=1)
Ebutton = tk.Button(data,text='Enter' ,command=recipe)
Ebutton.grid(row=2, column=2)
result = tk.Frame(root)
result.pack()
result_lable = tk.Label(result, text=" ")
result_lable.pack()
root.mainloop()