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
