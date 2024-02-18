from MateriasTemas.Infrestructure.Repository.Models.Tema import Tema
from MateriasTemas.Infrestructure.Controller.DTOS.MateriaResponse import MateriaResponse


class TemaResponse:

    def dict(self, tema: Tema) -> dict:
        return {"id": tema.id, "name": tema.nombre, "status": tema.status,
                "materia": MateriaResponse().dicts(tema.materia)}
