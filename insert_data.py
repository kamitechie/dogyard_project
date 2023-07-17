import psycopg2
from config import config
from datetime import date


def open_pic(dog_name):
    """Open picture file"""
    return open(f'small_pic/{dog_name}.jpg', 'rb').read()


sql_line_dogs_data = "INSERT INTO dogs_data (photo, dogs_name, birth_date, gender, pool, mother, father) " \
                     "VALUES(%s, %s, %s, %s, %s, %s, %s)"
dogs_data = [(psycopg2.Binary(open_pic('Haggel')), 'Haggel', date(year=2013, month=3, day=12), 'm', 'A', 34, 35),
             (psycopg2.Binary(open_pic('Troika')), 'Troika', date(year=2012, month=4, day=1), 'f', 'A', 28, 29),
             (psycopg2.Binary(open_pic('Drums')), 'Drums', date(year=2022, month=5, day=3), 'f', 'A', 25, 37),
             (psycopg2.Binary(open_pic('Elg')), 'Elg', date(year=2021, month=6, day=3), 'm', 'A', 9, 20),
             (psycopg2.Binary(open_pic('Stein')), 'Stein', date(year=2013, month=9, day=19), 'm', 'A', 26, 30),
             (psycopg2.Binary(open_pic('O2')), 'O2', date(year=2013, month=9, day=19), 'm', 'Racing', 26, 30),
             (psycopg2.Binary(open_pic('Krypton')), 'Krypton', date(year=2013, month=9, day=19), 'm', 'Racing', 26, 30),
             (psycopg2.Binary(open_pic('Daim')), 'Daim', date(year=2012, month=4, day=1), 'f', 'B', 28, 29),
             (psycopg2.Binary(open_pic('Dis')), 'Dis', date(year=2018, month=7, day=12), 'f', 'B', 31, 6),
             (psycopg2.Binary(open_pic('Puppy1')), None, date(year=2023, month=5, day=20), 'm', None, 24, 19),
             (psycopg2.Binary(open_pic('Puppy2')), None, date(year=2023, month=5, day=20), 'f', None, 24, 19),
             (psycopg2.Binary(open_pic('Puppy3')), None, date(year=2023, month=5, day=20), 'f', None, 24, 19),
             (psycopg2.Binary(open_pic('Tromso')), 'Tromso', date(year=2020, month=8, day=23), 'm', 'B', 24, 21),
             (psycopg2.Binary(open_pic('Kvaloya')), 'Kvaloya', date(year=2020, month=8, day=23), 'f', 'B', 24, 21),
             (psycopg2.Binary(open_pic('Sno')), 'Sno', date(year=2013, month=3, day=12), 'f', 'B', 34, 35),
             (psycopg2.Binary(open_pic('Python')), 'Python', date(year=2013, month=11, day=2), 'f', 'Racing', None, None),
             (psycopg2.Binary(open_pic('Tiki')), 'Tiki', date(year=2022, month=2, day=14), 'f', 'C', 16, 20),
             (psycopg2.Binary(open_pic('Ra')), 'Ra', date(year=2022, month=2, day=14), 'm', 'C', 16, 20),
             (psycopg2.Binary(open_pic('Rod')), 'Rod', date(year=2014, month=8, day=1), 'm', 'Racing', None, None),
             (psycopg2.Binary(open_pic('Kazys')), 'Kazys', date(year=2014, month=1, day=25), 'm', 'C', None, None),
             (psycopg2.Binary(open_pic('Oregano')), 'Oregano', date(year=2013, month=3, day=5), 'm', 'C', 32, 33),
             (psycopg2.Binary(open_pic('Karry')), 'Karry', date(year=2013, month=3, day=5), 'm', 'C', 32, 33),
             (psycopg2.Binary(open_pic('Avocado')), 'Avocado', date(year=2012, month=10, day=10), 'm', 'D', None, None),
             (psycopg2.Binary(open_pic('Laika')), 'Laika', date(year=2016, month=12, day=1), 'f', 'D', None, None),
             (psycopg2.Binary(open_pic('Agat')), 'Agat', date(year=2017, month=8, day=3), 'f', 'Racing', 26, 27),
             (psycopg2.Binary(open_pic('Princess')), 'Princess', date(year=2007, month=4, day=13), 'f', 'D', None, None),
             (psycopg2.Binary(open_pic('Lupus')), 'Lupus', date(year=2007, month=2, day=12), 'm', 'D', None, None),
             (psycopg2.Binary(open_pic('Gigi')), 'Gigi', date(year=2007, month=11, day=3), 'f', 'D', None, None),
             (psycopg2.Binary(open_pic('Bjorn')), 'Bjorn', date(year=2006, month=5, day=19), 'm', 'E', None, None),
             (psycopg2.Binary(open_pic('Skog')), 'Skog', date(year=2008, month=8, day=8), 'm', 'E', None, None),
             (psycopg2.Binary(open_pic('Maja')), 'Maja', date(year=2015, month=10, day=27), 'f', 'Racing', None, None),
             (psycopg2.Binary(open_pic('Sara')), 'Sara', date(year=2008, month=1, day=12), 'f', 'E', None, None),
             (psycopg2.Binary(open_pic('Fint')), 'Fint', date(year=2009, month=9, day=17), 'f', 'E', None, None),
             (psycopg2.Binary(open_pic('Ana')), 'Ana', date(year=2007, month=9, day=1), 'f', 'E', None, None),
             (psycopg2.Binary(open_pic('Will')), 'Will', date(year=2006, month=3, day=4), 'm', 'E', None, None)]

