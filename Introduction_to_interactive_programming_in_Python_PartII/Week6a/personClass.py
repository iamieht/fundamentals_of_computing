class Person(object):
    def __init__(self, name, lastname, year):
        self.first_name = name
        self.last_name = lastname
        self.birth_year = year
    
    def full_name(self):
        return self.first_name + " " + self.last_name
    
    def age(self, currentYear):
        return currentYear - self.birth_year
    
    def __str__(self):
        return "Person's name is " + self.full_name() + ". " + "Their birth year is " + str(self.birth_year)


me = Person("Ivan", "Hernandez", 1977)
print me.full_name()
print me
print me.age(2019)