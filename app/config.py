from decouple import config
class Config:
    # SQLALCHEMY_DATABASE_URI='mysql://root:12345678@localhost/db_shop_flask'
    # le indicamos que coja la variable global de .env para conectarse a la bd en la nube
    SQLALCHEMY_DATABASE_URI= config('MYSQL_ADDON_URI')
    SQLALCHEMY_TRACK_MODIFICATIONS=False
    JWT_SECRET_KEY='QWERTY123'