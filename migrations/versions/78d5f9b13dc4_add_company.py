"""add company

Revision ID: 78d5f9b13dc4
Revises: 59628dea39ff
Create Date: 2025-09-23 21:17:14.694783

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '78d5f9b13dc4'
down_revision = '59628dea39ff'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "company",
        sa.Column("id", sa.Integer, primary_key=True, autoincrement=True),
        sa.Column("company_name", sa.String(length=255), nullable=False),
        sa.Column("domain_name", sa.String(length=255), nullable=False),
    )

def downgrade():
    op.drop_table("company")
