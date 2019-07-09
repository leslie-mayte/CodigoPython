#Una funcion es un bloque de codigo que solo corre cuando se le llama. En python no usamos corchetes, usamos identaciones con tabs o space

#Crear la funcion, esta funcion no regresa solo imprime
def DecirHola (nombre=""):
  print("Hola {0}".format(nombre))

DecirHola("Leslie Mayte")

#Funcion que me regrese un valor
def hacersuma(num1, num2):
  total= num1 + num2
  return float(total)

hacersuma(2,3)
print(hacersuma(2,3),type(hacersuma(2,3)))

x=2
y=2
total= hacersuma(x,y)
print(total,type(total))



