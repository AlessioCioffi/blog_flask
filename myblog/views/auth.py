import functools
from os import error
from flask import (render_template, Blueprint,
                   flash, g, redirect, request,
                   session,url_for)
'''
render_template: se utiliza para redirigir templates
Blueprint: se utiliza para registrar las vistas en la aplicación
flash: se utiliza para enviar mensajes cuando ocurren errores
g: se utiliza para capturar el usuario que ha iniciado sesión
redirect: se utiliza para redirection a una nueva ruta
request: se utiliza para capturar las peticiones del cliente
session: se utiliza para realizar consultas a la base de datos
url_for: se utiliza para trabajar con las rutas de manera dinámica
'''

from werkzeug.security import check_password_hash,generate_password_hash
from myblog import db


auth = Blueprint('auth', __name__, url_prefix='/auth')

from myblog.models.user import User

# Registrar usuario
@auth.route('/register', methods=['GET','POST'])
def register():
    # Con el decorador .rout asignamos el nombre register;
    # Con la petición auth/register devolvemos la función que decora
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        user = User(username=username, password=generate_password_hash(password))
        # Consultar presencia de errores
        error = None
        if not username:
            error = 'Se requiere nombre de usuario'
        elif not password:
            error = 'Se requiere la contraseña'
        # Consultar la tabla del modelo User
        user_name = User.query.filter_by(username=username).first()
        if user_name == None:
            db.session.add(user)
            db.session.commit()
            return redirect(url_for('auth.login'))
        else:
            error = f'El usuario {username} ya está registrado'
        flash(error)
        # Con el tag get_flashed_messages() llamo los errores en los templates
    return render_template('auth/register.html')


# Iniciar sesión usuario
@auth.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        user = User(username=username, password=generate_password_hash(password))
        error = None
        user = User.query.filter_by(username=username).first()
        if user==None:
            error = 'El usuario no está registrado'
        elif not check_password_hash(user.password, password):
            error = 'La contraseña es incorrecta'

        if error is None:
            session.clear()
            session['user_id']=user.id
            return redirect(url_for('blog.index'))
        flash(error)
    return render_template('auth/login.html')


# Verificar login
# Con el siguiente decorador se llama la función para cualquier solicitud de la app
@auth.before_app_request
def load_logged_in_user():
    user_id = session.get('user_id')
    if user_id is None:
        # Con g almaceno el objeto para llamarlo sin buscarlo cada vez
        g.user = None
    else:
        g.user = User.query.get_or_404(user_id)


# Cerrar sesión
@auth.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('blog.index'))


# Inicio sesión obligatorio
def login_required(view):
    '''El decorador tiene la capacidad de envolver la función
    sin perder las informaciones, que contiene de la función original,
    para utilizarlas otra vez'''
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            # si g.user no contiene datos redirigir a login
            return redirect(url_for('auth.login'))
        return view(**kwargs)
    return wrapped_view

