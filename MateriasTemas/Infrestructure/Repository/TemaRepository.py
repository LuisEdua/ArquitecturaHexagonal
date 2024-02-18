from typing import Any
from MateriasTemas.Dominio.Port.TemaPort import TemaPort
from Database.MySQL import session_local, Base, engine
from MateriasTemas.Dominio.Entity.Tema import Tema
from MateriasTemas.Infrestructure.Repository.Models.Tema import Tema as Entity

class TemaRepository(TemaPort):
    def __init__(self):
        Base.metadata.create_all(engine)
        self._db = session_local()
    def create(self, tema: Tema) -> Entity:
        entity = Entity(id=tema.id, nombre=tema.nombre, materia_id=tema.materia, status=tema.status)
        self._db.add(entity)
        self._db.commit()
        return entity

    def update(self, id: str, status: bool) -> Entity:
        tema = self._db.query(Entity).filter(Entity.id == id).first()
        tema.status = status
        self._db.commit()
        return tema

    def delete(self, id: str):
        tema = self._db.query(Entity).filter(Entity.id == id).first()
        self._db.delete(tema)
        self._db.commit()

    def list(self) -> Entity:
        return self._db.query(Entity).all()

    def find(self, id: str) -> Any:
        return self._db.query(Entity).filter(Entity.id == id).first()
