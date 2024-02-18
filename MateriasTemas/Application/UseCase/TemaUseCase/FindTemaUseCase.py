from MateriasTemas.Dominio.Port.TemaPort import TemaPort
from typing import Any
from MateriasTemas.Infrestructure.Controller.DTOS.TemaResponse import TemaResponse


class FindTemaUseCase:
    def __init__(self, repository: TemaPort):
        self._repository = repository

    def run(self, id) -> Any:
        tema = TemaResponse().dict(self._repository.find(id))
        return {"Messsage": "Tema creada exitosamente", "data": TemaResponse().dict(tema), "status": "Succes",
         "status code": 200}
