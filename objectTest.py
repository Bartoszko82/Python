#Chapter 4 
import time
#
#def funkcjaTestowa(mojeImie):
#    print("Witaj %s" % mojeImie)
#    print("Obecna godzina to ", time.asctime())
#    
#
#funkcjaTestowa("Bartek")

class Dog(object):
    def bark(self):
        print("Woof! Woof!")
        
burek = Dog()
burek.bark()


class Dog(object):

    def __init__(self, name):
        self.name = name

    def bark(self):
        return "Woof! %s! Woof!" % (self.name,)

burek = Dog("Burek")
pluto = Dog("Pluto")
print(burek.bark())
print(pluto.bark()
