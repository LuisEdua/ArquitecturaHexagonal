from MateriasTemas.Dominio.Port.TemaPort import TemaPort
from typing import Any
from MateriasTemas.Infrestructure.Controller.DTOS.TemaResponse import TemaResponse


class DeleteTemaUseCase:
    def __init__(self, repository: TemaPort):
        self._repository = repository

    def run(self, id):
        self._repository.delete(id)
        return {"Message": "Deleted Tema", "status": "Success", "status code": 200}
