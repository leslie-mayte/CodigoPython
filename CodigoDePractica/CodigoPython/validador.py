#Ejemplo de un modulo que esta por default en python
imoirt re #re es un modulo que esta por default en python
def validate_email(email):
  if len(email) > 7:
     return bool(re.match("^.+@(\[?)[a-zA-z0-9-.]+.([a-zA-Z]{2,3}|[0-9]{1,3})(}?)$",email))
