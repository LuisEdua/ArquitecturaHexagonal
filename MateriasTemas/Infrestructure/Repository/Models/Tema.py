from sqlalchemy import Column, String, Boolean
from sqlalchemy.orm import relationship, backref
from Database.MySQL import Base
from Materia import Materia

class Tema(Base):
    __tablename__ = 'temas'
    id = Column(String(36), primary_key=True)
    name = Column(String(36), nullable=False)
    status = Column(Boolean, nullable=False)
    materia = relationship(Materia, backref=backref('temas', uselist=True))
