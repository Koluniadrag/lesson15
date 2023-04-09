class Person:
    def __init__(self, firstname, lastname, age):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age

    def talk(self):
        print(f"Hello, my name is {self.firstname} {self.lastname} and I'm {self.age} years old.")
carl = Person("Carl", "Johnson", 26)
carl.talk()  # Output: Hello, my name is Carl Johnson and I'm 26 years old.



