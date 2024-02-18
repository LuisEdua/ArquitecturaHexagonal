from MateriasTemas.Infrestructure.Controller.Materia.CreateMateriaController import CreateMateriaController
from MateriasTemas.Infrestructure.Controller.Materia.DeleteMateriaController import DeleteMateriaController
from MateriasTemas.Infrestructure.Controller.Materia.FindMateriaController import FindMateriaController
from MateriasTemas.Infrestructure.Controller.Materia.ListMateriasController import ListMateriasController
from MateriasTemas.Infrestructure.Controller.Materia.UpdateMateriaController import UpdateMateriaController
from MateriasTemas.Infrestructure.Repository.MateriaRepository import MateriaRepository
from flask import Blueprint, request


materia_blueprint = Blueprint('materias', __name__)
repository = MateriaRepository()


@materia_blueprint.route("/", methods=['POST'])
def create_materia():
    return CreateMateriaController(repository).run(request)

@materia_blueprint.route("/<string:id>", methods=['GET'])
def get_materia(id):
    return FindMateriaController(repository).run(id)

@materia_blueprint.route("/", methods=['GET'])
def get_all():
    return ListMateriasController(repository).run()

@materia_blueprint.route("/<string:id>", methods=['PUT'])
def update_materia(id):
    return UpdateMateriaController(repository).run(id, request)

@materia_blueprint.route("/<string:id>", methods=['DELETE'])
def delete_materia(id):
    return DeleteMateriaController(repository).run(id)