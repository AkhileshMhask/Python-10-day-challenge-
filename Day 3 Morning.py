'''
for i in range (10, 0, -1):
    print(i)


i=0
while i < 6:
    i = i+1
    if i == 3:
        continue
print (i)

'''


'''import math as math
r = -1
if r>=0:
    volume_sphere = (4/3) * math.pi*r**3
    print(volume_sphere)
else: 
    print('Radius cant be negative')    

'''

# Using while loop asking again to enter radius of the sphere 

'''import math 

while True:
    r = float0(input("Enter the radius of the sphere: "))
    if r >= 0:
        volume_sphere = (4/3) * math.pi * r ** 3
        print("The volume of the sphere is:", volume_sphere)
        break
    else:
        print("Error: Radius cannot be negative. Please try again.")
'''


'''
#Sir's code
import math
rad = float(input("Radius:"))
while True:
        if rad <= 0:
            rad = float(input("Enter the radius again:"))
        else:
            vol = 4/3 * math.pi * rad **3
            break   
print("The Volume is ", vol)        
'''



 

'''#Searched answer

users = {'user1': 'password1', 'user2': 'password2', 'user3': 'password3'}

# define a function for user authentication
def authenticate_user(username, password):
    if username in users and users[username] == password:
        print('Login successful!')
    else:
        print('Invalid username or password')

# prompt the user to enter their credentials
username = input('Enter your username: ')
password = input('Enter your password: ')

'''

# 
'''d = {
        'user1': 'password1', 'user2': 'password2', 'user3': 'password3'

    
}
while True:
    user = input("Username: ")
    if user in d:
        password = input("Enter Pass:")
        if password == d[user]:
            print("Logged in ")
            break
        else:
            print("Invalid credentials")
            password = input("Enter a valid passsword")    
    else:
        password = input("Create password:")
        d[user] = password
'''


#######

'''d = {
        'user1': 'password1', 'user2': 'password2', 'user3': 'password3'
}

user = input("Enter Username: ")
#password = input("Enter Password: ")

while True:
    #user = input("Username: ")
    if user in d:
        password = input("Enter password: ")
        if password == d[user]:
            print("Logged in!")
            break
        else:
            print("Invalid credentials")
            password = input("Enter a valid password: ")
            d[user] = password  # update the password in the dictionary
            
    else:
        password = input("Create password: ")
        d[user] = password
        print("Registred")
        break
        '''


'''
import time as t1

currentTime=t1.ctime()

print(currentTime)
days=[

    #'monday':'mon' all till sunday
]
timelist = currentTime.split()
print("Todays is {} {}, and day is {}. ".format(timelist[1],timelist[2],timelist[0]))

'''

'''import time
from time import strftime
hour = int(strftime("%H"))




while True:
    current_time = time.strftime('%I:%M:%S')
    
    if time.localtime().tm_hour <= 12:
        print(f"The current time is {current_time}. Good morning!")
        break
    elif time.localtime().tm_hour <= 18:
        print(f"The current time is {current_time}. Good afternoon!")
        break
    else:
        print(f"The current time is {current_time}. Good evening!")
        break
        time.sleep(1)

'''

'''from time import strftime # for time related operations
hour = int(strftime ("%H") )
amorpm = strftime("%p")
if hour in range(4, 12):
    print ("Good morning, it is {} {}". format (hour%12, amorpm))
elif hour in range(12, 17):
    print ("Good afternoon, it is {} {}". format (hour%12, amorpm))
elif hour in range(17, 20):
    pass
else:
    print("Good Night !!  Current time is {} {}".format(hour%12, amorpm))

'''

#next 15 leap years in the for loop
'''start_year = int(input("select year: "))
no_of_years = int(input("How many years wants to check"))
end_year =  start_year + no_of_years 

for year in range(start_year-1, end_year):
    year +=1
    if year %4 == 0 and (year %100 !=0 or year % 400==0):
        print ("{}: Is a leap year".format(year))
    else:
        print (year)    
'''
'''#
import time
year= int(time.strftime("%Y"))
leap_year=[]
while len(leap_year) < 15:
    if year %4 ==0:
        leap_year.append(year)
    year = year +1 
print(leap_year)


'''
'''given_year=int(input("year:"))
count=0
list_of_leap_years=[]

while(count<15) :
    if given_year %4 == 0 and (given_year%400 == 0 or given_year%100 !=0):
        list_of_leap_years.append(given_year)
        count=count+1
    given_year=given_year+1    
print(list_of_leap_years)

'''
#You are given a date. Your task is to find what the day is on that date.

