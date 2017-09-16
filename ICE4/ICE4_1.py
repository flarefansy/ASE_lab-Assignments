# -*- coding: utf-8 -*-
"""
Created on Fri Sep 15 16:32:27 2017

@author: Spencersun
"""



class student:
    count = 0
#    def DataMember(self):
        #number_student = len(data)
#        return number_student
    def __init__(self,name,rollno,grades):
        self.name = name
        self.rollno = rollno
        self.grades = grades
        student.count+=1
    def get_info(self):
        return self.name,self.rollno,self.grades
    
class TransferStudent (student):
    def __init__(self,name,rollno,grades):
        student.__init__(self,name,rollno,grades)
#    def __repr__(self):
#        return "The student is " + self.name + ", rollno is %d, grades is %d." % (self.rollno, self.grades)
        
if __name__== "__main__":
    
    f = student("john",23,90)
    print (f.count)
    g = student("john",23,90)
    print (f.get_info())
    s = TransferStudent("john",23,90)
    
    print (student.count)
    
     