#Un for loop es utilizado para iterar sobre una secuencia (puede ser una lista, directorio, un conjunto o un string)
#simple loop
people = ["Andres", "Alejandra", "Benito", "Jose"]
print("****Simple loop****")
for person in people: 
  print("Current Person: {0}".format(person))
#Break
print ("****Break loop****")
for person in people:
  if person == "Benito":
    break
  print("Current Person: {0}".format(person))

#Continue
print("****Continue loop****")
for person in people :
  if person == "Benito":
    continue
  print("Current Person: {0}".format(person))

print("****Range loop****")
range
for i  in range(len(people)):
  print(people[i])

for i in range (0,len(people)):
  print("Number: {0}".format(i))

#while loops: es hasta que se cumpla una condicion
count = 0
while count <= 10:
  print("count: {0}".format(count))
  count+=1
