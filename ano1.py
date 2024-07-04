choise=int(input("Enter 1 for odd Enter 2 for even numbers print:"))
ra=int(input("ENter the length:"))
if choise==1:
    
    print("odd number is the range is :")
    for i in range(1,ra+1,2):
        print(i)
else:
    print("Even number in range is :")
    for i in range(2,ra+1,2):
        print(i)