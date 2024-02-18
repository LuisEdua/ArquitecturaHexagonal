from MateriasTemas.Infrestructure.Repository.Models.Materia import Materia


class MateriaResponse:
    def dicts(self, materia: Materia) -> dict:
        return {"id": materia.id, "name": materia.nombre_materia, "status": materia.status,
                "carrera": materia.carrera}
    