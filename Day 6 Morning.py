# Prashant Sir
#Python object oriented programming

'''
Class in python

* Class is a way which binds data member and its associates
function together within a single unit.

* Any variables declare within a class are called data members,
any functions declare within a class are called members
functions.

* Everything in a python a object

* Class properties can be represented by member variable.

* In class action is done by member function



Syntax of class:-
Class classname:
    "statement"

    member variables
    member function

Ex-
Class Student:
    rollno = 101
    def show(self):
    print(self. roll no)

* Object:-
* It is a instance of class. It is a basic runtime entity of an object
  oriented system
* By using object we can communicate with data member and member
  function of the class

Q:-why we create object
-> To store the temporary data.


Syntax of object :-

Self variable:- 
                referencevariablename = classname()
Ex:-    
                obj = Student()

1.by usiqg self variable we pointing to the current object
2.self is a default argument
3.self is like this keyword in java
4.instead of writing self we can write any other name
5.in class level or in function first argument must be self




Object hamesha class ke bahar create kiya jata hai 




*Constructor :

1. Here in python the name of the constructor is __init__(self).
2. Constructor call automatically whenever we create object or we
   can say that at the time of creation of object.
3. By using constructor we initialize the object.  # Provide the memory for the process
4. There is no mandatory to declare a constructor inside class but
   if we are not going to declare constructor so python provide
   default constructor.
5. Constructor will execute only one time when we create a object.
6. Always we have to pass one argument in constructor(self).


kitni memory chaiye constructor 
checks how many data members are there then assigns  



'''


'''

class Student:
    roll_number = 101
    num1 = 50
    num2 = 100   # data member

    def add(self):      #member function
        print(self.num1+self.num2)
        self.name = input("Enter name:")
        print(self.namea)

obj = Student() # creating Object of a class
obj.add()
print(obj.roll_number)        

'''


#Example of Constructor
'''
class Hod:
    def __init__(self): # constructor
        self.name ='Akhilesh' #data member
        self.age=21
        self.empid=1001
        
    def info(self): # instance method
        print("My name is:",self.name)
        print("My Age:",self.age ) 
        print("My emp id:",self.empid)

obj = Hod()#object create
obj.info()

'''
# For each object only one time constructor called
'''class NewClass:
    def __init__(self): #constructor
        print("my name is constructor and i allways execute first")

    def show(self):#     member function inside of class
        print( 'welcome to class level programming')

obj = NewClass()
obj.show()
'''

#Note :- Python is having internally default constructor and it gets calls automatically when we create any object. 
'''
class Hod:
    def __init__(self,name,age,rollno) :  # parameterize constructor
        self.name = name
        self.age = age
        self.rollno = rollno

    def show(self):
        print('name = ',self.name)
        print(' age = ', self. age)
        print('rollno =' ,self. rollno)


obj = Hod( 'Akhilesh',21,101)
obj.show()

'''

'''
#In a class if we have to represent data so by using variable we can represent

There are three types of variable we can declare inside a class.

Instance variable ->     instance variable declare at object level
Static variable   ->    static variable declare at class level
Local variable    ->    local variable declare at function level
'''



#declaring instance variable inside a constructor by using self variable.
'''
class Student:
    def __init__(self):
        self.s_name = 'Akhilesh'
        self.l_name = 'Mhaske'
        self.s_age = 21
        self.s_rollno = 11
        self.s_branch = 'IT'

obj = Student()
print(obj.__dict__)        


'''

#declaring instance variable inside a instance method by using self variable.
'''
class Student:
    def __init__(self):

        self.s_name = 'Akhilesh'
        self.l_name = 'Mhaske'
        self.s_age = 21
        self.s_rollno = 11
        self.s_branch = 'IT'

    def getdata( self) : #instance method
        self.s_mb =    28282828282
 
obj = Student() # until and unless we call the method it will not not added to the object
obj . getdata( )
print(obj.__dict__ )

'''

#declaring instance variable outside a class by using object.
'''
class Student:
    def __init__(self):

        self.s_name = 'Akhilesh'
        self.l_name = 'Mhaske'
        self.s_age = 21
        self.s_branch = 'IT'
        
    def getdata( self) : #instance method
        self.s_mb =    28282828282
 
obj = Student() 
obj . getdata( )
obj.s_rollno = 11 # Adding instance variable by using object 
print(obj.__dict__ )

'''


