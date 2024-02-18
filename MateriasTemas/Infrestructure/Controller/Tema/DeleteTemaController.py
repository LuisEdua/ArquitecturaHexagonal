from MateriasTemas.Application.UseCase.TemaUseCase.DeleteTemaUseCase import DeleteTemaUseCase
from MateriasTemas.Dominio.Port.TemaPort import TemaPort
from typing import Any
from flask import jsonify

class DeleteTemaController:
    def __init__(self, repository: TemaPort):
        self._useCase = DeleteTemaUseCase(repository)

    def run(self, id):
        return jsonify(self._useCase.run(id))