from flask_restful import Resource,Api
from flask import request
from .. import shop
from ..models import Producto
from ..schemas import ProductoSchema

from decouple import config

api = Api(shop)

import cloudinary
import cloudinary.uploader         
cloudinary.config( 
  cloud_name = config('CLOUDINARY_CLOUD_NAME'), 
  api_key = config('CLOUDINARY_API_KEY'), 
  api_secret = config('CLOUDINARY_API_SECRET') 
)

class ProductoResource(Resource):

    def post(self):
        data = request.get_json()
        nombre = data['nombre']
        precio = data['precio']
        imagen = data['imagen']
        categoria_id = data['categoria_id']
        marca_id = data['marca_id']

        producto = Producto(nombre,precio,imagen,
                            categoria_id,marca_id)

        producto.save()
        print(producto)
        data_schema = ProductoSchema()
        context = {
            'status':True,
            'content':data_schema.dump(producto)
        }

        return context

    def get(self):
        data = Producto.get_all()
        print(data)
        data_schema = ProductoSchema(many=True)
        context = {
            'status':True,
            'content':data_schema.dump(data)
        }

        return context

class ProductoDetailResource(Resource):

    def get(self,id):
        producto = Producto.get_by_id(id)
        data_schema = ProductoSchema()
        context = {
            'status':True,
            'content':data_schema.dump(producto)
        }
        return context

    def put(self,id):
        data = request.get_json()
        nombre = data['nombre']
        precio = data['precio']
        descripcion = data['descripcion']
        imagen = data['imagen']

        producto = Producto.get_by_id(id)
        producto.nombre = nombre
        producto.precio = precio
        producto.descripcion = descripcion
        producto.imagen = imagen
        producto.save()

        data_schema = ProductoSchema()

        context = {
            'status':True,
            'content':data_schema.dump(producto)
        }

        return context

    def delete(self,id):
        producto = Producto.get_by_id(id)
        producto.delete()

        data_schema = ProductoSchema()

        context = {
            'status':True,
            'message':"Producto Eliminado",
            'content':data_schema.dump(producto)
        }

        return context

class ProductoImageUpload(Resource):
    
    def post(self):
        if 'imagen' not in request.files:
            context = {
                'status':False,
                'message':'no se encontro ninguna imagen'
            }
            return context,400

        producto_imagen = request.files['imagen']
        try:
            upload_result = cloudinary.uploader.upload(producto_imagen)
            print(upload_result)
            url_imagen = upload_result['secure_url']

            context = {
                'status':True,
                'content':url_imagen
            }

            return context,200

        except Exception as e:
            context = {
                'status':False,
                'message':str(e)
            }

            return context,500

api.add_resource(ProductoResource,'/producto')
api.add_resource(ProductoDetailResource,'/producto/<id>')
api.add_resource(ProductoImageUpload,'/producto/image/upload')