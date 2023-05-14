'''def f(x):
    "This is a power function."
    return x**5+ 2*x


given_year=int(input("year:"))
count=0
list_of_leap_years=[]

while(count<15) :
    if given_year %4 == 0 and (given_year%400 == 0 or given_year%100 !=0):
        list_of_leap_years.append(given_year)
        count=count+1
    given_year=given_year+1    
print(list_of_leap_years)

'''
'''
def find_leap_year(given_year):

    count=0
    list_of_leap_years=[]

    while(count<15) :
        if given_year %4 == 0 and (given_year%400 == 0 or given_year%100 !=0):
            list_of_leap_years.append(given_year)
            count=count+1
        given_year=given_year+1    

    return list_of_leap_years    
list_of_leap_years=find_leap_year(2000)
print(list_of_leap_years)  
'''

'''
#def function
def f1(x, y = 2, z = 3):
    return x ** y + 2 + z


print(f1(3,4,5)) # 3^3 
print(f1(3, z=4, y=5)) # 3^5 81*3 + 4 = 249
print(f1(z=1, y=3, x=5)) # 5^3 + 2+1 =128
#print(f1(z=1, y=3, 5)) # This will Give error 

'''

'''
def contcat(*x):   # using * we can passs any value directly 
    return x
print(contcat(" abcd","DY PATIL","anything"))
'''

#Tuple Arguments

'''def concat (*args, sep="/"):
    return sep.join(args)

print(concat("abcd","xyz","aabbcc"))
'''

'''def concat(*args, sep='/'):
    for name in args:

        print(name+sep, end="")
print (concat ( "Durga " ,"Sati", "Parvati"))

'''

'''def findvolume(length=1, width=1, depth=1):
    return length *width * depth
print(findvolume(1, 2, 3))
print(findvolume(length=5, depth=2, width=4))
print(findvolume(2, depth=3, width=4))
'''
###
'''def findvolume(*args):
    #Returns the volume of a cuboid.
    return args[0] * args[1]* args[2]
print (findvolume(1,2,3))

'''

'''#key word arguments 
def findvolume(**kwargs):
    #Returns the volume of a cuboid
    return kwargs['length'] * kwargs['depth'] *kwargs['width']
print (findvolume( length=5,depth=2,width=4) )
'''




#bydefault python uses tuple
def f():
     a = 5
     b = 6
     c = 7
     return a, b, c

result = f()
print(result)















































