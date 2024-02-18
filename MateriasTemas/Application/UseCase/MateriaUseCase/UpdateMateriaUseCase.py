from MateriasTemas.Dominio.Port.MateriaPort import MateriaPort
from typing import Any
from MateriasTemas.Infrestructure.Controller.DTOS.MateriaResponse import MateriaResponse


class UpdateMateriaUseCase:
    def __init__(self, repository: MateriaPort):
        self._repository = repository

    def run(self, id, data):
        materia = MateriaResponse().dicts(self._repository.update_status(id, data['status']))
        return {"Message": "Updated materia", "Materia": materia, "status": "Success", "status code": 200}
