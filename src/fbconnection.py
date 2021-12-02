#-------------------------------------------------------------------------------
# Name:        fbconnection
# Purpose:
#
# Author:      Boris
#
# Created:     07.03.2012
# Copyright:   (c) Boris 2012
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#!/usr/bin/env python

from PyAPI import *
from PyHandles import *
from PyStructures import *
from fbexceptions import *
from fbcursor import cursor
from ctypes  import pointer, cast


class connection:

    db_handle = py_db_handle()

#     def print_status_vector(self):
#         for i in range(0,19):
#             print self.status_vector_ptr[i]

    def connect(self, databaseName, username, password):
        print '*connect*'
        status_vector = py_status_vector()
        dpb = py_dpb(username, password)
        print dpb

        py_attach_database(status_vector, databaseName, self.db_handle, dpb)
        
        print self.db_handle
        
        if status_vector.error():
            
#              pvector = self.status_vector_ptr
#              error_buffer = py_error_buffer()
#              pvector = self.status_vector.pointer()
#              py_interprete(error_buffer, pvector)
            self.process_conection_errors(status_vector)


    def close(self):
        status_vector = py_status_vector()
        isc_detach_database(
            byref(status_vector.status_vector_ptr),
            byref(self.db_handle.value)
            
            )
        ## check status vector against errors!!!
        if status_vector.error():
            print '---------------------------------------------------'
            m = self.error_message(status_vector)
            print m
            print '---------------------------------------------------'
            raise DatabaseError(m,status_vector.status_vector_ptr[1])

    def commit(self):
        pass

    def rollback(self):
        pass

    def cursor(self):
        return cursor(self)

    def drop_database(self):
        print '*drop_database*'
        status_vector = py_status_vector()
        isc_drop_database(byref(self.status_vector_ptr), byref(self.db_handle))
           
        if self.isStatusError():
            self.print_status_vector()
#             error_buffer = py_error_buffer()
#             pvector = self.status_vector_ptr
#             py_interprete(error_buffer, addressof(pvector));
#             self.process_conection_errors(self.status_vector.value(1) )


    def create_database(self, databaseName, username, password, page_size=8192, default_charset='UTF8'):
            print '*create_database*'
            sql = """CREATE DATABASE '{}' 
                user '{}' 
                password '{}' 
                page_size {} 
                default character set {}""".format(databaseName,username,password,page_size,default_charset)    

            dpb = py_dpb(username, password)
            print dpb
            status_vector = py_status_vector()
            isc_dsql_execute_immediate(byref(self.status_vector_ptr),
                                None,
                                None,
                                len(sql),
                                sql,
                                1,
                                None )

            
            print self.print_status_vector()

#             if (self.status_vector.value(0) == 1) and (self.status_vector.value(1) > 1):
#                 pvector = self.status_vector.pointer()
#                 error_buffer = py_error_buffer()
#                 pvector = self.status_vector.pointer()
#                 py_interprete(error_buffer, addressof(pvector));
#                 self.process_conection_errors(self.status_vector.value(1) )


    def process_conection_errors(self, status_vector):
        errorcode = status_vector.status_vector_ptr[1]
        if errorcode==335544344 :
            raise DatabaseError('Invalid database name.',errorcode )
        elif errorcode==335544472:
            raise DatabaseError('Invalid username and/or password.',errorcode)
        elif errorcode ==335544324:
            raise DatabaseError('Invalid database handle (no active connection).',errorcode)
        else:
            raise DatabaseError('Unknown database error.',errorcode)

