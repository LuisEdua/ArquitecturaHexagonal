from sqlalchemy import Column, String, Boolean
from Database.MySQL import Base


class Materia(Base):
    __tablename__ = 'materias'
    id = Column(String(36), primary_key=True)
    nombre_materia = Column(String(255), nullable=False)
    status = Column(Boolean, nullable=False)
    carrera = Column(String(255), nullable=False)
