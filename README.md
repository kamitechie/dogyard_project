# Dogyard project

## 1. Database phase

Create database step-by-step:
1. Create database in PostgresSQL
2. Create file database.ini 

>Example:
>
>[postgresql]  
host=localhost  
dbname=my_data  
user=postgres  
password=your_password  
port=5432

3. Run file create_table.py
4. Run file insert_data.py

Database is done.
## 2. Creating classes phase
Creating classes:

1. In file dogyard_models.py change db_url variable with your user, password, host and data_name.
2. Run file dogyard_models.py
