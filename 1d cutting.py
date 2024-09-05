#main s
import pandas as pd
size=[]
print("Enter standard length : ")
std=int(input())
print("Enter number of cut sizes : ")
n=int(input())
print("Enter lengths :")
#size array with all cut sizes
for i in range(n):
    size.append(int(input()))
#making size decrescresing order
size.sort(reverse=True)
#initialization of combination array 
tu=[0]*n
comb=[]

#pattern function
def f(std,s,num):
    if(s==min(size)):
        temp=int(std/s)
        tu[num]=temp
        comb.append(list(tu))
    else:
        temp=int(std/s)
        while(temp>=0):
            tu[num]=temp
            r=std-temp*size[num]
            f(r,size[num+1],num+1) 
            temp=temp-1
#calling pattern function
f(std,size[0],0)

print(comb)

#just for exporting to text file
for i in range(len(comb)):
    for j in range(n-1):
        print(comb[i][j],end="\t")
    print(comb[i][j+1])

df = pd.DataFrame(comb, columns =[i for i in size]) 
print(df)