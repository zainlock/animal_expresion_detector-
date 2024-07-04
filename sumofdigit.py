# num=int(input("Entre a number: "))
# sum=0
# while(num>0):
#     rem=num%10
#     sum=sum+rem
#     num=num//10
#     print("sum of your number is",rem," ",num," ",sum)

       #nested while loop
k=1
x=int(input("input the number of lines: "))

#using nested while loop
while k<=x:
    j=1
    while j<=k:
        print(j,end=" ")
        j=j+1
    print("\n")
    k=k+1
    
    