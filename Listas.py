"""
          MANEJO DE LISTAS
"""
def lista():
    lista1 =[]
    lista2=list()

    listaConElementos= [30, 2000000, "Keiners Barraza", "Estudiante", True, ["Semestre", 2022]]
    #print(listaConElementos)
    print("Recorriendo lista con for ")
    for i in range(len(listaConElementos)): 
        print(listaConElementos[i])
    print("\n\n")
    
    print("Recorriendo lista con while")
    j=0
    while j < (len(listaConElementos)):
        print(listaConElementos[j])
        j+=1  


    print("\n")
    print("Imprimir una lista que está dentro de otra")
    print(listaConElementos[-1][1])

#mostrar los elementos con saltos listaConElementos[Donde empieza : Donde termina : Salto]
    print("\n")
    print("mostrar los elementos con saltos ")
    print("Elementos Pares\n")
    print(listaConElementos[0:len(listaConElementos):2])

    print("\nElementos Impares\n")
    print(listaConElementos[1:len(listaConElementos):2])


    print("\n")
    print("Agregar un elemento al final de la lista")
    listaConElementos.append(["Sede Riohacha", "Miguel Soto"])
    print(listaConElementos)

    print("\n")
    print("Agregar un elemento en una posicionn de la lista")
    listaConElementos.insert(2,"elemento agregado")
    print(listaConElementos)

    print("\n")
    print("Eliminar elemento de la lista")
    listaConElementos.pop(2)
    print(listaConElementos)

    listaConElementos.remove("Estudiante")
def main():
    lista()

if __name__ == "__main__":
    main()