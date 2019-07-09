#If/else son condicionales que se usan para decidir hacer algo basado en algo que es verdadero o falso
x=10
y=5

#Podemos usar operadores de comparacion (==,!=,>,<,>=,<=)
#simple if
if x>y:
	print("{0}es mas grande que {1}".format(x,y))
else x<y:
	print("{0}es mas grande que {x1}".format(y,x))
print("-------")

if x>y:
	print("{0}es mas grande que {1}".format(x,y))
	print(x)
elif x==y
	print("{0}es igual a {1}".format(x,y))
	print("x y y son iguales")
else:
	print("{0}es mas grande a {1}".format(y,x))
	print(y)

#if anidados
if x>2:
  if x<=10:
    print("{0}es mas grande que 2 e igual/menor a 10".format(x))
#una mejor forma de hacerlo: usar operadores logicos(and, or, not) se usaun para combinar condicionales

#and
if x>2 and x<=10:
  print("{0} es mas grande que 2 e igual/menor a 10".format(x))
#or
if x>2 or x<=10:
  print("{0}es mas grande que 2 e igual/menor a 10")
if not(x==y):
  print("{0} no es igual a {1}".format(x,y))

