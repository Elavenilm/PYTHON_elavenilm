from tabulate import tabulate
import mysql.connector

cont=mysql.connector.connect(host="localhost",user="root",password="elavenil",database="education")

def insert(name,age,grade,roll_no):
    res=cont.cursor()
    sql="insert into student(name,age,grade,roll_no)values(%s,%s,%s,%s)"
    users=(name,age,grade,roll_no)
    res.execute(sql,users)
    cont.commit()
    print("data insert success")

def update(name,age,grade,roll_no):
    res=cont.cursor()
    sql="update student set name=%s,age=%s,grade=%s where roll_no=%s"
    users=(name,age,grade,roll_no)
    res.execute(sql,users)
    cont.commit()
    print("data update success")

def select():
    res=cont.cursor()
    sql="select name,age,grade,roll_no from student"
    res.execute(sql)
    result=res.fetchall()
    print(tabulate(result,headers=["NAME","AGE","GRADE","ROLL_NO"]))

while True:
    print("1.INSERT DATA")
    print("2.UPDATE DATA")
    print("3.SELECT DATA")
    print("4.EXIT")
    choice=int(input("Enter Your Choice:"))

    if choice==1:
        name=input("Enter Name:")
        age=int(input("Enter Age:"))
        grade=input("Enter Grade:")
        roll_no=int(input("Enter Roll No:"))
        insert(name,age,grade,roll_no)

    elif choice==2:
        roll_no=int(input("Enter Roll No:"))
        name=input("Enter Name:")
        age=int(input("Enter Age:"))
        grade=input("Enter Grade:")
        update(name,age,grade,roll_no)

    elif choice==3:
        select()

    elif choice==4:
        quit()

    else:
        print("Invalid Selection Please Try Again!!!")