sql_line_positions = "INSERT INTO positions (position) VALUES(%s)"
positions = [('lead',),
             ('cheer',),
             ('wheel',)]

sql_line_dogs_position = "INSERT INTO dogs_position (dog_id, position_id) VALUES(%s, %s)"
dogs_position = [(1, 3),
                 (2, 1),
                 (2, 2),
                 (3, 3),
                 (4, 2),
                 (5, 3),
                 (8, 1),
                 (9, 2),
                 (13, 2),
                 (14, 2),
                 (15, 1),
                 (17, 2),
                 (18, 2),
                 (20, 2),
                 (20, 3),
                 (21, 2),
                 (22, 2),
                 (23, 2),
                 (24, 1),
                 (26, 2),
                 (27, 2),
                 (28, 2),
                 (29, 1),
                 (30, 3),
                 (31, 1),
                 (32, 2),
                 (33, 2),
                 (34, 1),
                 (35, 2),
                 (35, 3)]

sql_line_basic_hospital_data = "INSERT INTO basic_hospital_data (is_neutered, is_in_rut, date_of_death) " \
                               "VALUES(%s, %s, %s)"
basic_hospital_data = [(False, False, None),
                       (False, False, None),
                       (False, False, None),
                       (False, False, None),
                       (False, False, None),
                       (False, False, None),
                       (False, False, None),
                       (False, False, None),
                       (False, True, None),
                       (False, False, None),
                       (False, False, None),
                       (False, False, None),
                       (False, True, None),
                       (False, True, None),
                       (True, False, None),
                       (False, False, None),
                       (False, False, None),
                       (False, False, None),
                       (False, False, None),
                       (False, False, date(year=2023, month=4, day=23)),
                       (False, False, None),
                       (True, False, None),
                       (True, False, None),
                       (False, False, None),
                       (False, False, None),
                       (False, False, date(year=2021, month=10, day=3)),
                       (False, False, date(year=2022, month=12, day=13)),
                       (False, False, date(year=2019, month=6, day=14)),
                       (False, False, date(year=2020, month=6, day=1)),
                       (False, False, date(year=2021, month=9, day=5)),
                       (False, False, None),
                       (False, False, date(year=2018, month=9, day=1)),
                       (False, False, date(year=2018, month=10, day=4)),
                       (False, False, date(year=2019, month=4, day=2)),
                       (False, False, date(year=2020, month=1, day=5))]

sql_line_injury = "INSERT INTO injury (type) VALUES(%s)"
injury = [('biten',),
          ('fungus',),
          ('deep cut',),
          ('neutered',),
          ('abortion',),
          ('operation',),
          ('broken',),
          ('infection',),
          ('poisoning',)]

sql_line_injury_hospital_data = "INSERT INTO injury_hospital_data (dog_id, injury_date, vet_checkup_needed, " \
                                "injury_type_id, injury_place, drugs_name, drugs_time_in_days, stays_in, " \
                                "is_case_closed) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s)"
injury_hospital_data = [(5, date(year=2023, month=6, day=19), False, 1, 'face', 'metacam', 3, False, False),
                        (22, date(year=2019, month=12, day=2), False, 2, 'paw', 'vinegar bath', 14, True, True),
                        (25, date(year=2023, month=5, day=3), True, 3, 'abdomen', 'metacam', 5, True, True),
                        (25, date(year=2023, month=5, day=3), True, 3, 'abdomen', 'antibiotics', 7, True, True),
                        (23, date(year=2023, month=6, day=15), False, 1, 'leg', 'metacam', 3, True, False)]

sql_line_adoption_data = "INSERT INTO adoption_data (dog_id, adoption_date, owners_id, reason, is_adopted, " \
                         "is_ready_for_adoption) VALUES(%s, %s, %s, %s, %s, %s)"
