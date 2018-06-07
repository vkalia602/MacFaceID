#!/usr/bin/env python3
import rumps
import subprocess
import os
def child():
    os.system("MacFaceID/sleepwatcher -w MacFaceID/unlock_it.wakeup")
    print('\nA new child ',  os.getpid())
    os._exit(0)  

def parent():
   while True:
      newpid = os.fork()
      if newpid == 0:
         child()
      else:
         pids = (os.getpid(), newpid)
         print("parent: %d, child: %d\n" % pids)
      reply = input("q for quit / c for new fork")
      if reply == 'c': 
          continue
      else:
          break
class MacFace(rumps.App):
    @rumps.clicked("SetUp")
    def setup(self, _):
        value = rumps.alert("You are entering the setup")
        if value is 1:
            subprocess.Popen("MacFaceID/training_data.py")
        else:
            rumps.alert("Fine then, Go to hell")

    @rumps.clicked("Launch MacFace")
    def onoff(self, sender):
        sender.state = not sender.state
#        os.system("MacFaceID/sleepwatcher -w MacFaceID/unlock_it.wakeup")
        parent()
#        subprocess.Popen("MacFaceID/train_detect.py")

    @rumps.clicked("Say hi")
    def sayhi(self, _):
        rumps.notification("Awesome title", "amazing subtitle", "hi!!1")

if __name__ == "__main__":
    MacFace("MF").run()
