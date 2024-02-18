from MateriasTemas.Dominio.Port.TemaPort import TemaPort
from typing import Any
from MateriasTemas.Infrestructure.Controller.DTOS.TemaResponse import TemaResponse

class UpdateTemaUseCase:
    def __init__(self, repository: TemaPort):
        self._repository = repository

    def run(self, id, data) -> Any:
        tema = self._repository.update(id, data['status'])
        return {"Messsage": "Tema creada exitosamente", "data": TemaResponse().dict(tema), "status": "Succes",
                "status code": 200}
