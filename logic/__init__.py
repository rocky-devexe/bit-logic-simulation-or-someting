import sys,os
import tkinter as tk
from tkinter import Canvas
from tkinter import Button
from tkinter import Text
from tkinter import *
from logic import a1
#except
line = -1
def name(listbox):
    global line
    mw = tk.Tk()
    mc = Canvas(mw)
    mw.geometry("600x300")
    def num():
        global line
        line = line + 1
        listbox.insert(END, line)
        mw.destroy()
    def text():
        global line
        INPUT = inputtxt.get("1.0", "end-1c")
        line = line + 1
        if INPUT == "":
            listbox.insert(END, line)
        else:
            
            listbox.insert(END, INPUT)
        print(INPUT)
        mw.destroy()
    def calc():
        global line
        line = line - 1
        mw.destroy()
    turn_off = Button(mw, text="defelt", command=num)
    turn_off.pack(side=RIGHT)
    h = Button(mw, text="cancel", command=calc)
    h.pack(side=RIGHT)
    turn_on = Button(mw, text="ok",command=text)
    turn_on.pack(side=RIGHT)
    inputtxt = Text(mw, height = 10,width = 25)
    inputtxt.pack(side=LEFT)
    #while True:
    #    mc.update()
def edit(a,b,c,ca):
    if a == 1:
        a1.a(ca)
        print("omg")
    if b == 1:
        print("bom")
    if c == 1:
        print("fuck")
