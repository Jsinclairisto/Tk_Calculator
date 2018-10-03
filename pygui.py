"""Basic GUI calculator made in python"""
"""Copyright (C) 2018 Jakob Fletcher"""
from tkinter import *
from tkinter import ttk
from math import *

"""Updates text_input box according to what numeric button you press"""
def op_press(num):
    global counter
    global content
    content = content + str(num)
    text_input.set(content)
    counter = counter + 1

    if (counter > 1):
        text_input.set("Error! Ops cannot be next to eachother")
        content = ""
        counter = 0

def num_press(num):
    global content
    content = content + str(num)
    text_input.set(content)

"""Clears text box by clearing the content variable"""
def clear():
    global content
    global counter
    content = ""
    text_input.set(content)
    counter = 0

"""Uses built in python function eval once equals is clicked"""

def equal_event():
    try:
        global content
        global counter
        total = str(eval(content))
        text_input.set(total)
        content = ""
        counter = 0

    except:
        text_input.set("ERROR! Nothing to calculate")
        content = ""
        counter = 0

root = Tk()

counter = 0
content = ""

frame = Frame(root)
root.resizable(0,0)
num_frame = Frame(root)
zero_frame = Frame(root)
root.title("TK Calculator")

"""allows us to use the number entry bar"""
text_input = StringVar()

"""Create the buttons here"""
num_expr = Entry(frame, textvariable = text_input, bd=10, insertwidth = 3, font = 30, width = 23)
button_7 = Button(num_frame, text="7", bd=5, command=lambda: num_press(7), width=2, height=2)
button_4 = Button(num_frame, text="4", bd=5, command=lambda: num_press(4), width=2, height=2)
button_1 = Button(num_frame, text="1", bd=5, command=lambda: num_press(1), width=2, height=2)
button_8 = Button(num_frame, text="8", bd=5, command=lambda: num_press(8), width=2, height=2)
button_5 = Button(num_frame, text="5", bd=5, command=lambda: num_press(5), width=2, height=2)
button_2 = Button(num_frame, text="2", bd=5, command=lambda: num_press(2), width=2, height=2)
button_9 = Button(num_frame, text="9", bd=5, command=lambda: num_press(9), width=2, height=2)
button_6 = Button(num_frame, text="6", bd=5, command=lambda: num_press(6), width=2, height=2)
button_3 = Button(num_frame, text="3", bd=5, command=lambda: num_press(3), width=2, height=2)
button_0 = Button(zero_frame, text = "0", bd=5, command=lambda: num_press(0), width = 10, height=2)
add_button = Button(num_frame, text = "+", bd=5, command=lambda: op_press("+"), width=2, height=2)
sub_button = Button(num_frame, text = "-", bd=5, command=lambda: op_press("-"), width=2, height=2)
mult_button = Button(num_frame, text = "*", bd=5, command=lambda: op_press("*"), width=2, height=2)
div_button = Button(num_frame, text = "/", bd=5, command=lambda: op_press("/"), width=2, height=2)
eql_button = Button(num_frame, text = "=", bd=5, command=lambda: equal_event(), width=2, height=2)
clear_button = Button(num_frame, text = "C", bd=5, command=lambda: clear(), width=2, height=2)

dec_button = Button(zero_frame, text = ".", bd=5, command=lambda: num_press("."), width = 2, height=2)

"""passes constraints into the tk grid function for the buttons"""
num_expr.grid(row=0, column=1, sticky=W, pady=4)
button_7.grid(row=1, column=0, sticky=W, pady=4)
button_4.grid(row=2, column=0, sticky=W, pady=4)
button_1.grid(row=3, column=0, sticky=W, pady=4)
button_8.grid(row=1, column=1, sticky=W, pady=4)
button_5.grid(row=2, column=1, sticky=W, pady=4)
button_2.grid(row=3, column=1, sticky=W, pady=4)
button_9.grid(row=1, column=2, sticky=W, pady=4)
button_6.grid(row=2, column=2, sticky=W, pady=4)
button_3.grid(row=3, column=2, sticky=W, pady=4)

add_button.grid(row=1, column=3, sticky=W, pady=4)
sub_button.grid(row=2, column=3, sticky=W, pady=4)
mult_button.grid(row=3, column=3, sticky=W, pady=4)
div_button.grid(row=1, column=4, sticky=W, pady=4)
eql_button.grid(row=2, column=4, sticky=W, pady=4)
clear_button.grid(row=3, column=4, sticky=W, pady=4)

button_0.grid(row=3, column=0, sticky=S)
dec_button.grid(row=3, column=1)

"""adds these features to the app"""
frame.pack()
num_frame.pack()
zero_frame.pack()

"""Loops program until it is closed"""
root.mainloop()
