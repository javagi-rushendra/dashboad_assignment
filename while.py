# 01. Print all numbers from 1 to 100 using a while loop
a=1
while a<=100:
    print(a)
    a=a+1
# 02. Simulate a fan regulator by printing the numbers from 1 to 5 and then back to 1 using a while loop
# import time
# start = 1
# while start <= 5:
#     print("fan speed=",start)
#     time.sleep(1)  # Wait for 1 second
#     start += 1
# print()
# print("------------------------")
# while start > 1:
#     start -= 1
#     print("fan speed=",start)
#     time.sleep(1)  # Wait for 1 second
#03. Print all even numbers from 1 to 100 using a while loop
b=1
while b<=100:
    if b%2==0:
        print(b)
    b=b+1
# 04. Print all odd numbers from 1 to 100 using a while loop
c=1
while c<=100:
    if c%2==1:
        print(c)
    c=c+1
# 05. Write a program to find the sum of numbers from 1 to n (where n is a user-inputted number) using a while loop
n=int(input("enter a number: "))
e=1
sum=0
while e<=n:
    sum=sum+e
    e=e+1
print(sum)
   

# 06. Calculate the factorial of a given number using a while loop
r=5
fact=1
while r>=1:
    fact=fact*r
    r=r-1
print(fact)


# 07. Reverse a given number using a while loop
h=321
reverse=0
while h>0:
    digit=h%10
    h=h//10
    reverse = reverse *10+ digit
print(reverse)


# 08. Check whether a given number is a palindrome or not using a while loop
h=321
temp=h
reverse=0
while h>0:
    digit=h%10
    h=h//10
    reverse = reverse *10+ digit
if temp==reverse:
    print("palindrome")
else:
    print("not palindrome")
# 09. Count the number of digits in a given number using a while loop
n=12345678
count=0
while n>0:
    digit=n%10
    n=n//10
    count=count+1
print("no.of digits: ",count)
# 10. Find the sum of the digits of a given number in Python using a while loop
n=12345678
sum=0
while n>0:
    digit=n%10
    n=n//10
    sum=sum+digit
print("sumof digits: ", sum)