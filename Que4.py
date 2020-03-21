FirstNames = ['Bipin','Bipin','Bipin','Harini','Harini','Ratna']

class FirstNameCheck:
    def __init__(self, FirstName, FirstNames):
        self.FirstName = FirstName
        self.FirstNames = FirstNames

    def CountCommonFN(self):
        temp=[]
        cnt=int()
        final=int()
        if self.FirstName not in temp:
            temp.append(self.FirstName)
            for obj in FirstNames:
                if self.FirstName == obj:
                    cnt += 1
            if( cnt > 1):
                final += cnt#print(cnt)
            cnt = 0
        return final
        

CheckList = []
CheckList.append(FirstNameCheck('Bipin',CheckList))
CheckList.append(FirstNameCheck('Harini',CheckList))
CheckList.append(FirstNameCheck('Ratna',CheckList))

output=int()
for obj in CheckList:
    output += obj.CountCommonFN()
    
print("No.of Students sharing First Names are: ", output)