adoption_data = [(1, date(year=2023, month=6, day=1), 1, 'old', True, False),
                 (2, None, None, 'old', False, True),
                 (5, date(year=2023, month=6, day=1), 1, 'old', True, False),
                 (6, None, None, 'old', False, True),
                 (7, None, None, 'old', False, True),
                 (8, None, None, 'old', False, True),
                 (16, None, None, 'old', False, False),
                 (15, date(year=2021, month=6, day=1), 2, 'old', True, False),
                 (21, None, None, 'old', False, False),
                 (22, None, None, 'old', False, False),
                 (23, None, None, 'old', False, True),
                 (26, date(year=2016, month=6, day=1), 3, 'old', True, False),
                 (27, date(year=2016, month=6, day=1), 3, 'old', True, False),
                 (28, None, None, 'old', False, True),
                 (29, None, None, 'old', False, True),
                 (30, date(year=2021, month=6, day=1), 4, 'old', True, False),
                 (32, None, None, 'old', False, True),
                 (33, None, None, 'old', False, True)]

sql_line_adoption_owners_data = "INSERT INTO adoption_owners_data (first_name, last_name, phone_number, email, " \
                                "relocation_place) VALUES(%s, %s, %s, %s, %s)"
adoption_owners_data = [('Tadas', 'Zukauskas', '+3706294583', 'tadas.email@email.com', 'Lithuania'),
                        ('Ian', 'McDoughal', '+473239790', 'ian.email@email.com', 'Alta'),
                        ('Bente', 'Ellison', '+475974009', 'bente.email@email.com', 'Vikran'),
                        ('Ana', 'Ferguson', '+472003452', 'ana.email@email.com', 'Germany')]

sql_line_borrow_data = "INSERT INTO borrow_data (dog_id, borrowers_id, date_of_taking, date_of_giving_back, note) " \
                       "VALUES(%s, %s, %s, %s, %s)"
borrow_data = [(2, 1, date(year=2023, month=6, day=20), date(year=2023, month=6, day=27), None),
               (7, 2, date(year=2023, month=6, day=7), date(year=2023, month=6, day=10), 'Came back happy, '
                                                                                         'had a few hikes, '
                                                                                         'behaved good inside')]

sql_line_borrow_person_data = "INSERT INTO borrow_person_data (first_name, last_name, email, phone_number) " \
                              "VALUES(%s, %s, %s, %s)"
borrow_person_data = [('Simon', 'Davidson', 'simon@mail.com', '+472356335'),
                      ('Ingvild', 'Fevang', 'ingvild.@mail.com', '+479440239')]

sql_line_family_siblings = "INSERT INTO family_siblings (dog_id, sibling_id) VALUES(%s, %s)"
family_siblings = [(1, 15),
                   (2, 8),
                   (5, 6),
                   (5, 7),
                   (6, 5),
                   (6, 7),
                   (7, 6),
                   (7, 5),
                   (8, 2),
                   (10, 11),
                   (10, 12),
                   (11, 10),
                   (11, 12),
                   (12, 10),
                   (12, 11),
                   (13, 14),
                   (14, 13),
                   (15, 1),
                   (17, 18),
                   (18, 17),
                   (20, 31),
                   (21, 22),
                   (22, 21),
                   (31, 20)]


def insert_multiple_lines(sql_line, multiple_lines_list):
    """ insert multiple lines into the table  """

    conn = None
    try:
        # read database configuration
        params = config()
        # connect to the PostgreSQL database
        conn = psycopg2.connect(**params)
        # create a new cursor
        cur = conn.cursor()
        # execute the INSERT statement
        cur.executemany(sql_line, multiple_lines_list)
        # commit the changes to the database
        conn.commit()
        specific_table = sql_line.split(' ')[2]
        print(f'All records were inserted in {specific_table}.')
        # Fetch result
        cur.execute(f"SELECT * from {specific_table}")
        record = cur.fetchall()
        print("Result ", record)
        # close communication with the database
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print('Connection is closed.')


if __name__ == '__main__':
    # insert multiple positions
    insert_multiple_lines(sql_line_dogs_data, dogs_data)
    insert_multiple_lines(sql_line_positions, positions)
    insert_multiple_lines(sql_line_dogs_position, dogs_position)
    insert_multiple_lines(sql_line_basic_hospital_data, basic_hospital_data)
    insert_multiple_lines(sql_line_injury, injury)
    insert_multiple_lines(sql_line_injury_hospital_data, injury_hospital_data)
    insert_multiple_lines(sql_line_adoption_owners_data, adoption_owners_data)
    insert_multiple_lines(sql_line_adoption_data, adoption_data)
    insert_multiple_lines(sql_line_borrow_person_data, borrow_person_data)
    insert_multiple_lines(sql_line_borrow_data, borrow_data)
    insert_multiple_lines(sql_line_family_siblings, family_siblings)
