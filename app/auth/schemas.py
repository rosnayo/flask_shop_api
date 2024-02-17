from utils import ma
from marshmallow import fields

class UsuarioSchema(ma.Schema):
    class Meta:
        fields = ('id','email','is_admin')