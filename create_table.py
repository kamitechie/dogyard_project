import psycopg2
from config import config


def create_tables():
    """ create tables in the PostgreSQL database"""
    commands = (
        """
        CREATE TABLE IF NOT EXISTS dogs_data (
            dog_id SERIAL PRIMARY KEY NOT NULL,
            photo BYTEA,
            dogs_name VARCHAR(255),
            birth_date DATE NOT NULL,
            gender VARCHAR(10),
            pool VARCHAR(10),
            mother INT,
            father INT
        )
        """,
        """
        CREATE TABLE IF NOT EXISTS positions (
            id SERIAL PRIMARY KEY NOT NULL,
            position VARCHAR(10) UNIQUE NOT NULL
        )
        """,
        """ CREATE TABLE IF NOT EXISTS dogs_position (
            id SERIAL PRIMARY KEY NOT NULL,
            dog_id INT,
            position_id INT,
            FOREIGN KEY (dog_id)
              REFERENCES dogs_data (dog_id)
              ON UPDATE CASCADE ON DELETE CASCADE,
            FOREIGN KEY (position_id)
              REFERENCES positions (id)
              ON UPDATE CASCADE ON DELETE CASCADE
        )
        """,
        """
        CREATE TABLE IF NOT EXISTS basic_hospital_data (
            id SERIAL PRIMARY KEY NOT NULL,
            is_neutered BOOLEAN,
            is_in_rut BOOLEAN,
            date_of_death DATE,
            FOREIGN KEY (id)
              REFERENCES dogs_data (dog_id)
              ON UPDATE CASCADE ON DELETE CASCADE
        )
        """,
        """
        CREATE TABLE IF NOT EXISTS injury (
            id SERIAL PRIMARY KEY,
            type VARCHAR(255) UNIQUE NOT NULL
        )
        """,
        """
        CREATE TABLE IF NOT EXISTS injury_hospital_data (
            id SERIAL PRIMARY KEY NOT NULL,
            dog_id INT NOT NULL,
            injury_date DATE NOT NULL,
            vet_checkup_needed BOOLEAN,
            injury_type_id INT NOT NULL,
            injury_place VARCHAR(255),
            drugs_name VARCHAR(255),
            drugs_time_in_days INT,
            stays_in BOOLEAN,
            is_case_closed BOOLEAN,
            FOREIGN KEY (dog_id)
              REFERENCES dogs_data (dog_id)
              ON UPDATE CASCADE ON DELETE CASCADE,
            FOREIGN KEY (injury_type_id)
              REFERENCES injury (id)
              ON UPDATE CASCADE ON DELETE CASCADE
        )
        """,
        """
        CREATE TABLE IF NOT EXISTS adoption_owners_data (
            id SERIAL PRIMARY KEY,
            first_name VARCHAR(255),
            last_name VARCHAR(255),
            phone_number VARCHAR(255),
            email VARCHAR(255),
            relocation_place VARCHAR(255)
        )
        """,
        """
        CREATE TABLE IF NOT EXISTS adoption_data (
            id SERIAL PRIMARY KEY,
            dog_id INT NOT NULL,
            adoption_date DATE,
            owners_id INT,
            reason VARCHAR(255),
            is_adopted BOOLEAN,
            is_ready_for_adoption BOOLEAN,
            FOREIGN KEY (dog_id)
              REFERENCES dogs_data (dog_id)
              ON UPDATE CASCADE ON DELETE CASCADE,
            FOREIGN KEY (owners_id)
              REFERENCES adoption_owners_data (id)
              ON UPDATE CASCADE ON DELETE CASCADE
        )
        """,
        """
        CREATE TABLE IF NOT EXISTS borrow_person_data (
            id SERIAL PRIMARY KEY,
            first_name VARCHAR(255),
            last_name VARCHAR(255),
            phone_number VARCHAR(255),
            email VARCHAR(255)
        )
        """,
        """
        CREATE TABLE IF NOT EXISTS borrow_data (
            id SERIAL PRIMARY KEY,
            dog_id INT NOT NULL,
            borrowers_id INT NOT NULL,
            date_of_taking DATE,
            date_of_giving_back DATE,
            note TEXT,
            FOREIGN KEY (dog_id)
              REFERENCES dogs_data (dog_id)
              ON UPDATE CASCADE ON DELETE CASCADE,
            FOREIGN KEY (borrowers_id)
              REFERENCES borrow_person_data (id)
              ON UPDATE CASCADE ON DELETE CASCADE
        )
        """,
        """
        CREATE TABLE IF NOT EXISTS family_siblings (
            id SERIAL PRIMARY KEY,
            dog_id INT NOT NULL,
            sibling_id INT,
            FOREIGN KEY (dog_id)
              REFERENCES dogs_data (dog_id)
              ON UPDATE CASCADE ON DELETE CASCADE,
            FOREIGN KEY (sibling_id)
              REFERENCES dogs_data (dog_id)
              ON UPDATE CASCADE ON DELETE CASCADE
        )
        """

    )
    conn = None
    try:
        # read the connection parameters
        params = config()
        # connect to the PostgreSQL server
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        # create table one by one
        for command in commands:
            cur.execute(command)
            print('New table was created in database')
        # close communication with the PostgreSQL database server
        cur.close()
        # commit the changes
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print('Connection is closed.')


if __name__ == '__main__':
    create_tables()