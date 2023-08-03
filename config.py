class Config:
    '''
    Depuración y testing activos para probar el proyecto
    con una base de datos y un servidor de prueba
    '''
    DEBUG = True
    TESTING = True
    # No consentimos a SQL seguir la modificaciones
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # Base de datos utilizada
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:Djangoorm@localhost:3306/blog_db"


class ProductionConfig(Config):
    DEBUG = False


class DevelopmentConfig(Config):
    # Variable secreta para para la seguridad el na generación de tokens
    SECRET_KEY = "dev"
    DEBUG = True
    TESTING = True

