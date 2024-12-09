"""class shape():
    def area(self):
        print("Area not defined")
class circle(shape):
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        area_circle = 3.14 * (self.radius**2)
        print("the area of circle is ",area_circle)

n=int(input("enter the radius "))


obj=circle(n)
obj.area()
        

class employee():
    def work(self):
        print("employee is working")

class manager(employee):
    def work(self):
        print("manager is managing")

class developer(employee):
    def work(self):
        print("developer is working")

obj1=manager()
obj=developer()

obj1.work()
obj.work()

class vehicle():
    def start(self):
        print("starting vehicle")

class car(vehicle):
    def start(self):
        super().start() 
        print("starting car")

obj=car()
obj.start()


class calcs():
    def __init__(self,a):
        self.a=a
    def __add__(self,other):
       return self.a + other.a
    def __sub__(self,other):
       return self.a - other.a
    def __mul__(self,other):
       return self.a * other.a
    def __truediv__(self,other):
       return self.a / other.a
        
        
n=int(input("enter the value: "))
p=int(input("enter the value 2: "))

obj1=calcs(n)
obj2=calcs(p)

obj3=calcs(n)
obj4=calcs(p)

obj5=calcs(n)
obj6=calcs(p)

obj7=calcs(n)
obj8=calcs(p)


print("Addition:", obj1 + obj2)
print("Subtraction:", obj3 - obj4)
print("Multiplication:", obj5 * obj6)
print("Division:", obj7 / obj8)


class company:
    def __init__(self,name) -> None:
        self.__name=name
    def person(self):
        print(self.__name)

n= input("enter your name ")
obj=company(n)
obj.person()


class car:
    def __init__(self,model):
        self.__model= model

    def set_model(self,model):
        self.__model=model
    
    def get_model(self):
      return self.__model

n=input("enter the model ")
obj=car(n)
print(obj.get_model())

class employee:
    def __init__(self,name,salary) -> None:
        self.name=name
        self.__salary=None
        self.set_salary(salary)

    def set_salary(self,salary):
        if salary > 0:
            self.__salary=salary
        else:
            raise ValueError("Salary must be a positive value.")

    def get_salary(self):
        return self.__salary

n=input("enter your name: ")

try:
    s=int(input("enter the salary: "))
    obj=employee(n,s)
    print(obj.get_salary())

except ValueError as e:
    print(e)


#abstraction

from abc import ABC,abstractmethod

class theater(ABC):
    @abstractmethod
    def screens(self):
        pass

    @abstractmethod
    def canteen(self):
        pass

    @abstractmethod
    def parking(self):
        pass
    
    @abstractmethod
    def movies(self):
        pass


class movies(theater):
    def __init__(self,movieid,screen):
            self.movieid=movieid
            self.screen=screen

    def screens(self):
        print("this theater have 4 screens")

    def canteen(self):
        print("this theater have one canteen ")

    def parking(self):
        print("this theater have very large parking")

    def movies(self):
        print("currently running movie : ", self.movieid)
        print(f"currently  {self.movieid} running  screen : ", self.screen)


n=input("enter the movie name: ")
s=int(input("enter the screen: "))

obj=movies(n,s)
obj.screens()
obj.movies()"""

from abc import ABC,abstractmethod

class theater(ABC):
    @abstractmethod
    def screens(self):
        pass

    @abstractmethod
    def canteen(self):
        pass

    @abstractmethod
    def parking(self):
        pass
    
    @abstractmethod
    def movies(self):
        pass


class movies(theater,ABC):
    

    @abstractmethod
    def screens(self):
       pass
    
    @abstractmethod
    def canteen(self):
        pass

    @abstractmethod
    def parking(self):
        pass
    @abstractmethod
    def movies(self):
        pass


class pushpa_2(movies):
    def __init__(self,movieid,screen):
            self.movieid=movieid
            self.screen=screen

    def screens(self):
        print("this theater have 4 screens")

    def canteen(self):
        print("this theater have one canteen ")

    def parking(self):
        print("this theater have very large parking")

    def movies(self):
        print("currently running movie : ", self.movieid)
        print(f"currently  {self.movieid} running  screen : ", self.screen)



n=input("enter the movie name: ")
s=int(input("enter the screen: "))

obj=pushpa_2(n,s)
obj.screens()
obj.movies()