from tkinter import *

root = Tk()
root.title("Calculator")
root.geometry("500x500")

def opration(number):
    global op
    op = op + str(number)
    screen_output.set(op)

def evaluate_1():
    global op
    Output = eval(op)
    screen_output.set(Output)


def clear():
    global op
    op = ""
    screen_output.set(op)


op = ""
print(op)
screen_output = IntVar()




e1 = Entry(root, bg="black", fg="yellow",  width=30,font = ("Arial",13))
e1.place(x=80, y=10)

def button_add(number):
    return

button_7 = Button(root, text="1",bg="green",fg="yellow", bd=8, padx=10, pady=10, font=20, command =lambda:opration(7))
button_7.place(x=4,y=38)

button_8 = Button(root, text="2",bg="green" ,fg="yellow", bd=8, padx=10, pady=10, font=20,command =lambda:opration(8))
button_8.place(x=70,y=38)

button_9 = Button(root, text="3",bg="green",fg="yellow", bd=8, padx=10, pady=10, font=20,command =lambda:opration(9))
button_9.place(x=140,y=38)

# button_del = Button(root, text="DEl",bg="sky blue", bd=8, padx=10, pady=10, font=20,command =lambda:opration())
# button_del.place(x=210, y=38)

button_AC = Button(root, text="AC",bg="sky blue", bd=8, padx=10, pady=10, font=20, command=lambda:clear())
button_AC.place(x=290, y=38)

button_4 = Button(root, text="4",bg="green",fg="yellow", bd=8, padx=10, pady=10, font=20, command =lambda:opration(4))
button_4.place(x=4, y=110)

button_5 = Button(root, text="5",bg="green",fg="yellow", bd=8, padx=10, pady=10, font=20, command =lambda:opration())
button_5.place(x=70, y=110)

button_6 = Button(root, text="6",bg="green",fg="yellow", bd=8, padx=10, pady=10, font=20, command =lambda:opration())
button_6.place(x=140, y=110)

button_mul = Button(root, text="*",bg="sky blue", bd=8, padx=10, pady=10, font=20, command =lambda:opration())
button_mul.place(x=210, y=110)

button_div= Button(root, text="/",bg="sky blue", bd=8, padx=12, pady=10, font=20, command =lambda:opration())
button_div.place(x=290, y=110)

button_1 = Button(root, text="1",bg="green",fg="yellow", bd=8, padx=10, pady=10, font=20, command =lambda:opration())
button_1.place(x=4, y=190)

button_2 = Button(root, text="2",bg="green",fg="yellow", bd=8, padx=10, pady=10, font=20, command =lambda:opration())
button_2.place(x=70, y=190) 

button_3 = Button(root, text="3",bg="green",fg="yellow", bd=8, padx=10, pady=10, font=20, command =lambda:opration())
button_3.place(x=140, y=190)

button_add = Button(root, text="+",bg="sky blue", bd=8, padx=10, pady=10, font=20, command =lambda:opration())
button_add.place(x=210, y=190)


button_Sub = Button(root, text="-",bg="sky blue", bd=8, padx=10, pady=10, font=20,command =lambda:opration())
button_Sub.place(x=290, y=190)

button_0 = Button(root, text="0",bg="green",fg="yellow", bd=8, padx=10, pady=10, font=20,command =lambda:opration())
button_0.place(x=4, y=270)

button_point = Button(root, text=".",bg="sky blue", bd=8, padx=10, pady=10, font=20,command =lambda:opration())
button_point.place(x=70, y=270)

button_equal = Button(root, text="=",bg="sky blue", bd=8, padx=10, pady=10, font=20,command =lambda:opration())
button_equal.place(x=290, y=270)




root.mainloop()
