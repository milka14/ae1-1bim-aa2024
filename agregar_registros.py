from sqlalchemy.orm import sessionmaker
# se importa la clase(s) del
# archivo crear_entidades
from crear_entidades import comedoresLocales,centroDeportivos
# se importa el engine
from base_datos import engine


# Se crea una clase llamada Sessión,
# desde el generador de clases de SQLAlchemy
# sessionmaker.
Session = sessionmaker(bind=engine) # Se usa el engine
# Importante, se crea un objeto llamado session
# de tipo Session, que permite: permitir guardar, eliminar,
# actualizar y generar consultas a la base de datos.
session = Session()

# se crea un objetos de tipo Autor
local1 = comedoresLocales(nombreLocal="menestra del negro ", ubicacion ="San Camilo", capacidad="grande",
       numeroMesa="20")
local2 = comedoresLocales (nombreLocal="Cars Jr", ubicacion="Guayacan", capacidad="pequeño",
        numeroMesa="40")

      
# se crea un objetos de tipo Autor
centro1 = centroDeportivos (nombreCentro="Club de Leones", ubicacionCentro ="San Carlos", tamaño= "estadio",
       capacidadCentro="10")
centro2 = centroDeportivos (nombreCentro="Club de Neon", ubicacionCentro="Guayacan", tamaño="coliseo",
        capacidadCentro="100")

      
# se agrega los objetos de tipo Autor a la sesión
# a la espera de un commit
session.add(local1)
session.add(local2)

session.add(centro1)
session.add(centro2)

# se necesita confirmar los cambios que existan en la sessió
# se usar commit
session.commit()
