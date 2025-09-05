#write a program to print first 10 disari number
num=1
target=10
count=0
while count<target:
    summ=0
    dummy=num
    a=len(str(num))
    while dummy>0:
        rem=dummy%10
        summ+=rem**a
        dummy//=10
        a-=1

    if summ==num:
        print(num)
        count+=1
    num+=1