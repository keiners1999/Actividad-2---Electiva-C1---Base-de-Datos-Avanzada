"""
        ++++++++++++++++++
        |MANEJO DE LISTAS|
        ++++++++++++++++++
"""
def lista():
    lista1 =[]
    

    listaconelementos= [25, 2500000, "Dilan Ramirez", "Estudiante ing.sistemas", True, [" 9 Semestre", 2022]]
    
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

    

    listaconelementos.remove("Estudiante ing.sistemas") 
def main():
    lista()

if __name__ == "__main__":
    main()






if __name__ == "__main__":
    main()