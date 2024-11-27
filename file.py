"""f1=open("myfile.txt","w+")
l2=["balaji \n","hari \n"]
f1.writelines(l2)
f1.write("my  name is balaji")
f1.close()

f2=open("myfile.txt","r")

print(f2.read())
f2.close()"""


f1=open("myfile2.txt","w+")
f1.write("hello \n")
f2=["hello","welcome","to","spyder"]
f1.writelines(f2)
f1.close

f3=open("myfile2.txt","r")
print(f3.read())
f3.close()