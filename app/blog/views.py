from flask import (
    Blueprint,
    flash,
    redirect,
    render_template,
    request,
    url_for,
)
from flask_login import login_required, current_user
from app.blog.forms import BlogForm
from app.blog.models import Post
from app.utils import flash_errors
from flask_wtf import FlaskForm
blueprint = Blueprint("blog", __name__, static_folder="../static")
POSTS_PER_PAGE = 2
@blueprint.route("/insert", methods=["GET", "POST"])
def insert():
    """Add new blog post."""
    form = BlogForm(request.form)
    if form.validate_on_submit():
        Post.create(
            title=form.title.data,
            message=form.message.data,
            author_id=current_user.id
        )
        flash("Thank you adding new post.", "success")
        return redirect(url_for("public.home"))
    else:
        flash_errors(form)
    return render_template("/blog/add.html", form=form)


@blueprint.route("/list", )
def list():
    posts = Post.query.all()
    form = FlaskForm() #need thos for csrf_token
    return render_template("/blog/list.html", posts = posts, form = form)

@blueprint.route("/search", )
def search():
    search_word = request.args.get('search')
    if search_word:
        posts = Post.query.filter(Post.title.contains(search_word)|Post.message.contains(search_word))
    else:
        posts = Post.query.all()
    return render_template("public/home.html", posts=posts)


@blueprint.route("/list_pages", )
def list_pages():
    page = request.args.get('page', 1, type=int)
    posts = Post.query.paginate(page, per_page=POSTS_PER_PAGE)
    return render_template("/blog/list_pages.html", posts=posts)

#This route is for deleting a post
@blueprint.route('/delete/<id>/', methods = ['GET', 'POST'])
def delete(id):
    my_data = Post.query.get(id)
    my_data.delete()
    flash("Post Deleted Successfully")
    return redirect(url_for("public.home"))

@blueprint.route('/update/', methods = ['GET', 'POST'])
def update(id):
    my_data = Post.query.get(id)
    title=form.title.data
    message=form.message.data
    my_data.update(title=title,message=message)
    flash("Post Updated Successfully")
    return redirect(url_for("public.home"))
