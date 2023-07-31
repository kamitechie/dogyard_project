from dataclasses import dataclass
from sqlalchemy import Column, String, Integer, Date, Boolean, Text, LargeBinary, create_engine
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


@dataclass
class Position(Base):
    __tablename__ = "positions"
    id = Column(Integer, primary_key=True)
    positon = Column(String)


@dataclass
class DogPosition(Base):
    __tablename__ = "dogs_position"
    id = Column(Integer, primary_key=True)
    dog_id = Column(Integer)
    position_id = Column(Integer)


@dataclass
class MedicalRecord(Base):
    __tablename__ = "basic_hospital_data"
    id = Column(Integer, primary_key=True)
    is_neutered = Column(Boolean)
    is_in_rut = Column(Boolean)
    date_of_death = Column(Date)


@dataclass
class Injury(Base):
    __tablename__ = "injury"
    id = Column(Integer, primary_key=True)
    dog_id = Column(Integer)
    injury_date = Column(Date)
    vet_checkup_needed = Column(Boolean)
    injury_type_id = Column(Integer)
    injury_place = Column(String)
    drugs_name = Column(String)
    drugs_time_in_days = Column(Integer)
    stays_in = Column(Boolean)
    is_case_closed = Column(Boolean)


@dataclass
class AdoptionOwner(Base):
    __tablename__ = "adoption_owners_data"
    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    phone_number = Column(String)
    email = Column(String)
    relocation_place = Column(String)


@dataclass
class AdoptionDog(Base):
    __tablename__ = "adopton_data"
    id = Column(Integer, primary_key=True)
    dog_id = Column(Integer)
    adoption_date = Column(Date)
    owners_id = Column(Integer)
    reason = Column(String)
    is_adopted = Column(Boolean)
    is_ready_for_adoption = Column(Boolean)


@dataclass
class BorrowPerson(Base):
    __tablename__ = "borrow_person_data"
    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    phone_number = Column(String)
    email = Column(String)


@dataclass
class BorrowDog(Base):
    __tablename__ = "borrow_data"
    id = Column(Integer, primary_key=True)
    dog_id = Column(Integer)
    borrowers_id = Column(Integer)
    date_of_taking = Column(Date)
    date_of_giving_back = Column(Date)
    note = Column(Text)


@dataclass
class Sibling(Base):
    __tablename__ = "family_siblings"
    id = Column(Integer, primary_key=True)
    dog_id = Column(Integer)
    sibling_id = Column(Integer)


db_url = 'postgresql+psycopg2://user:password@host/database_name'
engine = create_engine(db_url)
