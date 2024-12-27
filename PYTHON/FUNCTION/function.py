# Creating a Function:                          # (def) - keyword
def python(parameters):                         # (python) - function name       
    #statement                                  # (statement) - body of statement
    return python                               # (return) - function return        
                                                        

# function calling:                             # Output: hello,world!
def python():
    print("hello,world!")
python()


# with argument with return:                    # Output: division :  12.5
def div(A , B):
    C = A/B
    return C
x = div(25,2)
print("division : ",x)


# with argument without return:                 # Output: difference :  23
def sub(A , B):
    C = A - B
    print("difference : ",C)
sub(25 , 2)


# without argument with return:                 # Output: multiplication :  275
def mul():
    A = int(input("enter A value : ")) #55
    B = int(input("enter B value : ")) # 5
    C = A * B
    return C
x = mul()
print("multiplication : ",x) 


# without argument without return:              # Output: total :  60
def add():
    A = int(input("enter A value : ")) #55
    B = int(input("enter B value :"))  # 5
    C = A + B
    print("total : ",C)
add()