from MateriasTemas.Dominio.Port.MateriaPort import MateriaPort
from typing import Any
from MateriasTemas.Infrestructure.Controller.DTOS.MateriaResponse import MateriaResponse


class FindMateriaUseCase:
    def __init__(self, repository: MateriaPort):
        self._repository = repository

    def run(self, id: str) -> Any:
        materia = self._repository.find(id)
        return {"message": "Materia found", "data": MateriaResponse().dicts(materia), "status": "Succes",
                "status code": 200}
