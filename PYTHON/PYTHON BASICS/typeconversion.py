#---TYPE CONVERSION---


#integer to float
x_int=10
y_float=float(x_int)
print("integer to float:",y_float)

#float to integer
a_float=3.5
b_int=int(a_float)
print("float to integer:",b_int)

#integer to string
x_int=5
c_str=str(x_int)
print("integer to string:",c_str)

#float to string
a_float=5.3
d_str=str(a_float)
print("float to string:",d_str)

#string to integer
e_str="20"
f_int=int(e_str)
print("string to integer:",f_int)

#string to float
g_str="3.15"
h_float=float(g_str)
print("string to float:",h_float)

#boolean to integer
i_bool=True
j_int=int(i_bool)
print("boolean to integer:",j_int)

#integer to boolean
k_int=0
l_bool=bool(k_int)
print("integer to boolean:",l_bool)

#string to boolean
m_str="True"
n_bool=bool(m_str)
print("string to boolean:",n_bool)

#list to tuple
o_list=[1,2,3]
p_tuple=tuple(o_list)
print("list to tuple:",p_tuple)

#tuple to list
q_tuple=(4,5,6)
r_list=list(q_tuple)
print("tuple to list:",r_list)