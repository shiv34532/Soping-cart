
def add(x,y):
    return(x+y)
def subtract(x,y):
    return(x-y)
def  multiply(x,y):
    return(x*y)
def divide(x,y):
    if y==0:
        return "canntot divide by zero"
    else:
        return (x/y)
print("select youu wat to opretion choice:")
print("1.addition:")
print("2.subtrect:")
print("3.multiplycation:")
def nw():
    print("4.divide")
     
    choice=input("enter your choice in [1,2,3,4] :")
    return choice
chiice=nw()
num1=float(input("enter fist number:"))
num2=float("enter second number:")

if chiice=="1":
    print("result:",add(num1 ,num2))
elif chiice=="2":
    print("result:",subtract(num1,num2))
elif chiice=="3":
    print("result:",multiply(num1,num2))
elif chiice=="4":
    print("result:",divide(num1,num2))
else:
    print("invalid input:")
