from MateriasTemas.Application.UseCase.TemaUseCase.UpdateTemaUseCase import UpdateTemaUseCase
from MateriasTemas.Dominio.Port.TemaPort import TemaPort
from typing import Any
from flask import jsonify


class UpdateTemaController:
    def __init__(self, repository: TemaPort):
        self._useCase = UpdateTemaUseCase(repository)

    def run(self, id, request) -> Any:
        return jsonify(self._useCase.run(id, request.get_json())), 200
