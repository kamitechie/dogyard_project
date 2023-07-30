from sqlalchemy.orm import sessionmaker
from dogyard_models import Dog, engine

Session = sessionmaker(bind=engine)
session = Session()
all_dogs = session.query(Dog).all()
for dog in all_dogs:
    print(dog.dogs_name, dog.birth_date)