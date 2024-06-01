"""
    Consultar información en una colección de MongoDB
    desde Python
"""
from enlace_base import client

# se obtiene la colección general (base de datos)

db = client.mongo001
coleccion = db.centrosDeportivos

# se usa método find_one con parámetros, a partir de la colección
print("Muestra un solo documento de la base de datos")
data_01 = coleccion.find_one({'nombreCentro':'club de Neon'})
print(data_01)


