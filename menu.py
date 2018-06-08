#!/usr/bin/env python3
import tkinter as tk
import os
def setup():
    os.system("MacFaceID/training_data.py")
def password_change():
    os.system("MacFaceID/credentials.py")
def startit():
    os.system("MacFaceID/sleepwatcher -w MacFaceID/unlock_it.wakeup")
def stopit():
    command = "pgrep -f sleepwatcher | awk '{print \"kill -9 \"$1}' | sh"
    os.system(command)
root = tk.Tk()
root.geometry('300x160')
root.title('Password Request')
#frame for window margin
parent = tk.Frame(root, padx=10, pady=10)
parent.pack(fill=tk.BOTH, expand=True)
#button to attempt to login
a = tk.Button(parent, borderwidth=4, text="SetUp", width=10, pady=8, command=setup)
b = tk.Button(parent, borderwidth=4, text="Password", width=10, pady=8, command=password_change)
c = tk.Button(parent, borderwidth=4, text="Start", width=10, pady=8, command=startit)
d = tk.Button(parent, borderwidth=4, text="Stop", width=10, pady=8, command=stopit)
d.pack(side=tk.BOTTOM)
c.pack(side=tk.BOTTOM)
b.pack(side=tk.BOTTOM)
a.pack(side=tk.BOTTOM)
parent.mainloop()
