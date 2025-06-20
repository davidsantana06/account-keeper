from flask_wtf import FlaskForm
from wtforms import SelectField, StringField, SubmitField
from wtforms.validators import DataRequired, Length

from app.facade import Password


class UserForm(FlaskForm):
    name = StringField(
        label="Nome",
        render_kw={"placeholder": "Nome*"},
        validators=[DataRequired(), Length(min=1, max=60)],
    )
    first_view = SelectField(
        label="Tela de abertura",
        choices=[("home:index", "Início"), ("account:index", "Contas")],
    )
    password_complexity = SelectField(
        label="Complexidade das senhas",
        choices=[
            (Password.LOW_COMPLEXITY, "Levis (Baixa)"),
            (Password.MEDIUM_COMPLEXITY, "Modicus (Média)"),
            (Password.HIGH_COMPLEXITY, "Perplexus (Alta)"),
        ],
    )
    zoom = SelectField(
        label="Escala de visualização",
        choices=[
            ("zoom-0", "Pé no Solo (100%)"),
            ("zoom-1", "Vista do Fórum (110%)"),
            ("zoom-2", "Olhar do Legado (120%)"),
            ("zoom-3", "Visão do Centurião (130%)"),
            ("zoom-4", "Olho de Júpiter (140%)"),
            ("zoom-5", "Horizonte do Coliseu (150%)"),
        ],
    )
    submit = SubmitField(label="Salvar", render_kw={"disabled": True})
