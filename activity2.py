from abc import ABC,abstractmethod
class amimal (ABC):
    def move (self):
        pass
class Human (amimal):
    def move (self):
        print("i can walk")
class cheetha (amimal):
    def move (self):
        print("i can run")
class dog (amimal):
    def move (self):
        print("i can eat")
r=Human()
r.move()
r=cheetha()
r.move()
r=dog()
r.move()