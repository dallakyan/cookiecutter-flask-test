# -*- coding: utf-8 -*-
"""Public forms."""
from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired
from wtforms.widgets import TextArea
class BlogForm(FlaskForm):
    """Blog form."""
    message = StringField("message", validators=[DataRequired()], widget=TextArea())

