#List is a collention which is ordered and changable.Allows duplicate

#Create a list, 1st way to do it
numbers = [1,2,3,4,5]
fruits = ["apple","orange","grapes","pears"]
#Create a list, use a constructor
numbers2 = list((1,2,3,4,5))
print(numbers,fruits)

#Get a value of a list
print(fruits[0])

#Get length
print(len(fruits))

#Append to the list
fruits.append("Mangos")
