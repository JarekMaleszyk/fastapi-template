from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.dialects.postgresql import JSONB
from datetime import datetime

Base = declarative_base()

class BasketRequest(Base):
    __tablename__ = "basket_requests"

    id = Column(Integer, primary_key=True, autoincrement=True)

    # Audit fields
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    api_version = Column(String, nullable=True)

    # Input fields (proste)
    REQUEST_ID = Column(String, nullable=True)
    SESSION_ID = Column(String, nullable=True)
    SYSTEM_CD = Column(String, nullable=True)
    SOURCE_ID = Column(String, nullable=True)
    CHANNEL_CD = Column(String, nullable=True)

    # Input fields (datagrid -> JSONB)
    GRID_IDENTIFIER_METADATA = Column(JSONB, nullable=True)
    GRID_IDENTIFIER_DATA = Column(JSONB, nullable=True)

    GRID_BASKET_METADATA = Column(JSONB, nullable=True)
    GRID_BASKET_DATA = Column(JSONB, nullable=True)

    ADD_PARAMS_METADATA = Column(JSONB, nullable=True)
    ADD_PARAMS_DATA = Column(JSONB, nullable=True)