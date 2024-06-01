"""
    Agregar información en una colección de MongoDB
    desde Python
"""
from enlace_base import client

# se obtiene la colección general (base de datos)

db = client.mongo001
coleccion = db.comedoresLocales

# conjunto de datos a guardar en la colección
# importante, aquí se usa la estructura de Python denominada diccionario
# proceso que agrega un solo documento
data_01 = {"nombre": "Luis", "apellido": "Valencia",
"nacionalidad":"ecuatoriana", "numero_publicaciones": 100}

coleccion.insert_one(data_01)

# proceso que agrega una lista de documentos
lista_comedoresLocales= [
{"nombreLocal": "menestra del negro", "ubicacion": "San Camilo", "numeroMesa":"20",
"capacidad": "grande"},
{"nombreLocal": "Cars Jr", "ubicacion": "Guayacan", "numeroMesa":"40",
"capacidad": "pequeño"}
]

coleccion.insert_many(lista_comedoresLocales)

db = client.mongo001
coleccion = db.centroDeportivos

# conjunto de datos a guardar en la colección
# importante, aquí se usa la estructura de Python denominada diccionario
# proceso que agrega un solo documento


# proceso que agrega una lista de documentos
lista_centroDeportivos= [
{"nombreCentro": "club de Neon", "ubicacionCentro": "Guayacan", "tamaño":"20",
"capacidadCentro": "grande"},
{"nombreCentro": "Club de Leones", "ubicacionCentro": "San Carlos", "tamaño":"30",
"capacidadCentro": "pequeño"}
]

coleccion.insert_many(lista_centroDeportivos)
