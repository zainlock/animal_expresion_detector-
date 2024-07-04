# limit=eval(input("Enter a number of length to print prime number: "))
# for value in range(2,limit+1):
#     is_prime=True
#     for factor in range(2,value):
#         if (value%factor==0):
#             is_prime=False
#             break
#     if is_prime:
#             print(value,end=" ")
# print()

k=1
limit=int(input("enter largest limit to find  prime number:"))
while(k<limit):
    j=2
    while j<=(k/j):
        if not(k%j):
            break
        j=j+1
        if(j>k/j):
            print(k, end=" ")
    k=k+2

print()