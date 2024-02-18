from MateriasTemas.Application.UseCase.TemaUseCase.CreateTemaUseCase import CreateTemaUseCase
from MateriasTemas.Dominio.Port.TemaPort import TemaPort
from typing import Any
from flask import jsonify



class CreateTemaController:
    def __init__(self, repository: TemaPort):
        self._useCase = CreateTemaUseCase(repository)

    def run(self, request) -> Any:
        return jsonify(self._useCase.run(request.get_json())), 200
