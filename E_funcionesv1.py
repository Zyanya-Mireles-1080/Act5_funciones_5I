print("Manejo de funciones V!")
def hola_mundo():
    print("Hola aquí estoy dentro de la función")

def Mensa(msg):
    print(msg)

def EscribeNC(Nombre, Apellido):
    print(Nombre, Apellido)
    print(f"Tu nombre completo es {Nombre} {Apellido}")

def suma2numeros(n1,n2):
    s = n1+n2
    return f"La suma de {n1} + {n2} es de:",s

# llamando a la funcion
hola_mundo()

Mensa("Hola Whatsapp") # llama a Mensa con un 1 parametro
Mensa("El profe me sorprendió enviando mensajes") # llama a Mensa con otro parametro

EscribeNC("Zyanya","Mireles")

print("Funciones que regresan valores")
print(suma2numeros(7,3))
print(suma2numeros(15,45))
