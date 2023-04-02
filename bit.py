def b():
    logic.name(a)
    logic.edit(1,1,1,bitcav)
import tkinter as tk
from tkinter import Canvas
from tkinter import *
import keyboard,time
import logic
#from nw import *
main = tk.Tk()


main.geometry("800x600")
a = Listbox(main)
a.pack(side = LEFT,fill= BOTH)
scrollbar = Scrollbar(main)
a.config(yscrollcommand = scrollbar.set)
scrollbar.config(command = a.yview)
menubar = Menu(main)
main.config(menu=menubar)
file_menu = Menu(menubar)
file_menu.add_command(
    label='New ctrl+n',
    command=b
)
file_menu.add_command(
    label='Exit alt+f4',
    command=main.destroy
)
menubar.add_cascade(
    label="File",
    menu=file_menu
)
bitcav = Canvas(main,width=600,height=600)
bitcav.pack()
while True:
    if keyboard.is_pressed("ctrl + n"):
        time.sleep(0.1)
        b()
        
    bitcav.update()
main.mainloop()
