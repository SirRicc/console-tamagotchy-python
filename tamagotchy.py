import time

MAXMONTH = 72
INTERVALL = 10

class Dog():
    def __init__(self):
        self.name = input("Give him a name: ")
        self.month = 0
        self.running = True
        self.hungry = 7
    
    #Not working yet
    def feed(self):
        if self.hungry < 10:
            print("TastyWoof!")
        else:
            print("He don´t want to eat.")
    
    #Display basic imformations
    def stats(self):
        print("His name is :" , self.name)
        print("Your dog is " , self.month , "months old.")
        print("His hungry level is: " , self.hungry)
        print(" ")
    
    #Very basic game-loop
    def run(self):
        while self.running == True:
            if self.month > MAXMONTH or self.hungry <= 0:
                print("RIP Dog")
                self.runing = False
                break
            else:
                self.stats()
                self.month += 1
                self.hungry -= 2
                time.sleep(INTERVALL)

#Summon a dog!
d = Dog()
d.run()
