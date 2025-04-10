from abc import ABC,abstractmethod
class absclass (ABC):
    def print (self,x):
        print("passing value",x)
    @abstractmethod
    def task (self):
        print("we are inside Abclass task")
class test_class(absclass):
    def task (self):
        print("We are inside test_class task")
test_obj = test_class()
test_obj.task()
test_obj.print(39201927)
# obj=absclass()
# obj.task()