#let's do some example with for and if staments
num=int(input("ENter a number of items: "))
amount=0
discont=0

#using for loop
for k in range(1,num+1):
    price=eval(input("ENter price: "))
    quntity=eval(input("Enter the quntity: "))
    amount=amount+(price*quntity)
print("total amoutn is: ",amount)

#using if statments
if(amount>5000):
    discont=amount*0.1
    print("discount 10% =",discont)
elif(amount>3000):
    discont=amount*0.07
    print("discoutn 7% =",discont)
elif(amount>1000):
    discont=amount*0.05
    print("Discoutn is 5% =",discont)
else:
    print("no discout ")

print("Net amoutn is ",amount-discont)
