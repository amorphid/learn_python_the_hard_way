## Animal is-a object (yes, sort of confusing) look at the extra credit
class Animal(object):
    pass

## a class that inherits from Animal
class Dog(Animal):

    def __init__(self, name):
        # set dog's name
        self.name = name

# another class that inherits from Animal
class Cat(Animal):

    def __init__(self, name):
        # set cat's name
        self.name = name

# class that inherits from object
class Person(object):

    def __init__(self, name):
        # set person's name
        self.name = name

        # Person may have a pet, but doesn't when created
        self.pet = None

# class inherits from Person
class Employee(Person):

    def __init__(self, name, salary):
        # calls name method on super class
        super(Employee, self).__init__(name)
        # sets employee's salary
        self.salary = salary

# class inherits from object
class Fish(object):
    pass

# class inherits from Fish
class Salmon(Fish):
    pass

# class inherits from Fish
class Halibut(Fish):
    pass


# rover is-a Dog
rover = Dog("Rover")

# satan is-a Cat
satan = Cat("Satan")

# Mary is a Person
mary = Person("Mary")

# mary has a cat
mary.pet = satan

# frank is an employee
frank = Employee("Frank", 120000)

# frank has a dog
frank.pet = rover

# flipper is a Fish
flipper = Fish()

# crouse is a Salmon
course = Salmon()

# harry is a Halibut()
harry = Halibut()
