#write a program to print 10th disarium number
num=1
target=18
count=0
while count<target:
    summ=0
    a=len(str(num))
    dummy=num
    while dummy>0:
        rem=dummy%10
        summ+=rem**a
        dummy//=10
        a-=1
    if num==summ:
        count+=1
        if count==target:
            print(num)
    num+=1