choice=int(input("Enter a numbar between 1-7:"))
try:
    if choice<1 or choice>7:
        raise ValueError()
    if (choice==1):
        weekday="monday"
    elif (choice==2):
        weekday="tusday"
    elif (choice==3):
        weekday="wednesday"
    elif (choice==4):
        weekday="thursday"
    elif (choice==5):
        weekday="friday"
    elif (choice==6):
        weekday="seturday"
    else:
        weekday="sunday"
    print("the day is:",weekday)
except ValueError:
    print("wrong!!!Check week day")