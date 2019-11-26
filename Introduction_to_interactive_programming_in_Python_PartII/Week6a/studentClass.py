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


def assign(listOfStudents, studentName, password, project_name):
    
    for student in listOfStudents:
        if student.get_name() == studentName and student.check_password(password):
            projects = student.get_projects()
            if project_name not in projects:
                student.add_project(project_name)




# Testing code

# joe_person = Person("Joe", "Warren", 52)
# joe_student = Student(joe_person, "TopSecret")

# print joe_student.get_name()
# print joe_student.check_password("qwert")
# print joe_student.check_password("TopSecret")

# print joe_student.get_projects()
# joe_student.add_project("Create practice exercises")
# print joe_student.get_projects()
# joe_student.add_project("Implement Minecraft")
# print joe_student.get_projects()

# Testing code assign function
# create some Student objects using Person object
joe = Student(Person("Joe", "Warren", 52), "TopSecret")
joe.add_project("Create practice exercises")
joe.add_project("Implement Minecraft")

scott = Student(Person("Scott", "Rixner", 29), "CodeSkulptor")
scott.add_project("Beat Joe at RiceRocks")

john = Student(Person("John", "Greiner", 47), "outdoors")


# create a list of students
profs = [joe, scott, john]

# test assign
print joe.get_projects()
assign(profs, "Joe Warren", "TopSecret", "Practice RiceRocks")
print joe.get_projects()

print john.get_projects()
assign(profs, "John Greiner", "OUTDOORS", "Work on reflexes")
print john.get_projects()
assign(profs, "John Greiner", "outdoors", "Work on reflexes")
print john.get_projects()
