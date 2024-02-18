from MateriasTemas.Application.UseCase.TemaUseCase.ListTemaUseCase import ListTemaUseCase
from MateriasTemas.Dominio.Port.TemaPort import TemaPort
from typing import Any
from flask import jsonify


class ListTemasController:
    def __init__(self, repository: TemaPort):
        self._useCase = ListTemaUseCase(repository)

    def run(self) -> Any:
        return jsonify(self._useCase.run())
