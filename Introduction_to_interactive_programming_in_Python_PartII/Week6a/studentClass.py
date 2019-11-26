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

class Student(Person):
    def __init__(self, person, password):
        self.person = person
        self.password = password
        self.projects = []
    
    def get_name(self):
        return self.person.full_name()
    
    def check_password(self, spassword):
        return spassword == self.password
    
    def get_projects(self):
        return self.projects
    
    def add_project(self, project_name):
        self.projects.append(project_name)

# Testing code

joe_person = Person("Joe", "Warren", 52)
joe_student = Student(joe_person, "TopSecret")

print joe_student.get_name()
print joe_student.check_password("qwert")
print joe_student.check_password("TopSecret")

print joe_student.get_projects()
joe_student.add_project("Create practice exercises")
print joe_student.get_projects()
joe_student.add_project("Implement Minecraft")
print joe_student.get_projects()
