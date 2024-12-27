#---LIST[]---


#CREATING A LIST:                                     # output:[1, 2, 3, 4, 5]
my_list = [1, 2, 3, 4, 5]          
print(my_list)

# 1.Appending Elements:                                # output: append: [1, 2, 3, 'ram']
my_list=[1,2,3]
my_list.append("ram")
print("append:",my_list)

# 2.extend():                                          # output: extend: [1, 2, 3, 4, 5, 6]
my_list=[1,2,3]
my_list.extend([4,5,6])
print("extend:",my_list)

# 3.Inserting Elements:                                # output: insert: [1, 2, 3, 4]
my_list=[1,2,3]
my_list.insert(3,4)
print("insert:",my_list)

# 4.Removing Elements:                                 # output: remove: [1, 3, 2]
my_list=[1,2,3,2]
my_list.remove(2)
print("remove:",my_list)

# 5.Popping Elements:                                  # output: pop: [2, 3]
my_list=[1,2,3]
new_list=my_list.pop(0)
print("pop:",my_list)

# 6.index list():                                      # output: index: 2
my_list=[1,2,3,2]
index=my_list.index(3)
print("index:",index)

# 7.counting a list:                                   # output: count: 4
my_list=[1,2,3,2,3,3,3]
count=my_list.count(3)
print("count:",count)

# 8.Sorting a List:                                    # output: sort: [1, 2, 3]
my_list=[3,1,2]
my_list.sort()
print("sort:",my_list)

# 9.Reversing a List:                                  # output: reverse: [5, 4, 3, 2, 1]
my_list=[1,2,3,4,5]
my_list.reverse()
print("reverse:",my_list)

# 10.Copying a List:                                   # output: copy: [1, 2, 3]
my_list=[1,2,3]
new_list=my_list.copy()
print("copy:",new_list)

# 11.Slicing Lists:                                    # output: sliced: [2, 3, 4]
my_list=[1,2,3,4,5]
sliced_list=my_list[1:4]
print("sliced:",sliced_list)

# 12.Clearing a List:                                  # output: clear: []
my_list=[6,7,8,9,10]
my_list.clear()
print("clear:",my_list)

# 13. Accessing Elements:                              # output: 1
my_list=[1,2,3,4,5]
print(my_list[0])

# 14. Length of List:                                  # output: length: 3
my_list=[6,7,8]
length = len(my_list)
print("length:",length)
 
# 15. List Comprehension:                              # output: list comprehension: [4, 16, 36, 64]
my_list=[2,4,6,8]
squared_list = [x**2 for x in my_list]
print("list comprehension:",squared_list)

# 16. Iterating Over a List:                           # output: 4,5,6 - one by one
my_list=[4,5,6]                                                
for item in my_list:                                           
    print(item)

# 17. Checking if an Item Exists:                      # output: 5 exists in the list
my_list=[1,2,3,4,5,6,7,8,9,10]
if 5 in my_list:
    print("5 exists in the list")

# 18.multilevel list:
multilevel_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

print(multilevel_list[2])              # Output: [7, 8, 9]
print(multilevel_list[2][1])           # Output: 8
del multilevel_list[1]                 # output:[[1, 2, 3], [7, 8, 9]]
print(multilevel_list)