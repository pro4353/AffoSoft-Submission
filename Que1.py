print("Enter Name : ")

ip = str(input())
mres = ""
for x in range(0,len(ip)):
    for y in range(0,x+1):
        mres += ip[y]
    print(mres.rjust(len(ip)))
    mres = ""
