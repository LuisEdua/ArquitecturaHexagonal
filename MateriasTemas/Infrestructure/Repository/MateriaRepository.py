from Database.MySQL import session_local, Base, engine
from MateriasTemas.Dominio.Entity.Materia import Materia
from MateriasTemas.Dominio.Port.MateriaPort import MateriaPort
from MateriasTemas.Infrestructure.Repository.Models.Materia import Materia as Entity


class MateriaRepository(MateriaPort):
    def __init__(self):
        Base.metadata.create_all(bind=engine)
        self._db = session_local()
    def create(self, materia: Materia) -> Entity:
        entity = Entity(id=materia.id, nombre_materia=materia.nombre_materia, status=materia.status, carrera=materia.carrera)
        self._db.add(entity)
        self._db.commit()
        return entity

    def update_status(self, id: str, status:bool) -> Entity:
        materia = self._db.query(Entity).filter(Entity.id == id).first()
        materia.status = status
        self._db.commit()
        return materia

    def delete(self, id: str):
        materia = self._db.query(Entity).filter(Entity.id == id).first()
        self._db.delete(materia)
        self._db.commit()

    def list(self) -> Entity:
        return self._db.query(Entity).all()

    def find(self, id: str) -> Entity:
        return self._db.query(Entity).filter(Entity.id == id).first()
