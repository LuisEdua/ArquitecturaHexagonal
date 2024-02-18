from MateriasTemas.Dominio.Entity.Tema import Tema
from MateriasTemas.Dominio.Port.TemaPort import TemaPort
from typing import Any
from MateriasTemas.Infrestructure.Controller.DTOS.TemaResponse import TemaResponse


class CreateTemaUseCase:
    def __init__(self, repository: TemaPort):
        self._repository = repository

    def run(self, data) -> Any:
        tema = Tema(data["nombre"], data["status"], data["id_materia"])
        tema_created = self._repository.create(tema)
        return {"Messsage": "Tema creada exitosamente", "data": TemaResponse().dict(tema_created), "status": "Succes",
                "status code": 200}
