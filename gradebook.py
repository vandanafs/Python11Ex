from uuid import uuid4

from enum import Enum

class AliveStatus(Enum):
    DECEASED=0
    ALIVE=1


class Person():
    def __init__(self):
     self.first_name=None
     self.last_name=None
     self.date_of_birth=None
     self.alive=None

def update_first_name(self,first_name):
    self.first_name=first_name

def update_last_name(last_name, self):
    self.last_name=last_name

def update_dob(self,dob):
    self.date_of_birth=dob

def update_status(self,alive):
    self.alive=alive

class Instructor(Person):
    def __init__(self,f_name,l_name,dob,alive):
        super().__init__(f_name,l_name,dob,alive)
        self.instructor_id= f'Instructor_{uuid4()}'

class  Student(Person):
    def __init__(self, f_name, l_name, dob, alive):
        super().__init__(f_name, l_name, dob, alive)
        self.studnet_id = f'Student_{uuid4()}'

class ZipCodeStudent(Student):
      def __init__(self,f_name,l_name,dob,alive):
          super().__init__(f_name,l_name,dob,alive)


class CollegeStudent(Student):
       def __init__(self,f_name,l_name,dob,alive,student_id):
           super().__init__(f_name,l_name,dob,alive,student_id)



class Classroom():
    def __init__(self,students:list,instructors:list):
        self.students={}
        self.instructors={}

    def add_instructor(self,instructor):
        if instructor.instructor_id not in self.instructors:
            self.instructors[instructor.instructor_id]=instructor
          # self.instructors.append(instructor)
        else:
            print("Instructor already exist")

    def remove_instructor(self,instructor):
         if instructor.instructor_id == self.instructors:
             del self.instructors[instructor.instructor_id]
             #self.instructors.remove(instructor)
         else:
             print("Instructor doesn't exist")

    def add_student(self,student):
        if student.studnet_id not in self.students:
            self.students[student.studnet_id]
        else:
            print("Student already exist")

    def   remove_student(self,student):
        if student.studnet_id == self.students:
           del self.students[student.studnet_id]
        else:
            print("student doesn't exist")

    def print_instructors(self,instructors):
        for instructor in instructors :
            print(instructor)

    def print_students(self,students):
        for student in students:
            print(student)