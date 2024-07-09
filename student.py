from datetime import date
import json
class Student:
    def __init__(self, fname, lname, grade, gender, height, address, interest):
        self.fname = fname
        self.lname = lname
        self.grade = grade
        self.gender = gender
        self.height = height
        self._address = address
        self.interest = interest
    def getPrivate(self):
        return f"First Name: {self.fname}\nLast Name: {self.lname}\nGrade: {self.grade}\nGender: {self.gender}\nHeight: {self.height}\nAddress: {self._address}\nCareer Interest: {self.interest}"
    
    def getPublic(self):
        return f"First Name: {self.fname}\nLast Name: {self.lname}\nGrade: {self.grade}\nCareer Interest: {self.interest}"
        
    
    def to_json(self):
        return json.dumps(self, default=lambda self: self.__dict__)



