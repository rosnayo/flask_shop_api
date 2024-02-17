from flask_restful import Resource,Api
from flask import request
from .. import auth
from ..models import Usuario
from ..schemas import UsuarioSchema

from werkzeug.security import(
    generate_password_hash,
    check_password_hash
)

from flask_jwt_extended import (
    create_access_token,
    jwt_required
)

api = Api(auth)

class UsuarioResource(Resource):

    def post(self):
        data = request.get_json()
        password = data['password']
        password_hash = generate_password_hash(password)
        usuario = Usuario()
        usuario.email = data['email']
        usuario.password = password_hash
        usuario.save()

        data_schema = UsuarioSchema()

        context = {
            'status':True,
            'message':'usuario registrado',
            'content':data_schema.dump(usuario)
        }

        return context

        
    @jwt_required()
    def get(self):
        data = Usuario.get_all()
        data_schema = UsuarioSchema(many=True)
        context = {
            'status':True,
            'message':'listado de usuarios',
            'content':data_schema.dump(data)
        }
        return context

class AuthenticationResource(Resource):

    def post(self):
        try:
            data = request.get_json()
            email = data['email']
            password = data['password']
            usuario = Usuario.get_by_email(email)
            if not usuario:
                context = {
                    'status':False,
                    'message':'no se encontro usuario con ese email'
                }
                return context,404

            is_password_checked = check_password_hash(usuario.password,
                                                      password)
            
            if is_password_checked:
               token = create_access_token(identity=usuario.id)
               context = {
                    'status':True,
                    'content':token
               }
               return context,201
            else:
                context = {
                    'status':False,
                    'message': 'contraseña incorrecta'
                }
                return context,400
        except Exception as e:
            context = {
                'status':False,
                'message':str(e)
            }

            return context,500

api.add_resource(UsuarioResource,'/user')
api.add_resource(AuthenticationResource,'/login')