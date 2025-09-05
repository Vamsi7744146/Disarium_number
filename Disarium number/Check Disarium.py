#wapt check the given number is disari number or not
num=int(input())
a=len(str(num))
summ=0
dummy=num
while dummy>0:
    rem=dummy%10
    summ+=rem**a
    dummy//=10
    a-=1
if num==summ:
    print('it is disari number')
else:
    print('it is not disari number')  