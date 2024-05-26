from tkinter import*
def clear():
    global expression
    global lable_show_cal
    result="0"
    expression =""
    lable_show_cal.set(result)
    
def press(number):
    global expression
    global lable_show_cal
    expression=expression+number
    lable_show_cal.set(expression)
def equal():
    try:
        global expression
        global lable_show_cal
        result=str(eval(expression))
        lable_show_cal.set(result)
    except:
        result="error"
        expression=""
        lable_show_cal
    lable_show_cal.set(result)
def undo():
    global expression
    global lable_show_cal
    if len(expression) > 0:
        expression = expression[:-1]
        lable_show_cal.set(expression)

m=Tk()
m.title("Calcuator")
m.configure(bg='black')
m.option_add("font","consolas 30")
m.option_add("*Font", "consolas 20")
lable_show_cal=StringVar()
lable_show_cal.set(0)
expression=""
 
Label(m,textvariable=lable_show_cal,  bg="lightgrey",  width=10,  font="k2d  40",fg="grey").grid(row=0,column=0,columnspan=4,  sticky="news")
Button(m,text="AC",command=clear,  bg="orange",relief="flat").grid(row=1,column=0,sticky="news")
Button(m,text="<-",command=undo,  bg="orange",relief="flat").grid(row=1,column=3,sticky="news")
Button(m,text="(", command=lambda: press("("),bg="orange",relief="flat").grid(row=1, column=1, sticky = "news")
Button(m,text=")", command=lambda: press(")"),bg="orange",relief="flat").grid(row=1, column=2, sticky = "news")

Button(m,text="7",command=lambda:press("7"),  bg="darkgrey",relief="flat").grid(row=2,column=0,  sticky="news")
Button(m,text="8",command=lambda:press("8"),  bg="darkgrey",relief="flat").grid(row=2,column=1,  sticky="news")
Button(m,text="9",command=lambda:press("9"),  bg="darkgrey",relief="flat").grid(row=2,column=2,  sticky="news")
Button(m,text="/",command=lambda:press("/"),  bg="darkgrey",relief="flat").grid(row=2,column=3,  sticky="news")
 
Button(m,text="4",command=lambda:press("4"),  bg="darkgrey",relief="flat").grid(row=3,column=0,  sticky="news")
Button(m,text="5",command=lambda:press("5"),  bg="darkgrey",relief="flat").grid(row=3,column=1,  sticky="news")
Button(m,text="6",command=lambda:press("6"),  bg="darkgrey",relief="flat").grid(row=3,column=2,  sticky="news")
Button(m,text="*",command=lambda:press("*"),  bg="darkgrey",relief="flat").grid(row=3,column=3,  sticky="news")
 
Button(m,text="1",command=lambda:press("1"),  bg="darkgrey",relief="flat").grid(row=4,column=0,  sticky="news")
Button(m,text="2",command=lambda:press("2"),  bg="darkgrey",relief="flat").grid(row=4,column=1,  sticky="news")
Button(m,text="3",command=lambda:press("3"),  bg="darkgrey",relief="flat").grid(row=4,column=2,  sticky="news")
Button(m,text="-",command=lambda:press("-"),  bg="darkgrey",relief="flat").grid(row=4,column=3,  sticky="news")
 
Button(m,text="0",command=lambda:press("0"),  bg="darkgrey").grid(row=5,column=0,  sticky="news")
Button(m,text=".",command=lambda:press("."),  bg="darkgrey").grid(row=5,column=2,  sticky="news")
Button(m,text="00",command=lambda:press("00"),  bg="darkgrey").grid(row=5,column=1,  sticky="news")
Button(m,text="+",command=lambda:press("+"),  bg="darkgrey").grid(row=5,column=3,  sticky="news")
 
Button(m,text="=",command=equal,  bg="gold").grid(row=6,column=0,columnspan=4,sticky="news")
m.mainloop()