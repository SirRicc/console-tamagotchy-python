#I decided to throw this threading idea for a simpler game loop

import threading
import time
import sys

INTERVALL = 6

global running
global data
running = True
data = 5

class test(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        global data
        global running
        print("run exectuting ...")
        i = 0
        while running == True:
            print(data)
            time.sleep(INTERVALL)

def increase():
    global data
    data += 1
    print "data increased to: ", data

def quit():
    global running
    running = False

t = test()
t.deamon = True
t.setName('test')
t.start()

while True:
    if raw_input() == "quit":
        quit()
        sys.exit()
    elif raw_input() == "increase":
        increase()
    else:
        print "no valid input"
