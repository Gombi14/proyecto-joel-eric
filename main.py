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
                print(
                    "Nom d'usuari o contrasenya incorrectes. Intents restants: {}".format(
                        intents
                    )
                )
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
                    if (
                        username == stored_username
                        and hashlib.md5(password.encode()).hexdigest()
                        == stored_password
                    ):
                        return True
        # Si el usuario no existe, añadirlo al archivo
        with open("usuaris.txt", "a") as file:
            file.write(
                "{}|{}\n".format(username, hashlib.md5(password.encode()).hexdigest())
            )
        return False
    except FileNotFoundError:
        print("El fitxer d'usuaris no existeix.")
        return False

def mostrar_llibre(titol):
    try:
        with open("llibres.txt", "r", encoding="utf-8") as file:
            for line in file:
                if titol.lower() in line.lower():
                    print(line.strip().replace("|", "\t"))
                    return
        print("Llibre no trobat.")
    except FileNotFoundError:
        print("El fitxer de llibres no existeix.")
def mostrar_llibre(titol):
    try:
        with open("llibres.txt", "r", encoding="utf-8") as file:
            for line in file:
                if titol.lower() in line.lower():
                    print(line.strip().replace("|", "\t"))
                    return
        print("Llibre no trobat.")
    except FileNotFoundError:
        print("El fitxer de llibres no existeix.")


# Función para mostrar todos los libros
def mostrar_tots_els_llibres():
    try:
        with open("llibres.txt", "r", encoding="utf-8") as file:
            for line in file:
                print(line.strip().replace("|", "\t"))
    except FileNotFoundError:
        print("El fitxer de llibres no existeix.")


# Función para añadir un libro
def afegir_llibre():
    try:
        with open("llibres.txt", "a", encoding="utf-8") as file:
            titol = input("Introdueixi el títol del llibre: ")
            autor = input("Introdueixi l'autor/a del llibre: ")
            any_publicacio = input("Introdueixi l'any de publicació del llibre: ")
            genere = input("Introdueixi el gènere del llibre: ")
            isbn = input("Introdueixi l'ISBN del llibre: ")
            file.write(
                "{}|{}|{}|{}|{}\n".format(titol, autor, any_publicacio, genere, isbn)
            )
            print("Llibre afegit amb èxit.")
    except FileNotFoundError:
        print("El fitxer de llibres no existeix.")


# Función para eliminar un libro
def eliminar_llibre(titol):
    try:
        with open("llibres.txt", "r", encoding="utf-8") as file:
            lines = file.readlines()
        with open("llibres.txt", "w", encoding="utf-8") as file:
            for line in lines:
                if titol.lower() not in line.lower():
                    file.write(line)
        print("Llibre eliminat amb èxit.")
    except FileNotFoundError:
        print("El fitxer de llibres no existeix.")


# Función para editar un libro
def editar_llibre(titol_vell):
    try:
        with open("llibres.txt", "r", encoding="utf-8") as file:
            lines = file.readlines()

        found = False
        with open("llibres.txt", "w", encoding="utf-8") as file:
            for line in lines:
                parts = line.strip().split("|")
                if len(parts) == 5 and parts[0].lower() == titol_vell.lower():
                    found = True
                    print("Trobat el llibre:")
                    print(line.strip())
                    titol_nou = input("Introdueixi el nou títol del llibre: ")
                    autor_nou = input("Introdueixi el nou autor/a del llibre: ")
                    any_publicacio_nou = input(
                        "Introdueixi el nou any de publicació del llibre: "
                    )
                    genere_nou = input("Introdueixi el nou gènere del llibre: ")
                    isbn_nou = input("Introdueixi el nou ISBN del llibre: ")
                    file.write(
                        "{}|{}|{}|{}|{}\n".format(
                            titol_nou,
                            autor_nou,
                            any_publicacio_nou,
                            genere_nou,
                            isbn_nou,
                        )
                    )
                    print("Llibre editat amb èxit.")
                else:
                    file.write(line)

        if not found:
            print("Llibre no trobat.")
    except FileNotFoundError:
        print("El fitxer de llibres no existeix.")