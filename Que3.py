from collections import Counter

re=[]
res =[]
    
with open('Text_Que2.txt','r') as file:
    for line in file:
        for word in line.split():
            re.append(word)
            
        
op =Counter(re)
res=list(op)
print("Count of Unique Words : ",len(res))
