import uuid


class Tema:
    def __init__(self, nombre:str, status:bool, id_materia: str):
        self.id = uuid.uuid4()
        self.nombre = nombre
        self.status = status
        self.materia = id_materia
