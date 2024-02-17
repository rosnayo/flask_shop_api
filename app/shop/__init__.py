from flask import Blueprint,jsonify

shop = Blueprint('shop',__name__,url_prefix='/')

from .resources import (
    categoria,marca,producto
)

@shop.route('/')
def index():
    context = {
        'message':'prueba de endpoint'
    }
    return jsonify(context)
    