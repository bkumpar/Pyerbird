#-------------------------------------------------------------------------------
# Name:        fdb
# Purpose:     class definition of connection to firebird database
#
# Author:      Boris
#
# Created:     25.02.2012
# Copyright:   (c) Boris 2012
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#!/usr/bin/env python

# from fbexceptions import *
# from fbclient import *
# from fbconstants import *
from fbconnection import connection
# from fbcursor import *
# from PyAPI import *

def connect(db_name, user, pwd):
    cnn =connection()
    cnn.connect(db_name, user, pwd)
    return cnn

def create(db_name, user, pwd):
    cnn =connection()
    cnn.create_database (db_name, user, pwd)
    return cnn



