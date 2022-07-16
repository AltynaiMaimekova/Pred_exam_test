from flask_wtf import FlaskForm
from wtforms import validators
import wtforms as wf


class UserForm(FlaskForm):
    username = wf.StringField('Пользователь', validators=[wf.validators.DataRequired()])
    password = wf.PasswordField('Пароль', validators=[wf.validators.DataRequired()])
    submit = wf.SubmitField('Ok')


class CustomerForm(FlaskForm):
    name = wf.StringField('Имя', validators=[wf.validators.DataRequired()])
    phone_number = wf.StringField('Телефон', validators=[wf.validators.DataRequired()])
    item = wf.StringField('Товар', validators=[wf.validators.DataRequired()])
    quantity = wf.IntegerField('Количество', validators=[wf.validators.DataRequired()])
    price = wf.IntegerField('Цена', validators=[wf.validators.DataRequired()])
    submit = wf.SubmitField('Ok')


