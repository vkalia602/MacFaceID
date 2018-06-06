#!/usr/bin/env python3
from tkinter import Label, Tk, Frame
from time import sleep
import sys
root = Tk()
def center_window(w=300, h=200):
    # get screen width and height
    ws = root.winfo_screenwidth()
    hs = root.winfo_screenheight()
    # calculate position x, y
    x = (ws/2) - (w/2)    
    y = (hs/2) - (h/2)
    root.geometry('%dx%d+%d+%d' % (w, h, x, y))
def close_after_2s():
    try:
        root.destroy()
    except:
        pass

def display_instruction(prompt=""):
    label1 = Label(text=prompt, width=len(prompt))
    label1.pack()
#    center_window(500, 300)
    try:
        root.after(2000, close_after_2s)
        root.mainloop()
    except:
        pass

if __name__ == '__main__':
    display_instruction("Heloo worldf")
