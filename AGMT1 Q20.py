# Write a Python function that takes a list of words and returns the length of the longest one.
l=[]
l1=[]
s1=input("enter the string:")
l.append(s1)
s2=input("enter the string:")
l.append(s2)
s3=input("enter the string:")
l.append(s3)
s4=input("enter the string:")
l.append(s4)
s5=input("enter the string:")
l.append(s5)
print("the list is:",l)
#largest=0
for i in l:
    s=len(i)
    l1.append(s)
print(l1)
print("the max length of the string in list is:",max(l1))

    
    
