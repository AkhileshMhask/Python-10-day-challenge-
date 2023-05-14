#Ronak sir 
# Selection sort 
'''
# Python program for implementation of the Selection sort algorithm

Array = [156,141,35,94,88,61,111]
  
# loop to Traverse through all the elements in the given array
for i in range(len(Array)):
      
    # setting min_indx equal to the first unsorted element
    
    min_indx = i
    # Loop to iterate over un-sorted sub-array
    for j in range(i+1, len(Array)):
    
    #Finding the minimum element in the unsorted sub-array
        if Array[min_indx] > Array[j]:
            min_indx = j
              
    # swapping the minimum element with the element at min_index to place it at its correct position    
    Array[i], Array[min_indx] = Array[min_indx], Array[i]
  
# Printing the modified array after the selection sort algorithm is applied

print(Array)



'''


#psudocode 
'''
repeat (numOfElements - 1) times

  set the first unsorted element as the minimum

  for each of the unsorted elements

    if element < currentMinimum

      set element as new minimum

  swap minimum with first unsorted position

'''

'''
def findsmallest(arr):
    smallest = arr[0]                #Stores the smallest value
    smallest_index=0                #stores the index of the smallest value
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest=arr[i]
            smallest_index=i
    return smallest_index    


#print(findsmallest([156,141,35,94,88,61,111]))


def selectionSort(arr):     #Sorts an arrray
    newArr = []
    for i in range (len(arr)):
        smallest = findsmallest(arr)  #finds the smallest element in the array and adds it to the new array.
        newArr.append(arr.pop(smallest))
    return newArr

print (selectionSort([5,3,6,7,10]))        

'''
#Insertion Sort 
'''
def InsertionSort(a):
  # traversing the array from 1 to length of the array(a)
    for i in range(1, len(a)):
  
        temp = a[i]
  
        # Shift elements of array[0 to i-1], that are
        # greater than temp, to one position ahead
        # of their current position
        j = i-1
        while j >=0 and temp < a[j] :
                a[j+1] = a[j]
                j -= 1
        a[j+1] = temp

# array to be sorted        
a = [10, 5, 13, 8, 2]
InsertionSort(a)
print("Array after sorting:")
print(a)
'''

'''
def quicksort(array):
    if len(array) < 2:
        return array        #Base case: arrays with 0 or 1 element are already “sorted.”
    else:
        pivot = array[0]                                    #Recursive case
        less = [i for i in array[1:] if i <= pivot]         #Sub-array of all the elements

        greater = [i for i in array[1:] if i > pivot]       #Sub-array of all the elements

        return quicksort(less) + [pivot] + quicksort(greater)

print (quicksort([10, 5, 2, 3]))


'''



class Nodes:
    #creating a node
    def __init__(self,item):
        self.item = item
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
                
#creating a object of linked list class and assigning a Null 

linked_list = LinkedList()   #linked list class constructor

linked_list.head= Nodes(1)
second = Nodes(2)
third = Nodes(3)

#connect nodes
linked_list.head.next = second
second.next = third

#print the linked list 
while linked_list.head != None:
    print(linked_list.head.item, end = " ")
    linked_list.head = linked_list.head.next



