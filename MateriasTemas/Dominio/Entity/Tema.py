import uuid
from MateriasTemas.Dominio.Entity.Materia import Materia


class Tema:
    def __init__(self, nombre:str, status:str, materia:Materia):
        self.id = uuid.uuid4()
        self.nombre = nombre
        self.status = status
        self.materia = materia
