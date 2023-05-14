#Prashant sir

'''
Before starting exception handling we should know about types of
error
1. Syntax error
2. Runtime error
Syntax error comes when we do not follow proper syntactical rule
means predefine grammatical rules of python language
Runtime error comes due to incorrect logic or wrong input given by
end user and run time error also known as exception



What is exception

As we know that when we execute any program we can say that a
normal flow of execution Has done so when due to any incorrect
logic or a unexpected wrong input given by from user side which
disturb a normal flow of execution so this is called exception.

Exception handling means suppose if any runtime error generate in
any part of the code so except that part rest of the code should be
executed and error part will be handled by exception handling code
so our normal flow of execution will be continue.


*****Types of exception********

Predefine exception

The exception which comes automatically by python virtual machine
whenever any abnormal condition occur ,that are called predefine
built in function
E.g) ZeroDivisionError, ValueError

User defined exception

Some time programmer want to indicates that something goes wrong
And declare explicitly by raise keyword that are called as user defined
exception or also we can say customize exception

'''
 #whene we have to maintain the flow of the program execution we use this  

'''a = int(input("Enter first no"))
b = int(input("Enter second no"))
try:
    print(a/b)
except:
    print("Can't divide by zero")

print('Hello')
'''
##when we use special symbols like & $ # 
'''
try:
    a = int(input("Enter first no"))
    b = int(input("Enter second no"))
    print(a/b)
except:
    print("Can't divide by zero")

print('Hello')
'''
## 
'''
try:
    print(2/0)

except ZeroDivisionError as message: # division by zero
    print("The description of exception: "*message)

'''
#Multiple execept block
'''
try :
    a=int(input("enter first integer no")) # $
    b=int(input("enter second integer no"))
    print(a/b)
except ZeroDivisionError as message:
    print("plz ensure that you can't divide any no by zero:",message)
except ValueError as message:
    print("Enter only interger no=>", message)
'''


#Hand1ing multiple diffrent kinds of exception with single except block.

'''try:
    a=int(input("enter first integer no"))
    b=int(input("enter second integer no"))
    print(a/b)
except    (ValueError, ZeroDivisionError) as message:
    print(message)
'''

#We can use else block if no error will genrate it is depend on our own need and neccessity
'''
try:
    a=int(input("enter first integer no"))
    b=int(input("enter second integer no"))
    print(a/b)

except (ValueError, ZeroDivisionError) as message:
        print("Enter correct number: " , message)
else:
    print ("everything is OK")    

'''
# Finally block will always executed whether try block genrate error or not
'''try:
    a=int(input("enter first integer no"))
    b=int(input("enter second integer no"))
    print(a/b)
except (ValueError, ZeroDivisionError) as message:
    print("Enter correct number: ",message)
finally:
    print("I will always executed ")'''

# nested try except block
'''try:
    a = int(input("Enter first number"))
    b = int(input("Enter second number"))
    try:
        print(a/b)
    except ZeroDivisionError as msg:
        print(msg)

except ValueError as msg:
    print(msg)    
'''

# All Blocks 
'''
try:
    a=int(input("enter first integer no"))
    b=int(input("enter second integer no"))
    print(a/b)
except (ValueError, ZeroDivisionError) as message:
    print ("Please ensure that you can't divide any no.by zero:", message)
    #default except block never use at place of first except block
except:
    print("Value Error!!")
else:
    print("There are  no error in try block ")
finally:
    print("I will always executed !!")         


'''

import csv
f = open("Exception.csv", "a", newline="")
a = csv.writer(f)
a . writerow(["Id","name","rollno","email","mobileno","p1","p2","p3","p4","p5","total","percentage","result"])

total = ()
percentage = float() 
result = ('')



try:
    n= int(input("How many records want to enter"))
    k=0
    while k < n :
        id = int(input("Enter student id:"))
        name = input("Enter your name")
        rollno = (input("Enter your roll number"))
        email = (input("enter your Email id"))
        mobileno = int(input("enter your mob no"))
        p1 = int(input("Enter your p1 marks"))
        p2 = int(input("Enter your p12 marks"))
        p3 = int(input("Enter your p3 marks"))
        p4 = int(input("Enter your p4 marks"))
        p5 = int(input("Enter your p5 marks"))

    total = p1+p2+p3+p4+p5
    percentage=(total/500)*100
    p=[p1,p2,p3,p4,p5]

    for i in range(0,5):
        if p[i]<=40:
            result="fail"
            break
        else:
            result="Pass"
    
   
    a.writerow([id,name,rollno,email,mobileno,p1,p2,p3,p4,p5,total,percentage,result])

    k=k+1

except (ValueError, ZeroDivisionError) as message:
    print("Bhai aise kaise chalega yaar: ",message)
else:
    #print("Nind mai ho kya ?")
    print("done")

'''
Modules in python

The group of function, variable, classes saved in python as a single
file then it is called as python module, an independent program in
python are called as python module.

Every .py file act as a python module because it contain everything

If we want to access any function variable or class from one program
to another program then we have to use import keyword
Syntax:-
import module_name 


'''

























