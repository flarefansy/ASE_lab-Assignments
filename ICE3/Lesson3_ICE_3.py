# -*- coding: utf-8 -*-
"""
Created on Fri Sep  8 16:30:34 2017

@author: Spencersun
"""

input_dic1 = {'course':"python", 'currentGPA':80, 'LastGPA':90}
input_dic2 = {'course':"python", 'currentGPA':95, 'LastGPA':85}
input_dic3 = {'course':"python", 'currentGPA':100, 'LastGPA':100}
List = [input_dic1, input_dic2, input_dic3]
for i in range(len(List)):
    average = int((List[i]['currentGPA'] + List[i]['LastGPA'])/2)
    List[i].pop('currentGPA')
    List[i].pop('LastGPA')
    List[i].update({'LastGPA+CurrentGPA':average})
print (List)
    
