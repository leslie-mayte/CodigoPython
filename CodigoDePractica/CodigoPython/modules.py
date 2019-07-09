#Un modulo es basicamente un archivo que contiene u conjuto de funciones para incluir a tu aplicacion.
import datetime
hoy = datetime.date.today()
print(hoy)

from datetime import date
hoy2 = date.today()
print(hoy2)

import time
estampatemporal = time()
print(estampatemporal)

import validador
from validador import validate_email
email = "prueba@gmail.com"
if validate_email(email):
  print("el correo esta bien escrito")
else:
  print("el correo esta mal escrito")

