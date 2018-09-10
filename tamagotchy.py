# -*- coding: utf-8 -*-

from threading import Thread,Lock
import sys
import datetime
import time

#Just a class for holding variables so they're not global
class Dog():
    pass

d = Dog()
d.running = True
d.hungry = 3
d.lock = Lock()



#Here we see our methods
def feed():
    with d.lock:
        d.hungry += 1
        print "~TastyBark\n"

def stats():
    with d.lock:
        print "\n\n    ~OVERVIEW~\nHis name is: ", d.name
        print "Hungry level at: ", d.hungry, "\n\n"

def help():
    with d.lock:
        print "stats\nfeed\nquit\n"

def quit():
    with d.lock:
        d.running = False
        sys.exit()



#This is a thread for continuously updated stats & hungry
def loop(sec):
    while d.running == True:
        t = datetime.datetime.now()
        #Updates & print stats
        if  t.second % sec == 0:
            stats()
            time.sleep(1)
            #Intervall to decrease hungry
        elif  t.second % 21 == 0:
            d.hungry -= 1
            time.sleep(1)
            print "Hungry decreased to ", d.hungry
    
#Thread for handling inputs
def input():
    while d.running == True:
        input = raw_input()
        if input == "quit":
            quit()
        elif input == "feed":
            feed()
        elif input == "help":
            help()
        elif input == "stats":
            stats()
        else:
            print "no valid input"
    sys.exit()

#It's kinda like a welcome screen when starting the game - and a thread aswell.
#But all threads need to wait for this one before executing.
def welcome():
    print "Staring Tamagotchy \n"
    d.name = raw_input("Give him a name: \n")
    print "\nWelcome to I´m bad with names!\nRaise %s and become best friends! " % (d.name)
    print "Write  help  to view your commands"

#I feel like this is not nessecary as sson as I learn more about deamons because stuff should exit itself.
def alive():
    while d.running == True:
        if d.hungry <= 0:
            print "Your Dog died. Type   quit   to exit."
            quit()



#Basic Thread management
w = Thread(target=welcome)
w.start()
w.join()


l = Thread(target=loop, args=(10,))
l.start()

i = Thread(target=input)
i.start()

a = Thread(target=alive)
a.start()

