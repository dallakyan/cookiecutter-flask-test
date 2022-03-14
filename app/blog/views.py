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

blueprint = Blueprint("blog", __name__, static_folder="../static")
@blueprint.route("/addpost", methods=["GET", "POST"])
def addpost():
    """Add new blog post."""
    form = BlogForm(request.form)
    if form.validate_on_submit():
        Post.create(
            message=form.message.data,
            author_id=current_user.id
        )
        flash("Thank you adding new post.", "success")
        return redirect(url_for("public.home"))
    else:
        flash_errors(form)
    return render_template("/blog/add.html", form=form)
