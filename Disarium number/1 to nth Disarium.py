#write a program to print 6th to 10th armstrong number
num=1
count=0
while count<10:
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
        if count>=6:
            print(num)
    num+=1