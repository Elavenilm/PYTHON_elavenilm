import array as arr

# Creating array of integers and accessing array:                   #Output: 1
a=arr.array('i',[1,2,3])                                            #        3
print(a[0])
print(a[2])


# Adding elements to array using append():                          #Output: array('i', [1, 2, 3, 4])
import array as arr
a=arr.array('i',[1,2,3])
a.append(4)
print(a)


# Iterating and printing each item:                                 #Output: 123
import array as arr                                
a=arr.array('i',[1,2,3])
for i in range(0,3):
    print(a[i],end="")


# Removing elements to array:                                       
#using remove()                                                     #Output: array('i', [1, 2, 1, 4, 5])
import array
arr=array.array('i',[1,2,3,1,4,5])
arr.remove(3)
print(arr)

#using pop()                                                        #Output: array('i', [1, 2, 4, 5])
arr.pop(2)
print(arr)


# Slicing of an array:                                              #Output: array('i', [4, 5, 6, 7, 8])
import array as arr                                                 #        array('i', [6, 7, 8, 9, 10])
a=[1,2,3,4,5,6,7,8,9,10]                                            #        array('i', [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
b=arr.array('i',a)

sliced_array=b[3:8]
print(sliced_array)

sliced_array=b[5:]
print(sliced_array)

sliced_array=b[:]
print(sliced_array)


# Searching elements in an array:                                   #Output: 1
import array                                                        #        0
arr=array.array('i',[1,2,3,4,5,1,2])
print(arr.index(2))
print(arr.index(1))    


# Updating elements in an array:                                    #Output: array('i', [1, 2, 3, 4, 2, 5])
import array
arr=array.array('i',[1,2,3,1,2,5])
arr[3]=4
print(arr)


# Extend elements in an array:                                      #Output: array('i', [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
import array as arr
a=arr.array('i',[1,2,3,4,5])
a.extend([6,7,8,9,10])
print(a)


# Counting elements in an array:                                    #Output: 4
import array
arr=array.array('i',[3,1,2,3,4,3,5,3])
count=arr.count(3)
print(count)


# Reversing elements in an array:                                   #Output: 5 4 3 2 1
import array
arr=array.array('i',[1,2,3,4,5])
arr.reverse()
print(*arr)