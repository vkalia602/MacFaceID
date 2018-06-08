#!/usr/bin/env python3
import tkinter as tk
import keyring
def make_entry(parent, caption, width=None, **options):
    tk.Label(parent, text=caption).pack(side=tk.TOP)
    entry = tk.Entry(parent, **options)
    if width:
        entry.config(width=width)
    entry.pack(side=tk.TOP, padx=10, fill=tk.BOTH)
    return entry
def enter(event):
    check_password()
def check_password():
    if (user.get() == password.get()):
        keyring.set_password("MacFace", "Account-name", password.get())        
        root.title('Recorded')
        return
    else:
        root.title('Try again')
root = tk.Tk()
root.geometry('300x160')
root.title('Password Request')
#frame for window margin
parent = tk.Frame(root, padx=10, pady=10)
parent.pack(fill=tk.BOTH, expand=True)
#entrys with not shown text
user = make_entry(parent, "Password:", 16, show='*')
password = make_entry(parent, "Confirm Password:", 16, show="*")
#button to attempt to login
b = tk.Button(parent, borderwidth=4, text="OK", width=10, pady=8, command=check_password)
b.pack(side=tk.BOTTOM)
password.bind('<Return>', enter)
user.focus_set()
parent.mainloop()
