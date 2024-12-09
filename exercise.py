
#print location list using for loop

"""location =['kvp','chennai','madurai']
for i in location :
    print(i)"""



#give user input list using for and range

"""a=[]
b=int(input("enter the value"))
for i in range(b):
    c=input("enter the list values")
    a.append(c)"""




"""a=input("enter your name ")
marks = int(input("ENTER THE Marks "))
if marks>60 or marks<70:
    print(f"{a} you are in elite")
elif marks>50:
     print(f"{a} you are pass")
else:
    print(f"{a} you are fail")"""


#fizzbuzz

"""a=[]
b=int(input("enter the values "))
for i in range(b):
    if i%3==0 and i%5==0:
        a.append("fizbizz")
    elif i%3==0:
        a.append("fizz")
    elif i%5==0:
        a.append("buzz")
    else:
        a.append(i)
print(a)"""



# sum of mod 5

"""a=[1,3,12,59,25,90,37,100]

b=0
for i in a:
    if i%5==0:
        b=b+i
print("the sum of odd no is ", b)"""


#sum of odd no

"""a=[1,3,12,59,25,90,37,100]

b=0
for i in a:
    if i%2!=0:
        b=b+i
print("the sum of odd no is ", b)"""


#find largest no

"""a=[1,3,12,59,25,900,37,100]
b=a[0]

for i in a:
    if i>b:
        b=i
print(b)"""


#Rainbow circle using python

"""import turtle

t=turtle.Turtle()
t.speed(50)
colors=['red','orange','yellow','green','blue','indigo','violet','gray','pink','ivory','silver','navy blue']
turtle.bgcolor('black')
for i in range(36):
    t.color(colors[i % 12])
    t.circle(100)
    t.right(10)
turtle.done()"""


#Network graph using pthon

"""import networkx as nx
import matplotlib.pyplot as plt

G=nx.Graph()
G.add_nodes_from(["A", "B", "C", "D", "E"])

edges=[("A","B"),("A","C"),("B","C"),("B","D"),("C","E"),("E","A"),("D","C")]
G.add_edges_from(edges)

plt.figure(figsize=(8,6))
nx.draw(G, with_labels=True, node_color="yellow", node_size=1000, edge_color="gray", font_size=16, font_weight="bold")
plt.title("network graph using python")
plt.show()"""


#nested loops

"""for i in range(0,3):
    for j in range(0,3):
        print(i,j, end=" ")
    print()"""
   

"""for i in range(0,9):
    for j in range(0,i):
        print("*", end=" ")
    print()"""


"""sums=[1,2,3,4,5]
b= sums[0]
for i in sums:
    if i>b:
        b=i
print(b)"""


"""a=[1,2,3,4,5]
b=0
c=0
for i in a:
    if i%2==0:
       b=b+i
    else:
        c=c+i
print("sum of odd numbers are", c)
print("sum of even numbers are", b)"""


"""nums=[1,2,3,4,5]

for i in nums:
    a=i*i
    print(a)"""


    
   

"""a=[1,2,3]
b=a[0]
for i in a:
    if i>b:
        b=i
print(b)"""


#factorial

"""n=int(input("enter the value "))
fact=1
for i in range(1,n+1):
    fact=fact*i
    print(fact)"""

setA = {1,2,3,4,5}
setB = {5,6,7,8,9,10}


"""unionset= setA.union(setB)
print("union set is",unionset)


intersectionset = setA.intersection(setB)
print("intersection set is", intersectionset)


differenceA = setA.difference(setB)
print("the difference A is", differenceA)

differenceB = setB.difference(setA)
print("the difference B is", differenceB)


diff_update= setA.difference_update(setB)
print("difference_update is",diff_update)


intersectionupdate = setA.intersection_update(setB)
print("intersection_update is", intersectionupdate)



sym_diff = setA.symmetric_difference(setB)
print("the symmetric_difference is", sym_diff)


sym_diff_update= setA.symmetric_difference_update(setB)
print("symmetric_difference_update is",sym_diff_update)



setA.difference_update(setB)
print("After difference_update, setB is:", setA)


setA.intersection_update(setB)
print("After intersection_update, setA is:", setA)"""



#leap year

"""a=int(input("enter the value "))
if a%4==0:
    print("leap year")
else:
    print("not leap year")"""


"""a=[]
b=int(input("enter values "))
a.append(b)

if a>50:
    print("pass")
else:
    print("fail")"""

#to find largest number in array via user input


"""b1=int(input("enter the number of values "))
values = []
b=0
for i in range(b1): 
    val = int(input(f"Enter value {i + 1}: "))
    values.append(val)
print("You entered:", values)
for j in values:
    if j>b:
        b=j
print("the largest number is ",b)"""



"""def addtwo(a,b=100):

    c=a+b
    print(c)

a=int(input("enter the value 1 "))


addtwo(a)"""


