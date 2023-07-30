from dataclasses import dataclass
from sqlalchemy import Column, String, Integer, Date, LargeBinary, create_engine
from sqlalchemy.orm import declarative_base
Base = declarative_base()


@dataclass
class Dog(Base):
    __tablename__ = "dogs_data"
    dog_id = Column(Integer, primary_key=True)
    photo = Column(LargeBinary)
    dogs_name = Column(String)
    birth_date = Column(Date)
    gender = Column(String)
    pool = Column(String)
    mother = Column(Integer)
    father = Column(Integer)

db_url = 'postgresql+psycopg2://user:password@host/database_name'
engine = create_engine(db_url)
