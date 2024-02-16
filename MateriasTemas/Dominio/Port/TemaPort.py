from abc import ABC, abstractmethod
from MateriasTemas.Dominio.Entity.Tema import Tema
from typing import Any


class TemaPort(ABC):
    @abstractmethod
    def create(self, tema: Tema) -> Any: pass

    @abstractmethod
    def update(self, id: str, status: bool) -> Any: pass

    @abstractmethod
    def delete(self, id: str) -> Any: pass

    @abstractmethod
    def list(self) -> Any: pass

    @abstractmethod
    def find(self, id: str) -> Any: pass
