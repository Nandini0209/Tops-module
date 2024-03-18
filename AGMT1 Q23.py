#Write a Python function to insert a string in the middle of a string.  
def insert_string_in_middle(orig_string, insert_string):

 mid = len(orig_string) // 2

 return orig_string[:mid] + insert_string + orig_string[mid:]

orig_string=input("enter the string:")
insert_string=input("enter the middle string:")
print(insert_string_in_middle(orig_string,insert_string))
