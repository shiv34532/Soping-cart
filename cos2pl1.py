#Write a Python script to find a maximum of given three numbers (Use ternary operator).
f=int(input("enter fist number:"))
s=int(input("enter second number"))
t=int(input("enter therd number:"))
m=f if f>t and f>s else s if s>t else t
print("maximum  numbr is:",m)