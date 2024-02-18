from sqlalchemy import Column, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship, backref
from Database.MySQL import Base
from .Materia import Materia

class Tema(Base):
    __tablename__ = 'temas'
    id = Column(String(36), primary_key=True)
    nombre = Column(String(36), nullable=False)
    status = Column(Boolean, nullable=False)
    materia_id = Column(String(36), ForeignKey('materias.id'))
    materia = relationship(Materia, backref=backref('temas', uselist=True))
