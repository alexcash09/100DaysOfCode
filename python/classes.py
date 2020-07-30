class MyClass:
    a = 123
    def hello(self):
        print('inside hello function')
        return 'hello world'

myClass = MyClass()

print(myClass.hello())

class Dog:

    kind = 'canine'         # class variable shared by all instances
    change = 'iwanttochange'

    def __init__(self, name, change):
        self.name = name    # instance variable unique to each instance
        self.change = change

myDog = Dog('harlow', 'please change')
yourDog = Dog('luna', 'dont change')
print(myDog.name)
print(myDog.kind)
myDog.kind = 'cat'
print('myDog: ', myDog.change)
print('youtDog: ', yourDog.change)
print('yourDog.kind: ', yourDog.kind)


class Bag:
    def __init__(self):
        self.data = []

    def add(self, x):
        self.data.append(x)

    def addtwice(self, x):
        self.add(x)
        self.add(x)

bag = Bag()

bag.add('hello')
bag.addtwice('world')

print(bag.data)