#!/usr/bin/env python3
import keyring
import os


"""
cmd = osascript -e 'display dialog "Please enter a your login password." default answer "" with icon stop buttons {"Cancel", "Continue"} default button "Continue" with hidden answer'
os.system(cmd)
"""
keyring.set_password("MacFace", "user", password)
