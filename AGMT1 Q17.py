# Write a Python program to get a single string from two given strings, separated by a space and swap the first two characters of each string.
s1=input("enter the string:")
s2=input("enter the string:")
str1=list(s1)
str2=list(s2)
str1[0],str1[1]=str1[1],str1[0]
str2[0],str2[1]=str2[1],str2[0]
ns1="".join(str1)
ns2="".join(str2)



print( ns1," ",ns2)
