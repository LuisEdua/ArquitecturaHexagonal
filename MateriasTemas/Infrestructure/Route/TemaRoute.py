from MateriasTemas.Infrestructure.Controller.Tema.CreateTemaController import CreateTemaController
from MateriasTemas.Infrestructure.Controller.Tema.FindTemaController import FindTemaController
from MateriasTemas.Infrestructure.Controller.Tema.ListTemasController import ListTemasController
from MateriasTemas.Infrestructure.Controller.Tema.UpdateTemaController import UpdateTemaController
from MateriasTemas.Infrestructure.Controller.Tema.DeleteTemaController import DeleteTemaController
from MateriasTemas.Infrestructure.Repository.TemaRepository import TemaRepository
from flask import Blueprint, request

tema_blueprints = Blueprint('tema_blueprints', __name__)
repository = TemaRepository()

@tema_blueprints.route('/', methods=['POST'])
def create_tema():
    return CreateTemaController(repository).run(request)

@tema_blueprints.route('/<string:id>', methods=['GET'])
def get_tema(id):
    return FindTemaController(repository).run(id)

@tema_blueprints.route('/', methods=['GET'])
def get_all_tema():
    return ListTemasController(repository).run()

@tema_blueprints.route('/<string:id>', methods=['PUT'])
def update_tema(id):
    return UpdateTemaController(repository).run(id, request)

@tema_blueprints.route('/<string:id>', methods=['DELETE'])
def delete_tema(id):
    return DeleteTemaController(repository).run(id)
