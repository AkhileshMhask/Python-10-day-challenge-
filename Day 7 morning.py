#Rounak Sir's

'''#Dogs Examplpe 
# - instance variable (Age, Height, weight, color )
# + Constructor (+ Dog(void+ setAge(int): void 
#   + getAge0: int
    + setHeight(float): void
    + getHeight(): float
    + setWeight(double): void
    + getWeight():double
   
'''


'''class Car:
#construct-paramterized constuctor


    def __inint__(self,name):
        print("This is parameterized constructor")
        self.name=name

    def model (self):
        print("my first self",self.name)

volvo = Car("Volvo S90")
volvo.model()
'''

'''
class Car(object):

    def __init__(self): #
        self.__mileage = 16

    def get_Mileage(self):
        print(self.__mileage)

    def set_mileage(self,mileage):
        self.__mileage = mileage 

volvo = Car()
volvo.get_Mileage()
volvo.set_mileage(20)
volvo.get_Mileage()

'''
'''
class Phone:
    def __init__(self, price, company, camera):
        self.price = price
        self.company = company
        self.camera = camera

    def buy(self):
        print ("Buying a phone")

    def return_phone(self):
        print ("Returning a phone")

class FeaturePhone(Phone):
    pass

class SmartPhone(Phone):
    pass

#FeaturePhone(10000,"Apple","13px").buy()
phone = SmartPhone(17000, "Motorola", "48 mg px")
phone.return_phone()

print(FeaturePhone)



'''

'''class A:
    pass
class B (A):
    pass    




'''

'''class Man:
    def sayHi (self,name=None) :
        if name is not None:
            print("Hi " + name)
        else:
            print("Hi")

obj = Man()
obj.sayHi()
obj.sayHi("Akhil")
'''
class Car:
    def start(self, a, b=None) :
        if b is not None:
            return a + b
        else:
            return a
car= Car()
print(car.start(2,8))
