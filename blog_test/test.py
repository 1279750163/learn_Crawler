from abc import abstractmethod, ABCMeta

class Vehicle(meteaclass=ABCMeta):
    @abstractmethod
    def move(self):
        pass


class train(Vehicle):
    def move(self):
        print("train move")

class plane(Vehicle):
    def move(self):
        print("plane fly")

class car(Vehicle):
    def move(self):
        print("car drive")
