from MateriasTemas.Application.UseCase.TemaUseCase.FindTemaUseCase import FindTemaUseCase
from MateriasTemas.Dominio.Port.TemaPort import TemaPort
from typing import Any
from flask import jsonify



class FindTemaController:
    def __init__(self, repository: TemaPort):
        self._useCase = FindTemaUseCase(repository)

    def run(self, id) -> Any:
        return jsonify(self._useCase.run(id)), 200