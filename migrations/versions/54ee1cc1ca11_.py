"""empty message

Revision ID: 54ee1cc1ca11
Revises: 65ef2dc34975
Create Date: 2025-02-15 21:28:38.495126

"""

from alembic import op


# revision identifiers, used by Alembic.
revision = "54ee1cc1ca11"
down_revision = "65ef2dc34975"
branch_labels = None
depends_on = None


def upgrade():
    # Atualiza o valor padrão da coluna
    with op.batch_alter_table("account", schema=None) as batch_op:
        batch_op.alter_column("category", server_default="bronze")

    # Força TODOS os registros a terem 'bronze' na categoria
    op.execute("UPDATE account SET category = 'bronze'")


def downgrade():
    # Reverte o valor padrão
    with op.batch_alter_table("account", schema=None) as batch_op:
        batch_op.alter_column("category", server_default="Comum")

    # Reverte TODOS os registros ao valor anterior
    op.execute("UPDATE account SET category = 'Comum'")
