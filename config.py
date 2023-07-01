class Config:
    '''
    Depuración y testing actívos para probar el proyecto
    con una base de datos y un servidor de prueba
    '''
    DEBUG = True
    TESTING = True
    # No censentimos a SQLA seguir la modificaciónes
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # Base de datos utilizata
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:'password'@localhost:3306/blog_db"


class ProductionConfig(Config):
    DEBUG = False


class DevelopmentConfig(Config):
    # Variable secreta para para la seguridad el na generación de tokens
    SECRET_KEY = "'secret key'"
    DEBUG = True
    TESTING = True

