from MateriasTemas.Dominio.Port.MateriaPort import MateriaPort
from typing import Any
from MateriasTemas.Infrestructure.Controller.DTOS.MateriaResponse import MateriaResponse


class ListMateriasUseCase:
    def __init__(self, repository: MateriaPort):
        self._repository = repository

    def run(self) -> Any:
        materias = [MateriaResponse().dicts(materia) for materia in self._repository.list()]
        return {"message": "Materias found", "data": materias, "status": "Succes",
                "status code": 200}

