print("Funciones creadas por el usuario")
# las funciones

def Mi_list():
    print("Lista")
    amigos = ["Iván", "Anahí", "Andrea"]
    for zyanya in amigos:
        print(zyanya)

def mi_tupla():
    print("\nTupla")
    planetas = ("Tierra","Marte","Jupiter")
    for mundos in planetas:
        print(mundos)

def mi_conj():
    print("\nConjunto")
    musica = {"Morat","Reik","Ela Taubert"}
    for canciones in musica:
        print(canciones)

def mi_dicc():
    print("\nDiccionario")
    Materias = {
        "Cálculo" : "Integral",
        "Ciencias" : "Y Tecnología",
        "Desarrollo" : "Web",
        "Conectividad" : "a BD"
    }
    print(Materias)

# Llamadas a funciones
Mi_list()
mi_tupla()
mi_conj()
mi_dicc()