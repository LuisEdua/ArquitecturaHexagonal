from MateriasTemas.Dominio.Port.MateriaPort import MateriaPort
from typing import Any
from MateriasTemas.Infrestructure.Controller.DTOS.MateriaResponse import MateriaResponse


class DeleteMateriaUseCase:
    def __init__(self, repository: MateriaPort):
        self._repository = repository

    def run(self, id):
        self._repository.delete(id)
        return {"Message": "Deleted Materia", "status": "Success", "status code": 200}
