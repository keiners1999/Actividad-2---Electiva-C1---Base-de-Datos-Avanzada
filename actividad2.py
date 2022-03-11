"""
        ++++++++++++++++++
        |MANEJO DE LISTAS|
        ++++++++++++++++++
"""
def lista():
    lista1 =[]
    

    listaconelementos= [25, 2500000, "Dilan Ramirez", "Estudiante ing.sistemas", True, [" 9 Semestre", "pediodo 2022"]]
    
    print("Motrando elemetos con el ciclo for ")
    for i in range(len(listaconelementos)): 
        print(listaconelementos[i])
    print("\n\n")
    
    print("Mostrando elementos con el ciclo while")
    j=0
    while j < (len(listaconelementos)):
        print(listaconelementos[j])
        j+=1  

    print("\n")
    print("Imprimir una lista que está dentro de otra")
    print(listaconelementos[-1][1])

    print("\n")
    print("mostrando elementos con saltos ")
    print("Elementos Pares\n")
    print(listaconelementos[0:len(listaconelementos):2])

    print("\nElementos Impares\n")
    print(listaconelementos[1:len(listaconelementos):2])

    print("\n")
    print("añadir un elemento al final")
    listaconelementos.append(["Sede maicao", "Mario Pelaez"])
    print(listaconelementos)

    print("\n")
    print("añadir un elemento en una posicion")
    listaconelementos.insert(2,"elemento añadido")
    print(listaconelementos)

    print("\n")
    print("Eliminar un elemento")
    listaconelementos.pop(2)
    print(listaconelementos)

    listaconelementos.remove("Estudiante ing.sistemas") 
def main():
    lista()

if __name__ == "__main__":
    main()






if __name__ == "__main__":
    main()