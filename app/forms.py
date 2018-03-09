from flask_wtf import FlaskForm
from wtforms import TextField, TextAreaField
from wtforms.validators import DataRequired


class TopicForm(FlaskForm):
	title = TextField("Title :", validators=[DataRequired("title field is required ?!")])
	content = TextAreaField("Content :", validators=[DataRequired("content field is required ?!")])