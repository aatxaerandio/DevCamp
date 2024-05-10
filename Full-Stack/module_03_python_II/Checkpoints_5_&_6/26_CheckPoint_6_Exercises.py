# Ejercicio práctico Python

"""
Cree una clase de Python llamada Usuario que use el método init y 
cree un nombre de usuario y una contraseña. Crea un objeto usando la clase.
"""

# crear la clase Usuario con el método init y los atributos nombre y contraseña.

class Usuario:
  def __init__(self, nombre, contraseña):
    self.nombre = nombre
    self.contraseña = contraseña

usuario = Usuario("Aitor", "PSW_1234")      # Crear un objeto de la clase Usuario.

#Acceder a los atributos del objeto:

print(f"Bienvenido! Tu usuario es {usuario.nombre} y tu contraseña {usuario.contraseña}")




