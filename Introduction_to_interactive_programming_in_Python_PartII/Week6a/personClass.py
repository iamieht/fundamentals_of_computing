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

# Test Person Class
# me = Person("Ivan", "Hernandez", 1977)
# print me.full_name()
# print me
# print me.age(2019)

def average_age(listOfPersons, currentYear):
    totalAges = 0

    for person in listOfPersons:
        totalAges += person.age(currentYear)
    
    return totalAges / len(listOfPersons)


# Test average_age
ivan = Person("Ivan", "Hernandez", 1977)
maria = Person("Maria", "Antonieta", 1986)
josefina = Person("Jose", "Fina", 1990)
rosa = Person("Rosa", "Melo", 2000)
jessica = Person("Jessica", "Jones", 1999)
cojo = Person("Co", "Jones", 2001)

listOfPersons = [ivan, maria, josefina, rosa, jessica, cojo]

print average_age(listOfPersons, 2019)