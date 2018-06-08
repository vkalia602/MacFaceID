#!/usr/bin/env python3
import rumps
import subprocess
import os


class MacFace(rumps.App):
    child_process = None
    def child():
        os.system("MacFaceID/sleepwatcher -w MacFaceID/unlock_it.wakeup")
        child_process = os.getpid()
        os._exit(0)  

    def parent():
#        sender.state = not sender.state
        newpid = os.fork()
        if newpid == 0:
            child()
        else:
            pids = (os.getpid(), newpid)
            print("parent: %d, child: %d\n" % pids)
        
    @rumps.clicked("SetUp")
    def setup(self, _):
        value = rumps.alert("You are entering the setup")
        if value is 1:
            subprocess.Popen("MacFaceID/training_data.py")
        else:
            rumps.alert("Fine then, Go to hell")

    @rumps.clicked("Launch MacFace")
    def onoff(self, sender):
#        os.system("MacFaceID/sleepwatcher -w MacFaceID/unlock_it.wakeup")
        newpid = os.fork()
        if newpid == 0:
            child()
#        parent()
#        subprocess.Popen("MacFaceID/train_detect.py")

    @rumps.clicked("Stop")
    def stop_macface(self, _):
        if child_process is not None:
            child_process.terminate()

if __name__ == "__main__":
    MacFace("MF").run()
