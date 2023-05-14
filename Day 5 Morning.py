#Ronak sir

'''#capitalize first letter 
states = ['alabama', 'GeoRgiA',' south carolina#','FIOrIda ',' West virginia?','PuNe','MuMBai']
#print(states)
states =[i.title() for i in states]

print(states)

'''
'''
inp =[1,2,3,4,5,6,7,8,9]
print("The numbers are",inp)
def square(x):
    return x**2
#map(square, inp)

print("& Their squares are",list(map(square, inp)))

'''

'''#Capitalize the starting word using capitalize function
def clean(x):
    return x. capitalize()

states=['alabama', 'GeoRgiA' ,'south carolina#','FIOrIda','West virginia?']

states = map(clean, states)
print(list(states))
'''

#Capitalize the starting word using title function
'''def clean(x):
    return x.title()

states=['alabama', 'GeoRgiA' ,'south carolina#','FIOrIda','West virginia?']

states = map(clean, states)
print(list(states))
'''

#use strip function to remove unnecesory charaters like # ?
'''def clean(x):
    return x.title().strip("#?")
states=['alabama', 'GeoRgiA' ,'south carolina#','FIOrIda','West virginia?']
states = map(clean,states)
print(list(states))
'''


#use str.replace (Not working properly)

'''def clean(x):
    return x.title().replace('# ?','')
states=['alabama', 'GeoRgiA' ,'south carolina#','FIOrIda','West virginia?']
states = map(clean,states)
print(list(states))
'''
#filter
#str.startswith function Return True if string starts with the prefix, otherwise return False.
#remove names that do not starts with  R and P 
'''names = [ "Rakesh" ,"Raunak" ,"Vishwajeet","Jay Prakash","Harjot" ,"Prasant " ]
def startswithRorP(x):
    if x.startswith('P') or x.startswith('R'):
        return True
    else:
        return False    

print(list(filter(startswithRorP,names)))
#print (names)
'''

# using lambda function 
'''
numbers=[1,2,3,4,5,6,7,8,9]
print(list(map(lambda x: x**2, numbers)))

'''

#create file containing names then print my friends are 

'''
f = open("friends.txt", "w")  
print("name of file" ,f.name)  
print("file mode",f.mode)  #file mode readable/writable
f. write(" Prajakta,")
f. write(" Shivam,")
f. write(" Rutuja,")
f. write(" Ronak,")
f. write(" Ujjwala,") 
f. close()  # Closing file
print(" file has closed", f. closed)  # #checks is it closed?

#Reading the file 
f = open("friends.txt","r")
print("My friends are ",)
print(f.read())
'''

##

trainers =[]
names = int(input("How many friends do you have? "))
try:
    with open( 'names.txt',"w" )as wr_fl:
        for name in range (names):
            trainers.append(input())
        trainers = map(lambda x: x+'\n', trainers)    
        wr_fl.writelines(trainers)
except:
    print("Error writing file")

f = open("names.txt","r")
print("My friends are:",)
print(f.read())

