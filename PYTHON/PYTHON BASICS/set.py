#---SET{}---


set1 = {1, 2, 3}
set2 = {3, 4, 5}

# Union:
print(set1 | set2)                       # Output: {1, 2, 3, 4, 5}

# Intersection:
print(set1 & set2)                       # Output: {3}

# Difference:
print(set1 - set2)                       # Output: {1, 2}

# Symmetric Difference:
print(set1 ^ set2)                       # Output: {1, 2, 4, 5}

# Access set{} values using loop:
names={'aaa','bbb','ccc','ddd'}
for name in names:
    print(name)

# Adding new element:                    # Output: {'ccc', 'ddd', 'aaa', 'zzz', 'bbb'}
names={'aaa','bbb','ccc','ddd'}
names.add('zzz')
print(names)

# Update another set of data:            # Output: {'html', 'c', 'css', 'java', 'python', 'c++'}
a={'python','java','c++'}
b={'c','html','css'}
a.update(b)
print(a)

# Remove data in set:                    # Output: {'java', 'python'}
a={'python','java','c++'}
a.remove('c++')
print(a)

# Using discard : #to remove doubtful datas              
a={'python','java','c++','c'}              
a.discard('c')                           # Output: {'python', 'java', 'c++'}
print(a)

# Pop set{}:                             # Output: {'java', 'c++', 'c'}
a={'python','java','c++','c'} 
a.pop()
print(a)

# Clear set{}:                           # Output: set()
a={'python','java','c++','c'} 
a.clear()
print(a)

# Delete set{}:                          # Output: NameError: name 'a' is not defined
a={'python','java','c++','c'} 
del a
print(a)

# isdisjoint():                          # Output: False
a={1,2,3,4,5}
b={5,6,7,8,9}
c=a.isdisjoint(b)
print(c)

# issubset():                            # Output: False           
a={1,2,3,4,5}
b={5,6,7,8,9}
c=a.issubset(b)
print(c)

a={5,6,7}                                # Output: True
b={5,6,7,8,9}
c=a.issubset(b)
print(c)

# issuperset():                          # Output: False
a={5,6,7}                             
b={5,6,7,8,9}
c=a.issuperset(b)
print(c)
 
# issuperset():                          # Output: True
a={5,6,7}                             
b={5,6,7}
c=a.issuperset(b)
print(c)