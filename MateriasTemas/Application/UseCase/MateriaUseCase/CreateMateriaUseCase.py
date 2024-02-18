from MateriasTemas.Dominio.Entity.Materia import Materia
from MateriasTemas.Dominio.Port.MateriaPort import MateriaPort
from typing import Any
from MateriasTemas.Infrestructure.Controller.DTOS.MateriaResponse import MateriaResponse


class CreateMateriaUseCase:
    def __init__(self, repository: MateriaPort):
        self._repository = repository

    def run(self, data) -> Any:
        materia = Materia(data['nombre'], data['status'], data['carrera'])
        materia_created = self._repository.create(materia)
        return {"Message": "Materia creada", "status": "Succes", "materia": MateriaResponse().dicts(materia_created),
                "status code": 200}

