n=int(input("enter a aplindrumnumber:"))
sum=0
b=n
while(n>0):
    z=n%10
    sum=z*10
    n=n//10
if(sum==b):
    print("paindrom")
else:
    print("not palindom")