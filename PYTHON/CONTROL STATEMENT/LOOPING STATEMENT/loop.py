# Loops

# 1.while loop:                                             #Output: hello,world!!!
count = 1                                                   #        hello,world!!!
while(count <= 3):                                          #        hello,world!!!
    count = count + 1
    print("hello,world!!!")

 # else statement with while loop:                          #Output: python
count = 1                                                   #        python
while(count <= 3):                                          #        python
    count = count + 1                                       #        hello,world!!! 
    print("python")
else:
    print("hello,world!!!")


# 2.range(start, stop, step)                                #Output: [1, 3, 5, 7, 9]
values = list(range(1, 10, 2))
print(values)  


# 3.for loop:                                               #Output: 0
A = 4                                                       #        1
for i in range(0,A):                                        #        2
    print(i)                                                #        3


# 4.nested loop:                                            #Output: *
for i in range(5):                                          #        **
    for j in range(i):                                      #        ***
        print("*",end="")                                   #        ****
    print("")


# python loop control statement:
# 5.continue:                                               #Output: 1
for loop in range(1,6):                                     #        2
    if loop == 3:                                           #        4
        continue                                            #        5
    print(loop)

for letter in "python":                                     #Output: p
    if letter == "o" or letter == "n":                      #        y
        continue                                            #        t
    print(letter)                                           #        h


# 6.break:                                                  #Output: 1
for loop in range(1,6):                                     #        2
    if loop == 4:                                           #        3
        break                                                
    print(loop)


# 7.pass:                                                   #Output: n
for letter in "python":
    pass
print(letter)


# 8.delete:                                                 #Output: NameError: name 'A' is not defined
A = 5
print(A)
del A
print(A)