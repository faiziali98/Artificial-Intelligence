
class Vehicle:
    def __init__(self):
        pass
    def getName(self):
        pass
class Car(Vehicle):
    def __init__(self,name,wheels):
        Vehicle.__init__(self)
        self.name=name
        self.wheels=wheels
    def getName(self):
        return self.name
    def describeMe(self):
        print (self.name+' '+`self.wheels`)


class Bike(Vehicle):
    def __init__(self,name,wheels):
        Vehicle.__init__(self)
        self.name=name
        self.wheels=wheels
    def getName(self):
        return self.name
    def describeMe(self):
        print (self.name+' '+`self.wheels`)

if __name__ == '__main__':
    s=Car("Honda",4)
    s.describeMe()