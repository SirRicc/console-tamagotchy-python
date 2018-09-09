
import sys
import datetime
import time

class Dog():
    def __init__(self):
        print "Staring Tamagotchy \n"
        self.name = raw_input("How do you call him?  \n")
        print "\nWelcome to I´m bad with names!.\nRaise %s and become best friends \n" % (self.name,)
        print "Write  help  to view your commands"
        self.running = True
        self.hungry = 1

    #Incremnting self.hungry causes to end my while loop down here.
    def feed(self):
        self.hungry += 1
        print "~TastyBark\n"

    def help(self):
        print "stats\nfeed\nquit\n"

    def stats(self):
        print "\n\n    ~OVERVIEW~\nHis name is: ", self.name
        print "Hungry level at: ", self.hungry, "\n\n"

    def quit(self):
        self.runing = False
        sys.exit()

    def input(self):
        input = raw_input()
        if input == "quit":
            quit()
            sys.exit()
        if input == "help":
            self.help()
        elif input == "feed":
            self.feed()
        elif input == "stats":
            self.stats()
        else:
            print "no valid input"

    #Timer is not executing well
    def timer(self):
        t = datetime.datetime.now()
        if  t.second % 6 == 0:
            self.stats()
            time.sleep(1)

    #Handle starvation in another way - Look Line20.
    def run(self):
        while self.running == True: # & self.hungry > 0:
            self.input()
            #self.timer()



d = Dog()
d.run()
#python ~/dev/python/tamagotchy/main.py
