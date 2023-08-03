# Blog con Flask

Este proyecto es un blog desarrollado con Flask.
El blog permite a los usuarios crear, ver o manipular publicaciones y realizar comentarios en ellas.

# Instalación

Para ejecutar este proyecto, se recomienda seguir los siguientes pasos:

1. Clona el repositorio

2. Crea el entorno virtual
python -m venv venv
     
3. Activa el entorno virtual en Windows
venv\Scripts\activate

4. Instala las dependencias utilizando el archivo requirements.txt:
pip install -r requirements.txt

5. Cadena de conexión para SQLAlchemy en config.py
SQLALCHEMY_DATABASE_URI = f"mysql+pymysql://{DATABASE_USER}:{DATABASE_PASSWORD}@{DATABASE_HOST}:{DATABASE_PORT}/{DATABASE_NAME}"

6. Ejecuta la app localmente
python main.py runserver
