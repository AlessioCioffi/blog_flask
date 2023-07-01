from flask import(
    render_template,Blueprint,flash,
    g, request, redirect, url_for
    )
from werkzeug.exceptions import abort
from myblog.models.post import Post
from myblog.models.user import User
from myblog.views.auth import login_required
from myblog import db

blog = Blueprint('blog',__name__)


# obtener el usuario
def get_user(id):
    user = User.query.get_or_404(id)
    return user


# Cbtener publiclaciónes
@blog.route('/')
def index():
    posts = Post.query.all()
    posts = list(reversed(posts))
    db.session.commit()
    return render_template('blog/index.html', posts=posts, get_user=get_user)


# Crar publicación
@blog.route('/blog/create', methods=['GET','POST'])#sigue la ruta /auth
@login_required
def create():
    if request.method == 'POST':
        title = request.form.get('title')
        content = request.form.get('content')

        post = Post(g.user.id, title=title,content=content)
        error = None
        if not title:
            error = 'Se requiere un titulo'
        elif not content:
            error = 'Se requiere el texto'
        elif error is not None:
            flash(error)
        else:
            db.session.add(post)
            db.session.commit()
            return redirect(url_for('blog.index'))
        flash(error)
    return render_template('blog/create.html')


# obtener post
def get_post(id, check_author=True):
    post = Post.query.get(id)

    if post is None:
        abort(404, f'Id {id} de la publicación no existe')

    if check_author and post.author!=g.user.id:
        abort(404)
    return post

# Editar publicacion
@blog.route('/blog/update/<int:id>', methods=['GET','POST'])#sigue la ruta /auth
@login_required
def update(id):

    post = get_post(id)

    if request.method == 'POST':
        post.title = request.form.get('title')
        post.content = request.form.get('content')

        error = None
        if not post.title:
            error = 'Se requiere un titulo'
        elif not post.content:
            error = 'Se requiere el texto'
        elif error is not None:
            flash(error)
        else:
            db.session.add(post)
            db.session.commit()
            return redirect(url_for('blog.index'))
        flash(error)
    return render_template('blog/update.html', post=post)


# Eliminar un post
@blog.route('/blog/delete/<int:id>')
@login_required
def delete(id):
    post = get_post(id)
    db.session.delete(post)
    db.session.commit()
    return redirect(url_for('blog.index'))

