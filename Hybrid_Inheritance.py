class Person:
    def __init__(self, name):
        self.name = name
    def show_name(self):
        print("Name:", self.name)

class Student(Person):
    def __init__(self, name, roll_no):
        super().__init__(name)
        self.roll_no = roll_no
    def show_student(self):
        print("Roll No:", self.roll_no)

class Course:
    def __init__(self, course_name):
        self.course_name = course_name
    def show_course(self):
        print("Course:", self.course_name)

class StudentDetails(Student, Course):
    def __init__(self, name, roll_no, course_name):
        Student.__init__(self, name, roll_no)
        Course.__init__(self, course_name)
    def show_details(self):
        self.show_name()
        self.show_student()
        self.show_course()

s = StudentDetails("Rahul", 12, "Computer Science")
s.show_details()
