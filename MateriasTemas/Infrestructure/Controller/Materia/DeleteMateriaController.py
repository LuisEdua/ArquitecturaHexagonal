from MateriasTemas.Application.UseCase.MateriaUseCase.DeleteMateriaUseCase import DeleteMateriaUseCase
from MateriasTemas.Dominio.Port.MateriaPort import MateriaPort
from typing import Any
from flask import jsonify

class DeleteMateriaController:
    def __init__(self, repository: MateriaPort):
        self._useCase = DeleteMateriaUseCase(repository)

    def run(self, id):
        return jsonify(self._useCase.run(id))