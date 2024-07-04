total=0
comp=False
while not comp:
        amount=eval(input("Enter the number (press 0 to quite):"))
        if(amount<0):
                print("Opps,you enter negtive value")
                continue
        #skip rest of body for this itration
        if(amount==0) :
                comp=True
        else:
                total+=amount
print("the total number is=",total)