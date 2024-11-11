
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