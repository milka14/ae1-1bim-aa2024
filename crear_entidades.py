from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, Integer, String
# se importa el engine
from base_datos import engine


# se crea la clase llamada Base que permite definir las clases bajo las
# características de SQLAlchemy
Base = declarative_base()

# Se crea la una entidad llamada Autor, que hereda
# de Base
class comedoresLocales (Base):
    __tablename__ = 'comedoresLocales' # El nombre de la entidad en sqlite
    # Se definen los atributos
    id = Column(Integer, primary_key=True) # este atributo es entero y
                                        # se lo considera como llave
                                        # primaria
    nombreLocal = Column(String) # atributo de tipo String
    ubicacion = Column(String)
    capacidad = Column(String)
    numeroMesa = Column(Integer)

    def __str__(self):
        return "%s %s %s %s" % (self.nombreLocal, self.ubicacion, self.capacidad,
        self.numeroMesa)
    
class centroDeportivos (Base):
    __tablename__ = 'centroDeportivos' # El nombre de la entidad en sqlite
    # Se definen los atributos
    id = Column(Integer, primary_key=True) # este atributo es entero y
                                        # se lo considera como llave
                                        # primaria
    nombreCentro = Column(String) # atributo de tipo String
    ubicacionCentro = Column(String)
    tamaño = Column(String)
    capacidadCentro= Column(Integer)

    def __str__(self):
        return "%s %s %s %s" % (self.nombreCentro, self.ubicacionCentro, self.tamaño,
        self.capacidadCentro)
     
  
# Sentencia que permite crear o migrar las clases en Python al
# gestor de base de datos, expresado en el engine.
Base.metadata.create_all(engine)
