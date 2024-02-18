from MateriasTemas.Application.UseCase.MateriaUseCase.CreateMateriaUseCase import CreateMateriaUseCase
from MateriasTemas.Dominio.Port.MateriaPort import MateriaPort
from typing import Any
from flask import jsonify


class CreateMateriaController:
    def __init__(self, repository: MateriaPort):
        self._useCase = CreateMateriaUseCase(repository)

    def run(self, request) -> Any:
        return jsonify(self._useCase.run(request.get_json())), 200
