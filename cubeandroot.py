#program to print even number's squre and odd number's cube
evenlist=[]
oddlist=[]
#even=dict()
#odd=dict()
i=int(input("Enter the number of length: "))
for n in range(1,i+1,1):
    if(n%2==0):
        evenlist.append(n*n)
        #even=n*n
        #print(even)
    else:
        oddlist.append(n*n*n)
        #odd=n*n*n
        #print(odd)
print(evenlist)
print(oddlist)