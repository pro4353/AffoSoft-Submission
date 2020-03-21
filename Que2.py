from collections import defaultdict
from abc import abstractmethod
class College():
    def Absentee_Students(self,Attendance):
        Absentees=[]
        for x in Attendance:
            if Attendance[x] == 'A':
                Absentees.append(x)
        return Absentees
    
Attendance = {'Pranay':'P','Hemanth':'A','Ben':'P','Larissa':'A','Christina':'A','Waleed':'A'}
class sec1_Year1_BTech(College):
    def Register():
        Student_Register=["Pranay","Hemanth"]
        return Student_Register

res = sec1_Year1_BTech()
result = res.Absentee_Students(Attendance)
print("Students, absent for today are: ")
for x in result:
    print(x)

class BTech(College):
    @abstractmethod
    def Register():
        pass
   
class MBA(College):
    @abstractmethod
    def Register():
        pass

class Year1_BTech(BTech):
    @abstractmethod
    def Attendance():
        pass
    
class Year1_MBA(MBA):

    @abstractmethod
    def Attendance():
        pass
    


