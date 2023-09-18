#STUDENT APPLICATION 
#import | class | add,remove,save,load  |  main  |test
import json
from os import name
import os.path
import math

class Directory:
    student = {}
    def __init__(self):
        pass

#Dictionary consists of key-value pair
    def add(self,key,qty):
        q=0                                                      #shortform for qty
        if key in self.student:
            v=self.student[key]
            q = v + qty
        else:
            q=qty
        self.student[key]=q    
        print(f"Added {qty} {key} : total= {self.student[key]}")

    def remove(self,key,qty):
        q=0                                                             
        if key in self.student:
            v=self.student[key]
            q = v-qty
        if q<0:
            q=0
        self.student[key]=q    
        print(f"Removed {qty} {key} : total= {self.student[key]}")

    def display(self):
        for key,value in self.student.items():
            print(f"{key} = {value}")

    def save(self):
        print("Saving inventory")
        with open('invent.txt','w') as f:
            json.dump(self.student,f)
        print("Saved")

    def load(self):
        print("Loading inventory")
        if not os.path.exists('invent.txt'):
            print("Skipping, Nothing to load")
            return 
        with open('invent.txt','r') as f:
            self.student =  json.load(f)
        print("Loaded")


dir = Directory()
while True:    
    act=input("Actions: ADD , REMOVE , LIST , SAVE , EXIT : ")
    if act == "EXIT":
        break
    if act == "ADD" or act=="REMOVE":
        key = input("Enter the student: ")
        qty = input("Enter the qty:")
        if act=="ADD":
            dir.add(key,qty)
        if act=="REMOVE":
            dir.remove(key,qty)    
    if act == "LIST":
        dir.display()
    if act == "SAVE":
        dir.save()   
    
dir.save()

