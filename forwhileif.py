#three control flow statments in program
choice=eval(input("Enter your choice 1 or 2:"))
if choice==1:
    start=eval(input("Enter the starting number: "))
    end=eval(input("Enter the ending number: "))
    for x in range(start,end):
        print(x,end=" ")
elif choice==2:
    ans="y"
    value=eval(input("Enter a value :"))
    while(ans=="y"):
        print(value)
        value=value+1
        ans=input("to continue press y:")
else:
    print("invalid choice")

        