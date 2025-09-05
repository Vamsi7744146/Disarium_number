#write a program to print disari number in a given range
LL=int(input())
UP=int(input())
for num in range(LL,UP+1):
    a=len(str(num))
    summ=0
    dummy=num
    while dummy>0:
        rem=dummy%10
        summ+=rem**a
        dummy//=10
        a-=1
    if summ==num:
        print(num)