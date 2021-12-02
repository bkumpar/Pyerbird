#-------------------------------------------------------------------------------
# Name:         test
# Purpose:      test program for pyerbird
#
# Author:       Boris
#
# Created:      24.02.2012
# Copyright:    (c) Boris 2012
# Licence:      <your licence>
#-------------------------------------------------------------------------------
#!/usr/bin/env python

import fdb
import fbcursor
import fbexceptions

#connection parameters
user_name = 'SYSDBA'
password = 'masterkey'
##database_name = 'D:\\baze\\Pytest2.fdb'
database_name = '/srv/firebird/pyrebird3.fdb'

def  test_create_database():
    connection = fdb.create(database_name, user_name, password)
    connection.close()

    

def test_create_table():
    sql_create_table = """CREATE TABLE PYTABLE(
                            ID INTEGER NOT NULL,
                            NAME VARCHAR(64),
                            NUMINT INTEGER,
                            NUMDBL DOUBLE PRECISION,
                            PRIMARY KEY(ID));"""

    try:
        connection = fdb.connect(database_name, user_name, password)
        cursor = connection.cursor()
        cursor.transaction_start()
        cursor.execute(sql_create_table)
        cursor.transaction_commit()
        cursor.close()

    except fbexceptions.DatabaseError as e:
        print "Error connection to database, code=" + str(e.gdscode)
    pass

def test_insert ():
    sql_insert_data = "insert into PYTABLE(id, name) values(1, 'PyThOn')"

    try:
        connection = fdb.connect(database_name, user_name, password)
        cursor = connection.cursor()
        cursor.transaction_start()
        cursor.execute(sql_insert_data)
        cursor.transaction_commit()
        cursor.close()

    except fbexceptions.DatabaseError as e:
        print "Error connection to database, code=" + str(e.gdscode)
    pass

def test_update ():
    sql_update_data = "UPDATE PYTABLE SET  NAME = 'New value'  WHERE ID = 1"

    try:
        connection = fdb.connect(database_name, user_name, password)
        cursor = connection.cursor()
        cursor.transaction_start()
        cursor.execute(sql_update_data)
        cursor.transaction_commit()
        cursor.close()

    except fbexceptions.DatabaseError as e:
        print "Error connection to database, code=" + str(e.gdscode)
    pass

def test_delete ():
    sql_update_data = "delete from  PYTABLE  WHERE ID = 1"

    try:
        connection = fdb.connect(database_name, user_name, password)
        cursor = connection.cursor()
        cursor.transaction_start()
        cursor.execute(sql_update_data)
        cursor.transaction_commit()
        cursor.close()

    except fbexceptions.DatabaseError as e:
        print "Error connection to database, code=" + str(e.gdscode)
    pass

    

def test_drop():

    try:
        connection = fdb.connect(database_name, user_name, password)
        connection.drop_database() # tested, seems OK
        connection.close()

    except fbexceptions.DatabaseError as e:
        print "Error connection to database, code=" + str(e.gdscode)
    pass

def test_update_param():
    try:

        connection = fdb.connect(database_name, user_name, password)
        cursor = connection.cursor()
        cursor.transaction_start()
        statement = "UPDATE PYTABLE SET  NAME = ?  WHERE ID = ?;                \0"
        params = ('REPLACEMENT', 1)
        cursor.method2(statement,params)
##        statement = "INSERT INTO PYTABLE(ID, NAME, NUMINT, NUMDBL) VALUES(?,?, ?, ?)"
##        params = (18 , 'New entry', 101, 105.5)
##        for i in range(50):
##            params = (i , 'New entry %d' % i, 100*i+i, 100.0 + 1.0/(i+1.0))
##            cursor.method2(statement,params)

        cursor.transaction_commit()
        cursor.close()
        connection.close()

    except fbexceptions.DatabaseError as e:
        print "Error connection to database, code=" + str(e.gdscode)
##        print cursor.error_message()
    pass

def test_retrieve():
    try:

        connection = fdb.connect(database_name, user_name, password)
        try:
            cursor = connection.cursor()
            cursor.transaction_start()
            statement = "SELECT * FROM PYTABLE WHERE ID<13"

            cursor.method3(statement)
            print cursor.description()
            row = cursor.fetchone()
            while row != None :
                print row
                row = cursor.fetchone()

            cursor.transaction_commit()
            cursor.close()
        except fbexceptions.DatabaseError as e:
            cursor.transaction_rollback()
            cursor.close()
            print "Error executing statement, code=" + str(e.gdscode)
        pass

        connection.close()

    except fbexceptions.DatabaseError as e:
        print "Error connection to database, code=" + str(e.gdscode)

    pass


def test_retrieve_param():
    try:

        connection = fdb.connect(database_name, user_name, password)
        try:
            cursor = connection.cursor()
            cursor.transaction_start()
            statement = "SELECT * FROM PYTABLE WHERE ID=?"
            params = (13,)

            cursor.method4(statement, params )
            print cursor.description()
            row = cursor.fetchone()
            while row != None :
                print row
                row = cursor.fetchone()

            cursor.transaction_commit()
            cursor.close()
        except fbexceptions.DatabaseError as e:
            cursor.transaction_rollback()
            cursor.close()
            print "Error executing statement, code=" + str(e.gdscode)
            print e.message
        pass

        connection.close()

    except fbexceptions.DatabaseError as e:
        print "Error connection to database, code=" + str(e.gdscode)

    pass


def test_client_info():
    from PyAPI import py_get_client_version
    from PyAPI import py_get_client_major_version
    from PyAPI import py_get_client_minor_version

    print py_get_client_version()
    print py_get_client_major_version(),'.',py_get_client_minor_version()
    pass




def main():
#    test_create_database()
#    test_drop()
#    test_create_table()
#    test_insert()
#    test_update()
#    test_update_param()
    test_retrieve()
#    test_retrieve_params()
#    test_client_info()


if __name__ == '__main__':
    main()

