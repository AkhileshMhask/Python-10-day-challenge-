'''movies =["Pathaan", "Pushpa"," KGF", "RRR","Drishyam"]
stars =["SRK","Allu Arjun", "Yash ","NTR J","Mohan Lal"]

for a in range(len(movies)):
    print("The {} Movie is {} ".format(a+1, movies[a]))

for a in range(0, len(stars)):
    print("{} stars in {}.".format(stars[a], movies[a]))

'''
###

'''subjects =[]
for i in range(5):
    subjects.append(input( " Enter the subject:"))
print(subjects)
'''

#squaring 
'''
inp=[1,2,3,4,5,6,7,8,9]
out =[]
for i in range (9):
    out.append(inp[i]*inp[i])
print (inp)
print(out)

#another mtd
 
print(inp)
for i in range(len(inp)):
    inp[i]= inp[i] ** 2
print(inp)    '''


'''tup = (4,5,6)

#tup[2]=6

nested_tup = tup,4,5,5,6
print(nested_tup)'''

'''
name =input("What's your name, dear?");
age = int(input("How old are you?"));
department =input ("Which department you are in?");

print("Hi %s, How are you ? You're %i years old and you're in %s" %(name, age, department))

'''
'''seq = []
#seq = [(1,2,3),(4,5,6,),(7,8,9)]
for i in range(0,7,3):
    seq.append((i+1,i+2,i+3))
print(seq)'''
##
'''
x= input().split()
print(x)'''

'''if condition:
    statement
elif condition2:
    star
else
'''
#volume of spheare using if else

import math as math
r = -1
if r>=0:
    volume_sphere = (4/3) * math.pi*r**3
    print(volume_sphere)
else: 
    print('Radius cant be negative')    









     