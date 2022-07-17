singers = list(("Freddie Mercury", "Robert Plant", "Jim Morrison"))
numbers = [1, 2, 3, 8, 9, 5, 4]

#Ordenar Listas
print("\n\t\t ########## Ordenar Listas ##########")
print(numbers)
numbers.sort()
print(numbers)

# Agregar elementos a listas
print("\n\t\t ######### Agregar Elementos #########")
singers.append("Bon Jovi")
singers.insert(1, "John Lennon")
print(singers)

# Eliminar elementos a listas
print("\n\t\t ######### Eliminar Elementos #########")
singer = singers.pop(1)
singers.remove("Bon Jovi")
print(singers)

# Ordenar elementos inversamente a listas
print("\n\t\t ######## Ordenar Inversamente ########")
print(numbers)
numbers.reverse()
print(numbers)

# Buscar elemento en listas
print("\n\t\t ########## Buscar Elementos ##########")
print("Freddie Mercury" in singers)

# Contar elemento en listas
print("\n\t\t ########## Contar Elementos ##########")
print(singers)
print(len(singers))

# Cuantas veces aparece un elemento
print("\n\t\t ####### Número De Repeticiones #######")
numbers.append(9)
print(numbers.count(9))

# Conseguir indice de un elemento
print("\n\t\t ####### Obtener Indice Elemento ######")
print(singers.index("Robert Plant"))

# Unir listas
print("\n\t\t ############ Unir Listas #############")
singers.extend(numbers)
print(singers)