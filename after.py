class bmw ():
    def fual(self):
        print("The fuel in a Bmw is 91")
    def max (self):
        print("230 is the max speed of a Bmw")   
class  Ferrari  ():
    def fual(self):
        print("the fuel in a ferrari is 91")
    def max (self):
        print("250 is the max speed of a Ferrari")    
obj_b=bmw()
obj_f=Ferrari()
for country in (obj_b,obj_f):
    country.fual()
    country.max()
