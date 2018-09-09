
import sys

lock = threading.Lock()

MAXMONTH = 72
INTERVALL = 10

class Dog():
    def __init__(self):
        print("Staring Tamagotchy")
        self.name = raw_input("dog name> ")
        self.running = True
        self.hungry = 3

    def feed(self):
        self.hungry += 3
        self.stats()

    def stats(self):
        print(self.hungry)
        print(self.name)

    def quit(self):
        self.runing = False
        sys.exit()

    def run(self):
        while self.running == True & self.hungry >= 0:
            input = raw_input()
            if input == "quit":
                quit()
                sys.exit()
            elif input == "feed":
                self.feed()
            elif input == "stats":
                self.stats()
            else:
                print("no valid input")


d = Dog()
d.start()

#python3 ~/dev/python/tamagotchy/main.py
