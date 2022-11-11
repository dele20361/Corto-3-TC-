# Teoria de la computacion 
# Corto No.3 
# Paola de Leon 20361
# Angel Carrera 200133
# Paola Contreras 20213
# Cristian Aguirre 20231


#Ejercicio No.1, ordernar por medio de una key la lista de diccionarios
D = [
    {"make": "Nokia",   "model": 216, "color": "Black"},
    {"make": "Apple",   "model": 2,   "color": "Silver"}, 
    {"make": "Huawei",  "model": 50,  "color": "Gold"}, 
    {"make": "Samsung", "model": 7,   "color": "Blue"}
    ]

print (sorted(D, key = lambda i:i['make']))


#Ejercicio No.2, Potencia de una lista

listpower = lambda x,y: [i**y for i in x]

print(listpower([2,3,5,7,11,13],2))

print(listpower([1, 2, 3, 4, 5, 6, 7, 8, 9, 10],3))

#Ejercicio No.3, Calcular la Transpuesta de una Matriz

#Ejercicio No.4, Reverso de una lista de strings

listreverse = lambda x: [i[::-1] for i in x]

print(listreverse(['abc','def','ghi']))
print(listreverse(['rojo', 'verde', 'aZul', 'Blanco', 'negro'],))

#Ejercicio No.5, Eliminar elementos de una lista dada


