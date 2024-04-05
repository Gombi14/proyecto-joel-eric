import hashlib

# Función para el inicio de sesión
def login():
   print("Benvingut a la biblioteca Can Casacuberta")
   intents = 3
   while intents > 0:
       username = input("Introdueixi el nom d'usuari: ")
       password = input("Introdueixi la contrasenya: ")
       # Comprobación del usuario y contraseña
       if verificar_credencials(username, password):
           return True
       else:
           intents -= 1
           if intents > 0:
               print("Nom d'usuari o contrasenya incorrectes. Intents restants: {}".format(intents))
           else:
               print("Ha superat el límit d'intents. Sortint del programa.")
               return False

# Función para verificar las credenciales del usuario
def verificar_credencials(username, password):
   try:
       with open("usuaris.txt", "r") as file:
           for line in file:
               parts = line.strip().split("|")
               if len(parts) == 2:
                   stored_username, stored_password = parts
                   if username == stored_username and hashlib.md5(password.encode()).hexdigest() == stored_password:
                       return True
       # Si el usuario no existe, añadirlo al archivo
       with open("usuaris.txt", "a") as file:
           file.write("{}|{}\n".format(username, hashlib.md5(password.encode()).hexdigest()))
       return False
   except FileNotFoundError:
       print("El fitxer d'usuaris no existeix.")
       return False