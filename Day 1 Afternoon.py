
'''
a = 13
b = 15

print("Addition= :",a+b)
print("Subtraction= :",a-b)
print("Multiplication= :",a*b)

c = a+b
print("Addition= :",c)

'''

'''#swapping (using 3rd variable)

num1 = 5
num2 = 10 

print("Before swapping the num1=", num1, "and Num2=",num2)
temp = num1 # temp —5
num1 = num2 # numl= 10
num2 = temp # num2
print("After swappping the num1=" ,num1,"and Num2=" ,num2)

'''
#swapping by logic 
'''a = 100
b = 200

print("Before swapping the a=",a,"and b=", b)
a = a+b
b = a-b
a = a-b 
print("After swapping the a=",a,"and b=" ,b)'''


# Percentage 
'''p1 = 50 
p2 = 60
p3 = 55

Total = p1+p2+p3 
percent = Total/3.0

print("Total  =:", Total)
print("Percentage =:", percent)
'''
# Calculate SI

'''p=10000
r=10 
t=1
si=p*r*t/100
print("Simple Interest=",si)
'''

# TO calculate area of circle

'''pi=3.14
r= 5
a=pi*r*r

print("Area=",a)'''


#Circumference of the circle

'''pi= 3.14
r = 5
a = 2*pi*r

print("circumference= ",a)'''


# WAP to enter height of user in feets and convert it into inch and centimeter

'''height =4
inch = height*12
cm= inch*2.54
print("inch = ", inch)
print("cm=",cm)'''

# To centigrate temp and convert it into feranite temp

'''ct = 20
f = 1.8*ct+240
print("feranite tem=", f)'''



'''name = "Akhileshhhhh" # string 
print(name[0]) #A
print(name[-1]) #h
print(name[1]) #k
print(name[10]) #h
print(name[0:12:2]) #Ahlshh
print(name[1:]) #khileshhhhh
print(name[:5]) #Akhil
print(name[:]) #Akhileshhhhh
print(name[1:4]) #khi

'''

#memory management Example 
'''math = 50
chem = 50 
physics = 40

print(id(math))
print(id(chem))
print(id(physics))

math = 39 
math = 49 

print (id(math))
print (id(chem))
print (id(physics))

'''

# int ( ) used to convert in integer 3.14=int=3

'''print(int(3.14))
#print(int(10+5j))
print(int(True))
print(int(False))
#print(int("4.22"))
print(int("4"))'''


#Float used to convert 
'''print(float(3))
#print(float (50+2j))
print(float(True))
print(float(False))
print(float(4.22))
print(float("4"))
'''
#Complex() used to convert 

'''print(complex(3))
print(complex(12.5))
print(complex(True))
print(complex(False))
print(complex("5"))
print(complex("5.6"))
print(complex(5,-3))
print(complex(True,False))'''


#Boolean() used to convert 
'''print (bool(0))
print (bool(15))
print (bool(3.14))
print(bool(0.0))
print(bool(1+2j))
print (bool(-1))
print (bool(0+0j))
print(bool(False))
print (bool(True))'''

#str() is used to convert 
'''print (str(100))
print (str(3.14))
print (str(True))
print (str(False))
print (str(5+6j))
print (str('A'))'''


'''#List is mutable 
mylist = ["prashant","Ashish", "komal", "ankush", "Ashish", 77," sandxp", 60.52,"prashant"]
print (mylist)
print (type (mylist))
print (mylist[1] )
print (mylist[2])
print (mylist[-1] )
print (mylist[2:5]) # n-5,n-1=4
print(mylist[:5]) # n=5 , n-1=4
print(mylist[1:]) # n=8, n-1=8-1=7
print(mylist[0:8:2]) #1,3,5,7
'''
'''mylist[2]="prajakta"
print(mylist)

mylist.append('harsh')
mylist.append("laxman" )
print(mylist)
#append() and extend() both work like same

mylist.insert(3, "sanket") #add
print(mylist)
mylist.remove("harsh") # remove or delete
print(mylist)
'''


'''mylist = [[ 'Prashant', 'jha'],[ '85.56 ' ] , [440022, "yyy" ]]
print("example of multidimensional list:")
print (mylist)
#print (mylist[ row] [ col])
print (mylist[0][0]) 
print (mylist[0][1]) 
print (mylist[1][0])
print (mylist[2][0])
print (mylist[2][1])'''

#Clear method
'''list2 = [50,25.50,'prashant']
print(list2)
list2.clear()
print(list2)'''

#Reverse () method 
'''
mylist =[40,30,20,5]
mylist.reverse()
print(mylist)
'''
'''#sorting example
mylist= [44,22,77, 0, 9,88]
mylist.sort ()
print (mylist)
'''

'''# Alising
# Alising means assigining one variable reference to another variable

mylist=[44,22,77,0,9,88]
newlist= mylist
print(id(mylist))
print(id(newlist))'''

d = {"john":40,"peter":45}
d["john"]
print(d)