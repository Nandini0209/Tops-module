# Write a Python program that will return true if the two given integer values are equal or their sum or difference is 5.
a=int(input("enter number:"))
b=int(input("enter number:"))

if a==5 and b==5:
    print("true")
elif a+b==5:
    print("true")
elif a-b==5:
    print("true")
else:
    print("false")
