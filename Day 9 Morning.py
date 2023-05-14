# Prashant 
 
#Stack program

'''#import time
mystack=[]      #Empty stack to get the values / element 
size = int(input("Enter the size of stack:"))   #stack size ex.5

for i in range (size):      #Loop ex. it will work for 5 times
    a= int(input("Push element in stack:"))
    mystack.append(a)
else:                           #when condition falis (Stack size gets full)
    print("Stack is full") 
    print(mystack)

print("Pop operation start :")
for i in range(size):
   # time.sleep(2)          #time library used for delaying pop operation form the stack.
    print(mystack.pop(),"pop element from stack")       #by Default pop function removes from top value
else:                       #when condition fails (Stack empty)
    print("Stack is empty")
    print(mystack)           

'''
#Queue
'''
import time
myqueue=[]      #Empty queue to get the values / element    
size = int(input("Enter the size of queue:"))   #queue size ex.5    
print()


for i in range (size):
    a = int(input("Add item in Queue :"))
    myqueue.append(a)
else:
    print("Queue is full")
    print("Queue Elements are :=", myqueue) 

for i in range(size):
    time.sleep(2)
    j=0
    print(myqueue.pop(j),": Remove element from Queue")

else:
    print("Queue is empty")    

'''




import time

class Tower:
    def __init__(self):
        print("WELCOME TO TOWER OF HANOI GAME")
        print()
        print("Given Problem  A = [3,2,1]    B = []   c[]")
        print()
        print("Expected Output A=[]          B = []   c[3,2,1]")
        self.A = []
        self.B = []
        self.c = []

    def tower(self, item):
        self.A.append(item)
        time.sleep(1)
        print("A=", self.A)
        print("Items in Tower A\n")

    def pass1(self):
        self.temp = self.A.pop(2)
        self.c.append(self.temp)
        time.sleep(1)
        print("A", self.A, "   ", "B=", self.B, "   ", "c=", self.c)
        print("===============Pass One Completed==================\n")
        print("Items in Tower A\n")

    def pass2(self):
        self.temp = self.A.pop(1)
        self.B.append(self.temp)
        time.sleep(1)
        print("A", self.A, "   ", "B=", self.B, "   ", "c=", self.c)
        print("===============Pass Two Completed==================\n")

    def pass3(self):
        self.temp = self.c.pop(0)
        self.B.append(self.temp)
        time.sleep(1)
        print("A", self.A, "   ", "B=", self.B, "   ", "c=", self.c)
        print("===================Pass Three Completed==================\n")

    def pass4(self):
        self.temp = self.A.pop(0)
        self.c.append(self.temp)
        time.sleep(1)
        print("A", self.A, "   ", "B=", self.B, "   ", "c=", self.c)
        print("==================Pass Four Completed==================\n")

    def pass5(self):
        self.temp = self.B.pop(1)
        self.A.append(self.temp)
        time.sleep(1)
        print("A", self.A, "   ", "B=", self.B, "   ", "c=", self.c)
        print("===============Pass Five Completed==================\n")

    def pass6(self):
        self.temp = self.B.pop(0)
        self.c.append(self.temp)
        time.sleep(1)
        print("A", self.A, "   ", "B=", self.B, "   ", "c=", self.c)
        print("=================Pass Six Completed==================\n")

    def pass7(self):
        self.temp = self.A.pop(0)
        self.c.append(self.temp)
        time.sleep(1)
        print("A",self.A  ,"   ",   "B=",self.B     ,"   ","C=",self.c)
        print("==============Pass Seven Completed==================\n")


obj = Tower()
obj.tower(3)
obj.tower(2)
obj.tower(1)
obj.pass1()
obj.pass2()
obj.pass3()
obj.pass4()
obj.pass5()
obj.pass6()
obj.pass7()

