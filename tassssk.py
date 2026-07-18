
for i in range(1,11):
    if i!=5:
        print(i)





def print_uppercase(strings):
    for s in strings:
        print(s.upper())





list_integers=[1,2,3,4,5,6,7,8,9]
sum=0
for x in list_integers:
    if x%2==0:
        sum+=x
print(sum)





dictionary={'age':24,'name':'ruthwik'}
for k,v in dictionary.items():
    print(k,v)





a,b=0,1
for x in range(10):
    print(a)
    a,b=b,a+b





exam_scores=[80,85,90,95]
sum=0
for x in exam_scores:
    sum+=x
average=sum/len(exam_scores)
print(average,"is average")






for i in range(1,6):
    for j in range(1,6):
        print((i-1)*5+j,end=" ")
    print()
