class Car:
    engine = "v8"
    def __init__(self, value):
        self.gear = value

obj = Car("auto")
obj.engine += "spyder"

obj2 = Car("dug")
print(obj2.engine)
