#!/usr/bin/env python3
"""
This module defines class for menu bar item and the options
user can click on. 
Includes features like:
    Setup
    Password (create/change)
    onoff- Launching daemon
    stop - stop the daemon from running
"""
import rumps
import subprocess
import os


class MacFace(rumps.App):
    new_process = None
    @rumps.clicked("SetUp")
    def setup(self, _):
        """
        Method to access setup options to create or change training data
        """
        subprocess.Popen([os.path.expanduser('~/MacFaceID/training_data.py')])

    @rumps.clicked("Password")
    def password(self, _):
        """
        Method to create or change password. Calls the script which 
        saves the password in keychain.
        """
        subprocess.Popen([os.path.expanduser("~/MacFaceID/credentials.py")])
        
    @rumps.clicked("Launch MacFace")
    def onoff(self, sender):
        """
        Method to launch MacFace daemon, saves process in class attribute new_process
        """
        self.new_process = subprocess.Popen([os.path.expanduser('~/MacFaceID/sleepwatcher'), '-w', os.path.expanduser('~/MacFaceID/unlock_it.wakeup')])

    @rumps.clicked("Stop")
    def stop_macface(self, _):
        """
        Method to stop the app from running. Uses kill to kill the 
        process launched in Launch Macface button
        """
        kill_it = "kill -9 {}".format(self.new_process.pid)
        os.system(kill_it)

    @rumps.clicked('Quit')
    def clean_up_before_quit(self,_):
        kill_it = "kill -9 {}".format(self.new_process.pid)
        os.system(kill_it)
        rumps.quit_application()

if __name__ == "__main__":
    app = MacFace('MF', quit_button=None)
    app.run()
