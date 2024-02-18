from MateriasTemas.Dominio.Port.MateriaPort import MateriaPort
from MateriasTemas.Application.UseCase.MateriaUseCase.FindMateriaUseCase import FindMateriaUseCase
from typing import Any
from flask import jsonify


class FindMateriaController:
    def __init__(self, repository: MateriaPort):
        self._useCase = FindMateriaUseCase(repository)

    def run(self, id) -> Any:
        return jsonify(self._useCase.run(id))
