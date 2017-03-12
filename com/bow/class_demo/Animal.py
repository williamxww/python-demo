class Animal:
    name = ""
    age = 0

    def __init__(self, name, age):
        print("init Animal")
        self.name = name
        self.age = age

    def tell_name(self):
        print("name is " + self.name)
