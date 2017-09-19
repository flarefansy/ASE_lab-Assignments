# -*- coding: utf-8 -*-
"""
Created on Sat Sep 16 04:04:18 2017

@author: Spencersun
"""
num = 0
class StudentEnrollmentSystem:
    num = 0
    def __init__(self, name, system, grades):
        self.name = name
        self.system = system
        self.grades = grades
        StudentEnrollmentSystem.num += 1
        self.__totalnumber = num
#        StudentEnrollmentSystem.__totalnumber += 1
        
class Student(StudentEnrollmentSystem):
    def __inif__(self):
        super().__init__()
#        StudentEnrollmentSystem.__inif__(self)
    def get_student(self):
        return self.name
        
class System(StudentEnrollmentSystem):
    def __inif__(self):
        super().__init__()
#        StudentEnrollmentSystem.__inif__(self)
    def get_system(self):
        return self.system
        
class Grades(StudentEnrollmentSystem):
    def __inif__(self):
        super().__init__()
#        StudentEnrollmentSystem.__inif__(self)
    def get_grades(self):
        return self.grades

class studentInfo(Student, System, Grades):
    def __inif__(self):
        super().__init__()
#        Student.__inif__(self)
#        System.__inif__(self)
#        Grades.__inif__(self)
    def get_studentinfo(self):
        return self.grades, self.system, self.name

if __name__== "__main__":
    a = StudentEnrollmentSystem("John",1,7)
    c = Student.get_student(a)
    b = System.get_system(a)
    e = Grades.get_grades(a)
    f = studentInfo.get_studentinfo(a)
    aa = StudentEnrollmentSystem("Smith",2,4)
    print (c, b, e)
    print (f)
    print (StudentEnrollmentSystem.num)
    z = StudentEnrollmentSystem.__totalnumber
