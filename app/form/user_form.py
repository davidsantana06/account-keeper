from flask_wtf import FlaskForm
from wtforms import SelectField, StringField, SubmitField
from wtforms.validators import DataRequired, Length


class UserForm(FlaskForm):
    name = StringField(
        label="Nome",
        render_kw={"placeholder": "Nome"},
        validators=[DataRequired(), Length(min=1, max=60)],
    )
    first_view = SelectField(label="Página inicial")
    password_complexity = SelectField(label="Complexidade das senhas")
    zoom = SelectField(label="Escala de visualização")
    submit = SubmitField(label="Salvar", render_kw={"disabled": True})