"""def person(fname,lname):
    print(fname,lname)

person(fname="getin",lname="tech")"""


"""def addn(a,b):
    c=a+b
    return c

a=int(input("enter the value 1 "))
b=int(input("enter the value 2 "))

result=addn(a,b)



def addn2(result,d):
    f=result+d
    print(f)

d=int(input("enter the value 3"))
addn2(result,d)"""


#find the sum of odd & even numbers using function

"""def addno():

    mylist1=[]
    c=0
    d=0

    a=int(input("enter the value: "))

    for i in range(a+1):
        n=int(input(f"enter the number {i+1} : "))
        mylist1.append(n)
    


    for i in mylist1:
        if i%2==0:
            c=i+c
        else:
            d=i+d
    print("the sum of even numbers : ", c)
    print("the sum of odd numbers: ", d)

addno()"""

#find the largest number using function

"""def large():
    a=[]
    b=0
    mylist=int(input("enter the value")) 

    for i in range(mylist+1):
        n=int(input(f"enter the number {i+1} "))
        a.append(n)


    for i in a:
        if i>b:
            b=i
    print("the largest number is ", b)

large()"""
      
#union, differnce, intersection using function

"""def setof():

    seta={1,2,3,4,5,6}
    setb={6,7,8,4,9,10}

    union1=seta.union(setb)
    print("the union of set is : ",union1)

    intersection1=seta.intersection(setb)
    print("the intersection of set is : ",intersection1)

    differenceA=seta.difference(setb)
    print("the Diff A is : ", differenceA)

    diffB=setb.difference(seta)
    print("the diff B is : ", diffB)

setof()"""


# leap year using function

"""def leap():

    a=int(input("enter the year "))
    if a%4==0:
        print(f"{a} is leap year")
    else:
        print(f"{a} is not leap year")

leap()"""

# square of number using function

    
"""def square():

    mylist=[]
    a=int(input("enter the value : "))
    for i in range(a):
        b=int(input(f"enter the number {i+1} : "))
        mylist.append(b)

    for j in mylist:
        c= j * j
        print(c)
    

square()"""


#fizzbuzz using function

"""def fizzbuzz():
    b=[]
    a=int(input("enter the value"))
    for i in range(a+1):
        if i%3==0 and i&5==0:
            b.append("fizzbuzz")
        elif i%3==0:
            b.append("fizz")
        elif i%5==0:
            b.append("buzz")
        else:
            b.append(i)
    print(b)

fizzbuzz()"""


"""n = int(input("enter the value"))

rem=0

while(n>0):
    div = n%10
    rem= rem*10+div
    n=n//10
print(rem)"""


"""def gen():
    a=[1,2,3,4,5,6]
    b=a[0]
    for i in a:
        if i>b:
            b=i
    yield b

for i in gen():
    print(i)"""


"""f1=open("myfile2.txt","w+")
f1.write("balaji \n")
f2=["welcome"," ","to"," ","spyder"]
f1.writelines(f2)
f1.close()

f3=open("myfile2.txt","r")
print(f3.read())
f3.close()

    class goa():
    def __init__(self,name):
        self.name= name

    def decide_act(self,activity):
        if activity=="party":
            print("lets go party")
        elif activity=="beach":
            print("lets go beach")
        else:
            print("go out from goa")

      
n=input("enter the name ")
activity=input("What do you want to do? (party/beach): ")


a=goa(n)
print(a.name)
a.decide_act(activity)


class person():
    def __init__(self,name,age,color,height,weight):
        self.name=name
        self.age=age
        self.color=color
        self.height=height
        self.weight=weight
    
    def eating(self):
        print("he is eating")
    def play(self):
        print("he is playing football")
    def watch(self):
        print("he is watching tv")
    def sleep(self):
        print("he is sleeping")




class student(person):
    def __init__(self,name,age,color,height,weight,rollno,section,marks):
        self.rollno=rollno
        self.section=section
        self.marks=marks
        super().__init__(name,age,color,height,weight)
        
    def studing(self):
        print("now he is studing")



n=input("enter your name ")
a=int(input("enter your age "))
c=input("enter your color ")
h=int(input("enter your height "))
w=int(input("enter your weight "))
r=int(input("enter your rollno "))
s=input("enter your section ")
m=int(input("enter your marks "))

obj=student(n,a,c,h,w,r,s,m)
print(f"Student Name: {obj.name}")
print(f"Roll Number: {obj.rollno}")
print(f"Section: {obj.section}")
print(f"Marks: {obj.marks}")

obj.eating()
obj.play()
obj.studing()"""





from abc import ABC

class computer(ABC):
    @abstractmethod
    def processor(self):
        print("i am processor")

class laptop(computer):
    def processor(self):
        print("pc")


obj=laptop()
obj.processor()














