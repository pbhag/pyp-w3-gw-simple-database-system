# - *- coding: utf- 8 - *-
import csv
import string
import os
import os.path
from simple_database.exceptions import *
from simple_database.config import BASE_DB_FILE_PATH


# A database is a collection of tables.
# Each table is a list of dictionaries. 
# Each dict is 4 things: 1. 'name' 2. name of value, 3. 'type' 4. value

class Database(object):
    
    def __init__(self, database_name):
        self.name = database_name
        self.table_names = []
        self.file_path = '{}{}/'.format(BASE_DB_FILE_PATH, database_name)
    
    def create_table(self, name, columns):
        table = Table(self.name, name, columns)
        setattr(self, name, table)
        self.table_names.append(name)
        # Get different csv name depending on table name
        headers_type_csv = '{}{}_type.csv'.format(self.file_path,name)
        data_csv = '{}{}_data.csv'.format(self.file_path,name)
        
        # Get both name and type info.
        names_in_list = [d['name'] for d in columns]
        types_in_list = [d['type'] for d in columns]
        both_in_list = zip(names_in_list, types_in_list)
        
        # Create 2 .csv files
        
        # Create data_csv - Blank, will write to in insert_table
        d = open(data_csv, 'w')
        d.close()
        
        # Create type_csv
        with open(headers_type_csv, 'w') as f:
            writer = csv.writer(f)
            #for row in both_in_list, write a row in headers_type_csv
            for row in both_in_list:
                writer.writerow(row)
            
        
        
class Table(object):
    def __init__(self, db_name, table_name, columns):
        self.name = table_name
        self.file_path = '{}{}/{}/'.format(BASE_DB_FILE_PATH, 
                                           db_name, table_name)
        self.headers = open('{}_type.csv'.format(table_name), 'a')
        self.data = '{}_data.csv'.format(table_name)
        
    def insert(self, *args):
        #raise exception if data types don't fit  # TODO
        with open(self.data, 'a') as f:
            writer = csv.writer(f)
            writer.writerow(args)


    def show_tables(self):
        pass
        

    def count(self):
        with open(self.data, 'a') as f:
            total = sum(1 for row in f)
        return total
        
def create_database(db_name):
    filepath ='{}{}'.format(BASE_DB_FILE_PATH, db_name)
    # Make a folder for each database, which has CSV-(tables)
    # If folder exists: Give database exist error
    if os.path.exists(filepath):
        raise ValidationError(
            'Database with name "{}" already exists.'.format(db_name))
    else:
        os.makedirs(filepath)
    return Database(db_name)
    # create and return the database object

def connect_database(db_name):
    filepath ='{}{}'.format(BASE_DB_FILE_PATH, db_name)
    #opening a folder on the computer
    # check if folder exists, if not: error
    if not os.path.exists(filepath):
        raise ValidationError(
            'Database with name "{}" doesnt exist.'.format(db_name))
    else:
        os.chdir(filepath)
   


def describe():
    pass

def query():
    pass
