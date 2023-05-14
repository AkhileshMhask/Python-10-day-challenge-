#File Handeling

'''f = open("myfile.txt", "w")  #open that file or create it 
print("name of file" ,f.name) # file name 
print("file mode",f.mode)  #file mode readable/writable
print(" readeble " , f. readable()) #checks is it readable?
print(" writeable ",f.writable())  #checks is it writeable?
print(" file has closed",f.closed) #checks file cloed or not 
f. close()  # Closing file
print(" file has closed", f. closed)  # #checks is it closed?
'''


'''# performing write operation
f = open("Covid.txt","w")   ##open that file or create it 
f. write("\n NGP is full vaccinated city") # Writing in the file 
f. write("\n Covid ab toh nhi hai ")
f. write("\n College bhi start hoo gya")
f. write("\n kya likhu samjh nhi aa rha ")
f. write("\n kuch bhi likh deta hu")
f. close()               #File CLose
print("file operation is done") #message to know that execution is done!
'''

'''#Overriding 
f = open("Covid.txt","w")   ##open that file or create it 
f. write("\n NGP is full vaccinated city") # Writing in the file 
f. write("\n Covid ab toh nhi hai ")
f. write("\n College bhi start hoo gya")
f.close()
'''
'''#Append mode
f = open("Covid.txt","a")   ##open that file or create it 
f. write("\n NGP is full vaccinated city") # Writing in the file 
f. write("\n Covid ab toh nhi hai ")
f. write("\n College bhi start hoo gya")
f. write("\n Data Append hoo rha hai?")
f.close()
'''


'''# write lines method

# inserting list
f = open("Covid.txt","w")
mylist= ["prashant " , "mahesh " , " suresh" ]
f. writelines(mylist) # here we can only can pass string not int and float
f. close()
print("written work has done successfully")'''



'''#WIth statement 
with open("myfile.txt","a") as f:
    f. write( " amit\n " )
    f.write("ashish\n")
    f. write("Prashant\n")
    print("file closed: " , f.closed)

print("file closed:", f.closed)'''

'''# read function
f = open("myfile.txt","r")
print("Curren index  position of file pointer",f.tell())
print(f.read())
'''

'''# operation with CSV file
import csv
f = open("student.csv", "a", newline="")
a = csv.writer(f)           # here it will return csvwriter object
a . writerow( [ " studentID" , " rollno" , " name" , "mobileno" ] )
#studentid= 1
#rollno = 111
#name= "Akhilesh"
#mobile no =8010637136
studentid = int("Enter student id:")
rollno = int("Enter your roll number")
name = input("Enter your name")
'''


'''
# write values in the file
 
import csv
f = open("student.csv", "a", newline="")
a = csv.writer(f)           # here it will return csvwriter object
#a . writerow( [ " studentID" , " rollno" , " name" , "mobileno" ] )
studentid= 1
rollno = 111
name= "Akhilesh"
mobileno = 8010637136
#studentid = int(input("Enter student id:"))
#rollno = int(input("Enter your roll number"))
#name = input("Enter your name")

a.writerow([studentid, rollno, name, mobileno])
print("record has saveed")'''

'''###### Taking values from the user
import csv
f = open("student.csv", "a", newline="")
a = csv.writer(f) 
studentid = int(input("Enter student id:"))
rollno = int(input("Enter your roll number"))
name = input("Enter your name")
mobileno = int(input("enter your mob no"))
a.writerow([studentid,rollno,name,mobileno])
print("student record has save")
'''


###
