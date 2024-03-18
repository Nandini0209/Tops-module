#Write a Python program to add 'ing' at the end of a given string (length should be at least 3). If the given string already ends with 'ing' then add'ly' instead
#if the string length of the given string is less than 3, leave it unchanged.

s=input("enter the string:")
l=len(s)

if s.endswith("ing"):
    s1=s+"".join("ly")
    print(s1)
elif l>=3:
    s2=s+"".join("ing")
    print(s2)

elif l<3:
    print("the string is unchanged:",s)
