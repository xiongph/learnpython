#基类（父类/超类）与子类
#继承与多态

class Animal(object):
    '''Animal class type'''
    def tell(self):
        '''Animal tell()'''
        print("I'm an animal..")

class Dog(Animal):
    '''Dog class type'''
    def tell(self):
        '''Dog tell()'''
        print("I'm a dog...")

class Cat(Animal):
    '''Cat class type'''
    def tell(self):
        ''' Cat tell()'''
        print("I,m a cat...")

def run_tell(animal):
    ''' Animal tell()'''
    animal.tell()

a = Animal()
b = Dog()
c = Cat()
a.tell()
b.tell()
c.tell()

run_tell(a)
run_tell(b)
run_tell(c)