# accessing and deleting instance variable from the class
''' 
class Student:
    def __init__(self):

        self.s_name = 'Akhilesh'
        self.l_name = 'Mhaske'
        self.s_age = 21
        
        
    def getdata( self) : #instance method
        self.s_mb =    28282828282
 
obj = Student() 
obj.getdata()
obj.s_branch = 'IT'
obj.s_rollno = 11   #Adding instance variable by using object 
del obj.s_age    #deleting a instance variable 
print(obj.s_name)   #Accessing a variable outside a class
print(obj.__dict__ )

'''


'''
#Static Variables:-

We can declare static variable in class level and outside of method
So we can say that it is in class level instead of instance level , static
variable is initialize only one time in it's life cycle, it is exist only single
instance in every class.

Only one copy of static variable is created for total class and this will
be accessible for all object of the class.

# How to access static variable ? 
There are two ways to access static variable the first one is by class
name or second way by object but programmer recommended to access 
by class name.

By using object or self variable we can we can access or read static
variable but we can not do modification or deletion.

If we try to delete then we will get error



'''

# for every object a seprate copy of instance variable created but in case of static variable on:
# one copy will be created and it is accessble for every object of the class
'''
class College:
    collegename= "DYP College" #static variable (1 memory)
    def __init__(self):
        self. studentname = "Akhilesh" #instance varible(3 seprate memory)

principal = College() # object creation
teacher = College()
accountant = College()

print( "principal= ",principal.collegename, " .... " ,principal.studentname)
print( "teacher =",teacher.collegename,"......",teacher.studentname)
print( "accountant =",accountant.collegename,"......",accountant.studentname)


College.collegename="DYP"  #second way to add static variable
principal.studentname = "Akhilesh Mhaske"

print( "principal=" , principal.collegename, " | " , principal.studentname)
print( "teacher =",teacher.collegename, " | ", teacher.studentname)
print( " accountant=",accountant.collegename, " |", accountant.studentname)
'''

# where we can declare static varaible ?
#inside a class but outside of method
#in a constructor by using class name
#in a instance method by using class name
#in a classmethod using class name or cls varible
#staticmethod by using class name
# ================================
#how do we access static variable ?
# inside instance method using self or class name
# in a constructor using self or class name
# in a class method using CIs variable or class name
# in a static method using class name
# outside of the class using object or class name
# how do we delete the static variable ?
# del classname. Staticvariablename
# inside classmethod we can use cls variable: del cls:Staticvariablename


'''
Types of methods
There are three types of methods
1. Static method
2. Instance method
3. Class method

Instance method:-
1.If any instance variable we are implementing inside of any method
2.then that method will be called as instance method.
3.Instance method should have self as parameter.

Static method:-
1.We can use static method when the code that belongs to class it do not use the object.
2.St they are not dependent on the state of the object
3.in a static method we will not use any instance or class variable.
4.Self and cls argument doesn't required here to declare
5.We can declare static method using @staticmethod decorator

Class Methods:    #does not asked in the interview

1.Inside method implementation if we are using only class variables (static variables),
  then such type of methods we should declare as class method.

1.We can declare class method explicitly by using @classmethod decorator. For class
  method we should provide cls variable at the time of declaration
  We can call classmethod by using classname or object reference variable.


'''


#implementing innner class concept
class BE_first_year:
    def __init__(self):
        self.college_name = "DYP"
        self.branch_name = "IT"
        self.objsem = self.Firstname() #inner class
    def display(self):
        print("college name =",self.college_name)
        print("Branch_name =", self.branch_name)

    #inner class
    class Firstname:
        def __init__(self): 
            self.sub1 ="M1"
            self.sub2 ="Phy"
            self.sub3 ="chem"
            self.sub4 ="Eng"
            self.sub5 ="C-lang"
            self.sub6 ="Python"

        def show(self):
            print("subject1 =", self.sub1) 
            print("subject2 =", self.sub2) 
            print("subject3 =", self.sub3) 
            print("subject4 =", self.sub4) 
            print("subject5 =", self.sub5)  
            print("subject6 =", self.sub6)   

obj = BE_first_year()
obj.display()
objsem =obj.objsem
objsem.show()










