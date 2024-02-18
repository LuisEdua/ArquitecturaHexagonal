from MateriasTemas.Application.UseCase.MateriaUseCase.ListMateriasUseCase import ListMateriasUseCase
from MateriasTemas.Dominio.Port.MateriaPort import MateriaPort
from typing import Any
from flask import jsonify

class ListMateriasController:
    def __init__(self, repository: MateriaPort):
        self._useCase = ListMateriasUseCase(repository)

    def run(self):
        return jsonify(self._useCase.run())
