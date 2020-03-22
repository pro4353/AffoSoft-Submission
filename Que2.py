class College:
        Student1 = {'Name':'Pranay','Stream':'BTech','Year':'1','Sec':'101','Attendance':'A'}
        Student2 = {'Name':'Minal','Stream':'MBA','Year':'1','Sec':'101','Attendance':'A'}
        Student3 = {'Name':'Shinam','Stream':'BTech','Year':'1','Sec':'101','Attendance':'P'}
        Student4 = {'Name':'shanay','Stream':'MBA','Year':'1','Sec':'101','Attendance':'P'}
        Students =[Student1,Student2,Student3,Student4]

        def Student_Register(self):
            return self.Students
            
class BTech:
    BTech_Register=[]
    bt = College()
    Reg_Meth = bt.Student_Register()
    
    for x in Reg_Meth:
        if x['Stream'] == 'BTech':
            BTech_Register.append(x)
            
    def BTech_Student_Register(self):
        return self.BTech_Register

class MBA:
    MBA_Register=[]
    mb = College()
    Reg_Meth = mb.Student_Register()
    
    for x in Reg_Meth:
        if x['Stream'] == 'MBA':
            MBA_Register.append(x)
            
    def MBA_Student_Register(self):
        return self.MBA_Register


class BTech_Year1:
    temp =[]
    BTech_Year1_Register=[]
    bt_y1 = BTech()
    Bt_Y1_Meth = bt_y1.BTech_Student_Register()
    
    for x in Bt_Y1_Meth:
        if x['Year'] == '1':
            temp.append(x['Name'])
            temp.append(x['Sec'])
            temp.append(x['Attendance'])
            BTech_Year1_Register.append(temp)
            temp = []
            
    def BTech_Student_Year1_Register(self):
        return self.BTech_Year1_Register

class MBA_Year1:
    temp =[]
    MBA_Year1_Register=[]
    mb_y1 = MBA()
    mb_Y1_Meth = mb_y1.MBA_Student_Register()
    
    for x in mb_Y1_Meth:
        if x['Year'] == '1':
            temp.append(x['Name'])
            temp.append(x['Sec'])
            temp.append(x['Attendance'])
            MBA_Year1_Register.append(temp)
            temp = []
            
    def MBA_Student_Year1_Register(self):
        return self.MBA_Year1_Register

class BTech_Year1_Sec101:
    temp = []
    BTech_Year1_Sec101_Register=[]
    bt_y1_101 = BTech_Year1()
    BTech_Year1_Sec101_Meth = bt_y1_101.BTech_Student_Year1_Register()
    
    for y in range(len(BTech_Year1_Sec101_Meth)):
        if BTech_Year1_Sec101_Meth[y][1] == '101':
                temp.append(BTech_Year1_Sec101_Meth[y][0])
                temp.append(BTech_Year1_Sec101_Meth[y][2])
                BTech_Year1_Sec101_Register.append(temp)
                temp = []

    def Absent_Students(self):
        Section_Attendance = self.BTech_Year1_Sec101_Register
        print("Absent Students of BTech 1st year 101 are :")
        for y in range(len(Section_Attendance)):
                if Section_Attendance[y][1] == 'A':
                    print(Section_Attendance[y][0])

class MBA_Year1_Sec101:
    temp = []
    MBA_Year1_Sec101_Register=[]
    mb_y1_101 = MBA_Year1()
    MBA_Year1_Sec101_Meth = mb_y1_101.MBA_Student_Year1_Register()
    
    for y in range(len(MBA_Year1_Sec101_Meth)):
        if MBA_Year1_Sec101_Meth[y][1] == '101':
                temp.append(MBA_Year1_Sec101_Meth[y][0])
                temp.append(MBA_Year1_Sec101_Meth[y][2])
                MBA_Year1_Sec101_Register.append(temp)
                temp = []

    #Polymorphism with same function name as in BTech_Year1_Sec101
    def Absent_Students(self):
        Section_Attendance = self.MBA_Year1_Sec101_Register
        print("\nAbsent Students of MBA 1st year 101 are :")
        for y in range(len(Section_Attendance)):
                if Section_Attendance[y][1] == 'A':
                    print(Section_Attendance[y][0])

#Calling Absent_Students in BTech_Year1_Sec101, MBA_Year1_Sec101 classes using Student_Register object, in College Class                

sp = BTech_Year1_Sec101()
op = sp.Absent_Students()

sp = MBA_Year1_Sec101()
op = sp.Absent_Students()

    
    
            
    

    
