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

import sys
sys.path.append('/home/bkumpar/eclipse-workspace/Pyerbird/src/')
print sys.path


import database
import cursor
from fbexceptions import DatabaseError


# common data
user_name = 'SYSDBA'
password = 'masterkey'
database_name = '/srv/firebird/pyrebird.fdb'

def test_create_database():
	try:
		# create new database and connect onto..
		connection = database.create(database_name, user_name, password)
		connection.close()

	except DatabaseError as e:
		print "Error connection to database, code=" + str(e.gdscode)

def test_create_table():
	sql_create_table = "CREATE TABLE PYTABLE(ID INTEGER NOT NULL, NAME VARCHAR(64), PRIMARY KEY(ID));"
	sql_insert = "insert into PYTABLE(id, name) values(1, 'PyThOn')"
	try:
		connection = database.connect(database_name, user_name, password)
		cursor = connection.cursor()
		cursor.execute(sql_create_table)
		cursor.execute(sql_insert)
		cursor.close()
	except Exception as e:
		print "Error creting table, code=" + str(e.gdscode)

def test_drop():
	
#	try:

##  connect to existing database or ..
		connection = database.connect(database_name, user_name, password)
		connection.drop_database() # tested, seems OK
##        connection.close()

#	except DatabaseError as e:
#		print "Error connection to database, code=" + str(e.gdscode)
#


def main():
#	test_create()
	test_create_table()
#	test_drop()
	



if __name__ == '__main__':
	main()

