# 1.if statement:                                               #Output: 10 is less than 15
A = 10
if(A < 15):
    print("10 is less than 15")


# 2.if else statement:                                          #Output: A is positive
A = 10
if(A > 0):
    print("A is positive")
else:
    print("A is 0 or negative")

 # using ('AND' '&') with if else:                           
B = int(input("enter the value:"))
if B >=1 and B <=10:
    print("positive")
else:
    print("negative")


# 3.nested if else statement:                                   #Output: C is smaller than 20
C = 10                                                          #        C is smaller than 15
if(C == 10):
    if(C < 20):
        print("C is smaller than 20")
    if(C < 15):
        print("C is smaller than 15")
    else:
        print("C is greater than 20")
else:
    print("C is not equal to 10")


# 4.if elif else statement:                                     #Output: D is not present
D = 30
if(D == 10):
    print("D is 10")
elif(D == 20):
    print("D is 20")
elif(D == 25):
    print("D is 25")
else:
    print("D is not present")