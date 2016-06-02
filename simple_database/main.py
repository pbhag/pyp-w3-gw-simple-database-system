import csv
import string
import os
import exceptions

# A database is a collection of tables.
# Each table is a list of dictionaries. 
# Each dict is 4 things: 1. 'name' 2. name of value, 3. 'type' 4. value

def create_database(db_name):
    # Make a folder for each database, which has CSV-(tables)
    # If folder exists: Give database exist error

    if os.path.exists(db_name):
        raise ValidationError(
            'Database with name "{}" already exists.'.format(db_name))
    else:
        os.makedirs(db_name)

def connect_database(db_name):
    #opening a folder on the computer
    if not os.path.exists(db_name):
        raise ValidationError(
            'Database with name "{}" doesnt exist.'.format(db_name))
    else:
        os.chdirs(db_name)
   
    raise NotImplementedError()

def show_tables(db_name):
    #print the filenames of everything in the current directory
    os.listdir(db_name)

def create_table(table):
    # Creating a .csv file
    csvfilename = '{}.csv'.format(db_name)
    with open(csvfilename):
        pass

def table_count(db_name):
    pass
