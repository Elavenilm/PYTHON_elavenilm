# User-defined functions:                           #Output:  hello,world!!! 

def function():
    print("hello,world!!!")
function()
 

# parameterized():                                  #Output: even
def fun(A):
    if(A % 2 == 0):
        print("even")
    else:
        print("odd")
fun(2)


# default arguments:                                #Output: A :  10
def fun(A,B = 20):                                  #        B :  20
    print("A : ",A)
    print("B : ",B)
fun(10) 


# keyword arguments:                                #Output: arun kumar
def student(firstname,lastname):
    print(firstname,lastname)
student(firstname="arun",lastname="kumar")


# pass by reference or pass by value:               #Output: value :  30 id :  140704479119176
def fun(x):
    print("value : ",x ,"id : ",id(x))
x=30
fun(x) 


# function with return value:                       #Output: 5
def fun(x , y):                                     #        True
    return x + y
def is_true(x):
    return bool(x)
result=fun(2,3)
print(result)
result=is_true(2<5)
print(result) 