n1=int(input("enter 1 number:"))
n2=int(input("enter 2 number:"))
op=input("enter operator:")
if op=="+":
    print(n1+n2)
if op=="-":
    print(n1-n2)
if op=="*":
    print(n1*n2)
if op=="/":
    print(n1/n2)    
else:
    print("invalid operator")