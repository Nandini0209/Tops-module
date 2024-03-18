# How memory is managed in Python?

'''
Memory management in Python is primarily handled by Python's memory manager,
which is responsible for allocating and deallocating memory as needed to store objects and data structures.
Python's memory management is based on a combination of reference counting and garbage collection.

Reference Counting: Python uses reference counting as its primary mechanism for memory management.
Each object in Python contains a reference count, which keeps track of how many references point to that object.
When an object's reference count drops to zero, meaning there are no more references to it,
Python's memory manager deallocates the memory associated with that object.

Garbage Collection: In addition to reference counting, Python also employs a garbage collector to deal with more complex situations
such as circular references, where two or more objects reference each other and no external references exist.
Python's garbage collector periodically runs to identify and collect unreachable objects, freeing up the memory they occupy.

Python's memory management system allows developers to focus on writing code without worrying too much about memory allocation
and deallocation'''
