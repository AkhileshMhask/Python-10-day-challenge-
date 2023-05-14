def binanry_search(list, item):
    low = 0                     #low and high keep track of which part of the list you'll search in.
    high = len(list)-1
    
    while low <= high:      #While you haven't narrowed it down to one element ...
        mid =(low + high)//2    #Check the middle element.
        guess =list[mid]
        if guess == item:       #Found the item.
            return mid
        if guess > item:        #The guess was tooo high
            high = mid -1
        else:                   #the guess was too low.
            low = mid + 1
    return None             #the item doesn't exist.
list =[1,2,3,4,5,6,7,8,9,10]
print(binanry_search(list,6))


    