# for num in range(11,20):
#     print(num)
#     if(num>15):
#         break

#break in while loop
total=0
print("Enter positive numbers to add,enter negetive number to end:")
while True:
    amount=eval(input("ENter a amount: "))
    if amount<0:
        break
    total+=amount

print("total amount is: ",total)