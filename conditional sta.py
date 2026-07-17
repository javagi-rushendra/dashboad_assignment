salary=int(input("enter amount"))
if salary>0:

    if salary<=250000:
        print("no tax")
    elif salary<=500000:
        salary=salary-250000
        salary=(salary*5)/100
        print("salary taxes:",salary)
    elif salary<=1000000:
        salary=salary-250000
        salary=(salary*7)/100
        print("salary taxes:",salary)
    elif salary>1000000:
        salary=salary-250000
        salary=(salary*10)/100
        print("salary taxes:",salary)
else:
    print("enter valid amount")
