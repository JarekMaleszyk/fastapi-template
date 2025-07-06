from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

def upgrade():
    op.create_table(
        'basket_requests',
        sa.Column('id', sa.Integer(), primary_key=True),
        sa.Column('created_at', sa.DateTime(), nullable=False),
        sa.Column('api_version', sa.String(), nullable=True),
        sa.Column('REQUEST_ID', sa.String(), nullable=True),
        sa.Column('SESSION_ID', sa.String(), nullable=True),
        sa.Column('SYSTEM_CD', sa.String(), nullable=True),
        sa.Column('SOURCE_ID', sa.String(), nullable=True),
        sa.Column('CHANNEL_CD', sa.String(), nullable=True),
        sa.Column('GRID_IDENTIFIER_METADATA', postgresql.JSONB(), nullable=True),
        sa.Column('GRID_IDENTIFIER_DATA', postgresql.JSONB(), nullable=True),
        sa.Column('GRID_BASKET_METADATA', postgresql.JSONB(), nullable=True),
        sa.Column('GRID_BASKET_DATA', postgresql.JSONB(), nullable=True),
        sa.Column('ADD_PARAMS_METADATA', postgresql.JSONB(), nullable=True),
        sa.Column('ADD_PARAMS_DATA', postgresql.JSONB(), nullable=True),
    )
