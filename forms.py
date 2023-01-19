from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, URL
from flask_ckeditor import CKEditorField

##WTForm
class CreatePostForm(FlaskForm):
    title = StringField("Blog Post Title", validators=[DataRequired()])
    subtitle = StringField("Subtitle", validators=[DataRequired()])
    img_url = StringField("Blog Image URL", validators=[DataRequired(), URL()])
    body = CKEditorField("Blog Content", validators=[DataRequired()])
    submit = SubmitField("Submit Post")

##RF
class RegisterForm(FlaskForm):
    email = StringField("Enter your email address", validators=[DataRequired()])
    password = PasswordField("Enter your password", validators=[DataRequired()])
    name = StringField("Enter your first name", validators=[DataRequired()])
    submit = SubmitField("SIGN UP")

##LF
class LoginForm(FlaskForm):
    email = StringField("Enter your email", validators=[DataRequired()])
    password = PasswordField("Enter your password", validators=[DataRequired()])
    submit = SubmitField("Login")

#CF
class CommentForm(FlaskForm):
    comment_text = CKEditorField("Comment", validators=[DataRequired()])
    submit = SubmitField("SUBMIT COMMENT")