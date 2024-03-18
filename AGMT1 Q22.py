# Write a Python program to get a string made of the first 2 and the last 2 chars from a given a string. If the string length is less than 2, return instead of the empty string

#s="tops technologies"
s=input("enter the string:")
s1=len(s)
if s1>2:
 s2=s[0:2]+s[-2:]
 print(s2)
else:
    print("none change")
