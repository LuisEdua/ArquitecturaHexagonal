from MateriasTemas.Dominio.Port.TemaPort import TemaPort
from typing import Any
from MateriasTemas.Infrestructure.Controller.DTOS.TemaResponse import TemaResponse

class ListTemaUseCase:
    def __init__(self, repository: TemaPort):
        self._repository = repository

    def run(self) -> Any:
        temas = [TemaResponse().dict(tema) for tema in self._repository.list()]
        return {"Messsage": "Tema creada exitosamente", "data": temas, "status": "Succes",
                "status code": 200}