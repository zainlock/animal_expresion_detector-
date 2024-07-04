num=int(input("Enter a number:"))
try:
    if(num<0):
        raise ValueError
    fact=0
    for i in range (0,num+1):
        multi=i*i
        fact=multi+fact
    print(fact)
except ValueError:
    print("this value is not acceptable")