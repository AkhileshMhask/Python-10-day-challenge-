#Rounak 
'''
class Car:
    'common base class for all cars'
    carcount = 0

    def __init__(self, name, year):
        self.name = name
        self.year = year
        Car.carcount += 1
        
    def dislplayCount(self):
        print("Total car %d" % Car.carcount)

    def displayCar(self):
        print("Name :",self.name,",Year :",self.year)


#this would create first object of Car class
car1= Car("Lambo",2012)
#This would create second object of Car Class
car2 = Car("AUDi", 2021)
#This would create Third object of Car Class
car3 = Car("Fortunur", 2020)

car1.displayCar()
car2.displayCar()
car3.displayCar()

print("Total car %d" % Car.carcount)


'''

#Sorting 
'''
def sort(array):
    n =len(array)

    for i in range(n): 
        alreadysorted = True

    for j in range (n-i-1):
        if array[j]>array[j+1]:
            array[j],array[j+1] = array[j+1],array[j]

            alreadysorted = False
        if alreadysorted:
            break

    return array             

# Initialize an array with values
my_array = [5, 3, 8, 6, 7, 2]

# Call the bubble_sort function and pass the array as an argument
sorted_array = sort(my_array)

# Print the sorted array
print(sorted_array)
'''


def bubble_sort(array):
    n = len(array)

    for i in range(n):
        # Create a flag that will allow the function to
        # terminate early if there's nothing left to sort
        already_sorted = True

        # Start looking at each item of the list one by one,
        # comparing it with its adjacent value. With each
        # iteration, the portion of the array that you look at
        # shrinks because the remaining items have already been
        # sorted.
        for j in range(n - i - 1):
            if array[j] > array[j + 1]:
                # If the item you're looking at is greater than its
                # adjacent value, then swap them
                array[j], array[j + 1] = array[j + 1], array[j]

                # Since you had to swap two elements,
                # set the `already_sorted` flag to `False` so the
                # algorithm doesn't finish prematurely
                already_sorted = False

        # If there were no swaps during the last iteration,
        # the array is already sorted, and you can terminate
        if already_sorted:
            break

    return array

# Initialize an array with values
my_array = [5, 3, 8, 6, 7, 2]

# Call the bubble_sort function and pass the array as an argument
sorted_array = bubble_sort(my_array)

# Print the sorted array
print(sorted_array)
