#-------------------------------------------------------------------------------
# Name:        PyAPI
# Purpose:
#
# Author:      Boris
#
# Created:     28.02.2012
# Copyright:   (c) Boris 2012
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#!/usr/bin/env python

from ctypes import c_char_p, byref, c_long, cast, POINTER
from fbclient import *
from fbconstants import *
from XSQLDA import PyXSQLDA

def py_attach_database(status_vector, database_name, db_handle, dpb ):
    databaseName_ptr = c_char_p(database_name)
    databaseName_len = len(database_name)
    isc_attach_database(byref(status_vector.status_vector_ptr),
                        databaseName_len,
                        databaseName_ptr,
                        byref(db_handle.value),
                        dpb.length(),
                        byref(dpb.dpb_ptr))

def py_detach_database(status_vector, db_handle):
    isc_detach_database(byref(status_vector.status_vector_ptr), byref(db_handle.value))

def py_print_status(status_vector):
    isc_print_status(status_vector.address())
    return

def py_interprete(error_buffer, status_vector):
    #print status_vector.status_vector_ptr
    svp= cast(status_vector.status_vector_ptr, POINTER(c_long))
    return isc_interprete(byref(error_buffer.data_ptr), byref(svp))


def py_drop_database(status_vector, db_handle):
    isc_drop_database(byref(status_vector.status_vector_ptr),
                               byref(db_handle.value))

def py_dsql_execute_immediate(status_vector, db_handle, tr_handle, sql  ):
    isc_dsql_execute_immediate(byref(status_vector.status_vector_ptr),
                               byref(db_handle.value),
                               byref(tr_handle.value),
                                0,
                                sql,
                                1,
                                None )
    

def py_dsql_execute(status_vector, tr_handle, st_handle, sqlda):
    isc_dsql_execute(byref(status_vector.status_vector_ptr),
                    byref(tr_handle.value),
                    byref(st_handle.value),
                    1,
                    byref(sqlda))

def py_dsql_execute2(status_vector, tr_handle, stmt, in_xsqlda, out_xsqlda):
    isc_dsql_execute2(byref(status_vector.status_vector_ptr),
                      byref(tr_handle.value),
                      stmt.address(),
                      1,
                      byref(in_xsqlda),
                      byref(out_xsqlda))

def py_start_transaction(status_vector,
                         tr_handle,
                         db_handle,
                         tpb):
    print '*py_start_transaction*'
    isc_start_transaction(byref(status_vector.status_vector_ptr),
                          byref(tr_handle.value),
                          1,
                          byref(db_handle.value),
                          tpb.length(),
                          byref(tpb.tpb_ptr) )
    
def py_commit_transaction(status_vector, tr_handle):
    print '*py_commit_transaction*'
    isc_commit_transaction(byref(status_vector.status_vector_ptr),
                          byref(tr_handle.value));

def py_rollback_transaction(status_vector, tr_handle):
    isc_rollback_transaction(byref(status_vector.status_vector_ptr),
                            byref(tr_handle.value))

def py_dsql_allocate_statement(status_vector, db_handle, st_handle):
    isc_dsql_allocate_statement(byref(status_vector.status_vector_ptr),
                                   byref(db_handle.value),
                                   byref(st_handle.value))

def py_dsql_prepare(status_vector, tr_handle, st_handle, statement, sqlda):
    isc_dsql_prepare(byref(status_vector.status_vector_ptr),
                     byref(tr_handle.value),
                     byref(st_handle.value),
                     #len(statement),
                     50, # for NULL terminated string
                     c_char_p(statement),
                     SQLDA_VERSION1,
                     byref(sqlda))
    print "isc_dsql_prepare"

def py_dsql_describe_bind(status_vector, st_handle, sqlda):
    isc_dsql_describe_bind(byref(status_vector.status_vector_ptr),
                           byref(st_handle.value),
                           SQLDA_VERSION1,
                           byref(sqlda))
    print "py_dsql_describe_bind"
    
def py_dsql_describe(status_vector, st_handle, sqlda):
    isc_dsql_describe(byref(status_vector.status_vector_ptr),
                      byref(st_handle.value),
                      SQLDA_VERSION1,
                      byref(sqlda))
    print "py_dsql_describe"


def py_get_client_version():
    buff = c_char_p('00000000000000000000000000000000')
    isc_get_client_version(buff)
    return buff.value


def py_get_client_major_version():
    return isc_get_client_major_version()


def py_get_client_minor_version():
    return isc_get_client_minor_version()


def py_dsql_sql_info(status_vector, st_handle, item_length, items, buffer_length, buffer):
    items = c_char_p('00000000000000000000000000000000')
    buffer = c_char_p('00000000000000000000000000000000')
    isc_dsql_sql_info( byref(status_vector.status_vector_ptr),
                       byref(st_handle.value),
                       32,
                       items,
                       32,
                       buffer)
    return

def py_dsql_fetch (status_vector, st_handle, out_sqlda ):
     return isc_dsql_fetch(byref(status_vector.status_vector_ptr),
                           byref(st_handle.value),
                           1,
                           byref(out_sqlda))


def py_portable_integer(return_bufer, offset, length):
    return isc_portable_integer(byref(return_bufer.data_ptr, offset), length)

def py_dsql_set_cursor_name(status_vector,stmt_handle,cursor_name):
    ret = isc_dsql_set_cursor_name(status_vector.address(),
                         stmt_handle.address(),
                         c_char_p(cursor_name),
                         None );
    print '*py_dsql_set_cursor_name*', ret
