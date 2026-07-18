import time
for i in range(10, 0, -1):
    print(i)
    time.sleep(1)
print("BOOM!")







n=int(input("enter number"))
for i in range(1, n):
    if i % 7 == 0:
        print(i)








scores=[50,65,70]
total=0
for i in scores:
    total=total+i
print("Total score:", total)











n=int(input("enter value:"))
for i in range(1,11):
    print(f'{n}*{i}',"=",n*i)







count=0
char=input("enter string:")
for x in char:
    if x in "aeiouAEIOU":
        count+=1
print(count)








balance=1000
amounts=[100,200,150]
for i in amounts:
    balance=balance-i
print(balance)








max2=0
marks=[45,78,89,66]
for i in marks:
    print(i)
    if i>max2:
        max2=i
print("max2 =",max2)







for i in range(1,51):
    if i==25:
        print("match found")
    else:
        print("match not found")





count=0
for i in range(2,11,2):
    count=count+1
print(count)





n="python"
s=""
for x in n:
    s=x+s
print(s)



sum=0
for x in (100,250,75):
    sum=sum+x
print(sum)




import time
for i in range(20,0,-1):
    time.sleep(1)
    print(i)
print("launch successful")


 





char="PyThOnPrOgRaM"
count=0
for i in char:
    if i.isupper():
        count=count+1
print(count)









n="programming"
count=0
for i in n:
    print(i)
    count=count+1
print("Number of characters in the string:", count)





string="madam"
sum=""
for char in string:
    sum=char+sum
if sum==string:
    print("palindrome")






list1=[10, 45, 23, 89, 67,]
y=0
for x in list1:
    if x>y:
        y=x
s=0
for i in list1:
    if i>s and i<y:
        s=i
print(s,"is second largest number")






year=5
principal=1000
rate=0.05
for i in range(1, year + 1):
    interest = principal * rate * i
    print(f"Year {i}: Interest = {interest}")








sum=0
for x in range(1,50):
    if x%2==1:
        sum=sum+x
print(sum)








temp=0
prices=[500,1000,1500]
for x in prices:
    print("original price:",x)
    temp=x*(10/100)
    print("discount price:",x-temp)






sum=0
n=int(input("enter number"))
for x in range(1,n):
    if n%x==0:
        sum=sum+x
if sum==n:
    print("perfect number")
else:
    print("not a perfect number")







n=int(input("enter number"))
x=len(str(n))
automorphic=(n*n)%(10**x)
if automorphic==n:
    print("automorphic number")
else:
    print("not automorphic number")








a,b=0,1
for x in range(9):
    print(a)
    a,b=b,a+b










n=18
sum=0
for i in str(n):
    print(i)
    sum=sum+int(i)
if n%sum==0:
    print("harshad number")
else:
    print("not a harshad number")










