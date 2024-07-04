# n=input("Enter a Sting: ")
# count=0
# for latters in n:
#     if(latters!=" "):
#         count=count+1

# print("total charecter is: ",count)

#deter mind that one string is in kangaroos

str1=input("Enter a string :")
str2=input("Enter a string :")
flag=True

#basic condition
# if len(str1)<len(str2):
#     print("Its wrong second string is bigger then first String")
# else:
#     val=0
#     for i in range(0,len(str2)):
#         for j in range(val,len(str1)):
#             if(str2[i]==str1[j]):
#                 val=j
#                 flag=True
#             else:
#                 flag=False
#         if(flag==False):
#                 break

# if flag==False:
#     print("it is not a kangaroo words")
# else:
#     print("it is  a kangaroo words")

#user demans
total=0
choi="yes"

while choi=="yes":
    opraation=input("Choice: a(ADD) or s(SUM):")
    amount=int(input("Enter the amount:"))
    opraation.lower()
    if opraation=="a":
        total=total+amount
    elif opraation=="s":
        total=total-amount
    else:
        pass
    choi=input("whish to continue yes/no:")
    
print("total amount is :",total)