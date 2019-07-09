#helloworld AwA
print("hello word AwA")

#This is a small programe to practice python
"""
VARIABLES RULES
-Variable name are case sensitive (name and NAME are different)
-Must start whith a letter or an underscore
-Can have a number but can not start with one
"""
x=1	#int
y=2.5	#float
name="Leslie"	#string
is_cool=True	#bool

#miltiple assigment
x,y,name, is_cool=(1,2.5,"Leslie",True)

#Basic math
a=x+y

print(x,y,name,is_cool,a)

#chec the type 
print(type(x))

#cast, e.g. x to string

x= str(x)	#passing x
y= int(y)	#passing y
z= float(y)

print(type(y),y)
print(type(z),z)
