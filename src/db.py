from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from config import get_db_url
from sqlalchemy import BigInteger
# Создаем базу
Base = declarative_base()

# Определяем модель


class MarketData(Base):
    __tablename__ = 'market_data'
    id = Column(Integer, primary_key=True, autoincrement=True)
    ticker = Column(String)
    period = Column(String)
    date = Column(String)
    time = Column(String)
    open = Column(Float)
    high = Column(Float)
    low = Column(Float)
    close = Column(Float)
    volume = Column(BigInteger)


DATABASE_URL = get_db_url()
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base.metadata.create_all(bind=engine)
