import uuid


class Materia:
    def __init__(self, nombreMateria:str, status:bool, carrera:str):
        self.id = uuid.uuid4()
        self.nombreMateria = nombreMateria
        self.status = status
        self.carrera = carrera
