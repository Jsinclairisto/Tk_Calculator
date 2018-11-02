#/usr/bin/env python3
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
    print(num)
    if (counter > 1):
        text_input.set("Error! Ops cannot be next to eachother")
        content = ""
        counter = 0

def num_press(num):
    global content
    content = content + str(num)
    text_input.set(content)
    print(num)

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

buttons = ['1','2','3','4',
           '5','6','7','8',
           '9','0', '.']
op_buttons = ['+', '-', '*', '/']

row = 1
col = 0
op_row = 2
frame = Frame(root)
root.resizable(0,0)
num_frame = Frame(root)
zero_frame = Frame(root)
root.title("TK Calculator")

for i in buttons:
    action = lambda num = i: num_press(num)
    button = Button(num_frame, text = i, width = 4, bd=5, height = 4, font = 5, command = action) \
		.grid(row = row, column = col, sticky = 'nesw',)
    col += 1
    if col > 4:
        col = 0
        row += 1

for i in op_buttons:
    op_action = lambda num = i: op_press(num)
    button = Button(num_frame, text = i, width = 4, bd=5, height = 4,font = 5, command = op_action)\
             .grid(row = row, column = col, sticky = 'nesw',)
    col += 1
    if col > 4:
        col = 0
        op_row += 1

"""allows us to use the number entry bar"""
text_input = StringVar()

"""Create Entrybox here"""
num_expr = Entry(frame, textvariable = text_input, bd=10, insertwidth = 3, font = 30, width = 25)
eql_button = Button(zero_frame, text = "=", bd=5, command=lambda: equal_event(), width=16, height=2)
clear_button = Button(zero_frame, text = "C", bd=5, command=lambda: clear(), width=16, height=2)

"""passes constraints into the tk grid function for the buttons"""
num_expr.grid(row=0, column=1, sticky=W, pady=4)

eql_button.grid(row=2, column=4, sticky=W, pady=4)
clear_button.grid(row=2, column=5, sticky=W, pady=4)

"""adds these features to the app"""
frame.pack()
num_frame.pack()
zero_frame.pack()

"""Loops program until it is closed"""
root.mainloop()
