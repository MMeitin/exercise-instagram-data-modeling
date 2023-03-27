import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class Usuario(Base):
    __tablename__ = 'usuario'
    id = Column(Integer, primary_key=True)
    nombre_de_usuario = Column(String(250), nullable=False)
    correo_electronico = Column(String(250), nullable=False)
    contrasena = Column(String(250), nullable=False)
    nombre_completo = Column(String(250), nullable=False)
    fecha_de_nacimiento = Column(DateTime, nullable=False)
    biografia = Column(String(250))

class Publicacion(Base):
    __tablename__ = 'publicacion'
    id = Column(Integer, primary_key=True)
    id_usuario = Column(Integer, ForeignKey('usuario.id'))
    descripcion = Column(String(250))
    ubicacion = Column(String(250))
    fecha_y_hora_de_publicacion = Column(DateTime)

class Comentario(Base):
    __tablename__ = 'comentario'
    id = Column(Integer, primary_key=True)
    id_publicacion = Column(Integer, ForeignKey('publicacion.id'))
    id_usuario = Column(Integer, ForeignKey('usuario.id'))
    texto_del_comentario = Column(String(250))

class MeGusta(Base):
    __tablename__ = 'megusta'
    id = Column(Integer, primary_key=True)
    id_publicacion = Column(Integer, ForeignKey('publicacion.id'))
    id_usuario = Column(Integer, ForeignKey('usuario.id'))

    # Un usuario puede tener muchas publicaciones, pero una publicación solo puede pertenecer a un usuario. Por lo tanto, la tabla Publicación tiene una clave foránea que hace referencia a la tabla Usuario.

    # Una publicación puede tener muchos comentarios, pero un comentario solo puede pertenecer a una publicación. Por lo tanto, la tabla Comentario tiene una clave foránea que hace referencia a la tabla Publicación.

    # Una publicación puede tener muchos “Me gusta”, pero un “Me gusta” solo puede pertenecer a una publicación. Por lo tanto, la tabla MeGusta tiene una clave foránea que hace referencia a la tabla Publicación.

    # Un usuario puede hacer muchos comentarios y dar muchos “Me gusta”, pero un comentario o “Me gusta” solo puede pertenecer a un usuario. Por lo tanto, las tablas Comentario y MeGusta tienen claves foráneas que hacen referencia a la tabla Usuario.

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
