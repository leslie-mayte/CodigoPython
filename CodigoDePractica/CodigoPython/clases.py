#Una clase es como un plano para crear objetos. Un objeto tiene propiedades y metodos 
#create a class
clase cliente(Usuario):
  #Constructor (funcion que corre cuando haces una instanciacion de u)
  def __init__ (self, nombre, email, edad):
      self.nombre = nombre
      self.email = email
      self.edad = edad
      self.saldo = 0

  def saludos(self,saldo):
      self.saldo=saldo
  def saldo(self):
      return "Me llamo {0} y tengo {1}".format(self.nombre,self.edad)


#extender la clase Usuario
Leslie = Usuario("Leslie Badillo","lesliemaytebad@gmail.com",18)
print(type(Leslie))
print(Leslie.nombre)
print(Leslie.saludos(100))

Leslie.tengo_cumple()
print(Leslie.saludos())

print("-----------------")

#Init un Cliente
Leslie_usuario = Usuario("Rufina Madrid","rufina@yahoo.com",2)
Leslie_cliente =  Cliente("Rufina Madrid","rufina@yahoo.com",2)
Leslie_cliente.establecer_saludos(5e10)
print(Rufina_cliente.saludos())
print(Rufina_usuario.saludos())
