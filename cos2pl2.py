#Write a Python script to perform various bitwise operations.

#bitvise and
a=int(input("enter fist number:"))
b=int(input("enter second number:"))
c= a and b
print(f"anser is and opretor is:",c)


#bitvise or
c=a or b
print(f"anser of OR opretor is:",c)


#bitvise xor
c=a ^ b
print(f"anser of XOR opretor is:",c)


#biswisee not
c = ~a
print(f"anser of  NOT opretor is:",c)

#bitwise leftshift
c=a << b 
print(f"ansr of  LEFTSHIFT opretor is:",c)

# birwise ringth hift
c= a >> b
print(f"anser of RITHSHIFT opretor is:",c)
