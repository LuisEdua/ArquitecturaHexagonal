from abc import ABC, abstractmethod
from typing import Any
from MateriasTemas.Dominio.Entity.Materia import Materia


class MateriaPort(ABC):
    @abstractmethod
    def create(self, materia:Materia) -> Any: pass

    @abstractmethod
    def update_status(self, id:str, status:bool) -> Any: pass

    @abstractmethod
    def delete(self, id:str) -> Any: pass

    @abstractmethod
    def list(self) -> Any: pass

    @abstractmethod
    def find(self, id:str) -> Any: pass
