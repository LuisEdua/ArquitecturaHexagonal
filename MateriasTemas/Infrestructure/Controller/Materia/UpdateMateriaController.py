from MateriasTemas.Application.UseCase.MateriaUseCase.UpdateMateriaUseCase import UpdateMateriaUseCase
from MateriasTemas.Dominio.Port.MateriaPort import MateriaPort
from typing import Any
from flask import jsonify


class UpdateMateriaController:
    def __init__(self, repository: MateriaPort):
        self._useCase = UpdateMateriaUseCase(repository)

    def run(self, id, request) -> Any:
        return jsonify(self._useCase.run(id, request.get_json())), 200