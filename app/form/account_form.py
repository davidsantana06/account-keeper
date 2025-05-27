from flask_wtf import FlaskForm
from wtforms import (
    EmailField,
    SelectField,
    StringField,
    SubmitField,
    TelField,
    TextAreaField,
)
from wtforms.validators import DataRequired, Length, Optional
from wtforms.widgets import PasswordInput


class AccountForm(FlaskForm):
    name = StringField(
        label="Nome",
        render_kw={"placeholder": "Nome*"},
        validators=[DataRequired(), Length(min=1, max=60)],
    )
    category = SelectField(
        label="Categoria",
        choices=[
            ("bronze", "I - Bronze"),
            ("silver", "II - Prata"),
            ("gold", "III - Ouro"),
        ],
    )
    notes = TextAreaField(
        label="Notas",
        render_kw={"placeholder": "Notas"},
        validators=[Optional(), Length(max=900)],
    )
    username = StringField(
        label="Usuário",
        render_kw={"placeholder": "Usuário"},
        validators=[Optional(), Length(max=30)],
    )
    email = EmailField(
        label="E-mail",
        render_kw={"placeholder": "E-mail"},
        validators=[Optional(), Length(max=60)],
    )
    phone = TelField(
        label="Telefone",
        render_kw={
            "placeholder": "Telefone",
            "data-pattern": "(00) 90000-0000",
        },
        validators=[Optional(), Length(min=15, max=15)],
    )
    password = StringField(
        label="Senha",
        render_kw={"placeholder": "Senha"},
        validators=[Optional(), Length(max=60)],
        widget=PasswordInput(hide_value=False),
    )
    submit = SubmitField(label="Salvar", render_kw={"disabled": True})
