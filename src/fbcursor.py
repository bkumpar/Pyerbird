#-------------------------------------------------------------------------------
# Name:         fbcursor
# Purpose:      containn class implements cursor functionality
#
# Author:       Boris
#
# Created:      24.02.2012
# Copyright:    (c) Boris 2012
# Licence:      <your licence>
#-------------------------------------------------------------------------------
#!/usr/bin/env python

from PyAPI import *
from PyHandles import *
from PyStructures import *
from fbexceptions import *
from fbconstants import *
from XSQLDA import PyXSQLDA
from ctypes import *

class cursor():
    _description = None
    _rowcount = -1
    arraysize = 1
    status_vector = py_status_vector()
    tpb = py_tpb()
    transaction = py_tr_handle()
    active = False
    connection = None


    def __init__(self, connection):
        self.active = True
        self.connection = connection
        pass

    def description(self):
        return self._description

    def rowcount(self):
        return self._rowcount

    def close(self):
        self.active = False
        self.connection = None

    def transaction_start(self):
        py_start_transaction(self.status_vector,
                             self.transaction,
                             self.connection.db_handle,
                             self.tpb)

    def transaction_commit(self):
        py_commit_transaction(self.status_vector, self.transaction)

    def transaction_rollback(self):
        py_rollback_transaction(self.status_vector, self.transaction)


    def execute(self, operation, parameters = []):
        if self.active :
            py_dsql_execute_immediate(self.status_vector,
                                      self.connection.db_handle,
                                      self.transaction,
                                      c_char_p(operation )
                                      )
        else:
            raise Error

    def executemany(self,operation,seq_of_parameters):
        pass

    def fetchmany(self, size=-1):
        pass

    def fetchall(self):
        pass

    def nextset(self):
        pass

    def setinputsizes(self,sizes):
        pass

    def setoutputsize(self,size,column=0):
        pass

    def method1(self):
        # statement without input or output parameters
        pass

    def method2(self, statement, params):
        status_vector = py_status_vector()
        
        #Declare and initialize an SQL statement handle
        stmt_handle = py_stmt_handle()

        py_dsql_allocate_statement(status_vector, self.connection.db_handle, stmt_handle)
        ## check status vector against errors!!!
        if status_vector.error():
            print '(1)', stmt_handle.value , status_vector
            print self.error_message()
            raise Error

        #Preparing and executing a statement string with parameters
##        sql=c_char_p(statement)

        # Parse the statement string
        
        py_dsql_prepare(status_vector, self.transaction, stmt_handle, statement, None)

        ## check status vector against errors!!!
        if status_vector.error():
            print '(2)', stmt_handle.value , status_vector
            print self.error_message(status_vector)
            raise Error

        #Creating the input XSQLDA
        self.in_SQLDA = PyXSQLDA()

        py_dsql_describe_bind(status_vector, stmt_handle, self.in_SQLDA)

        ## check status vector against errors!!!
        if status_vector.error():
            print '(3)', stmt_handle.value , status_vector
            print self.error_message(status_vector)
            raise Error

        #Compare the value of the sqln field of the XSQLDA to the value of the
        # sqld field to make sure enough XSQLVAR s are allocated to hold
        # information about each parameter.
        cparams=[]
        if(self.in_SQLDA.sqln < self.in_SQLDA.sqld):
            raise Exception('No room enough for parameters')
        for i in range(self.in_SQLDA.sqld):
            var = self.in_SQLDA.sqlvar[i]
            print i, var.sqltype
            dtype = var.sqltype & ~ 1 ## remove NULL flag
            if dtype == SQL_VARYING :
                var.sqltype = SQL_TEXT
                cparams.append(c_char_p(params[i]))
                var.sqldata = cparams[i]
            elif dtype == SQL_TEXT:
                cparams.append(c_char_p(params[i]))
                var.sqldata = cparams[i]
            elif dtype == SQL_LONG:
                cparams.append(c_long(params[i]))
                var.sqldata =  addressof(cparams[i])
            elif dtype == SQL_DOUBLE :
                cparams.append(c_double(params[i]))
                var.sqldata =  addressof(cparams[i])

            if( var.sqltype & 1) != 0 :
                var.sqlind = addressof(c_short(0))

        print  '[4] ', self.in_SQLDA

        py_dsql_execute(status_vector, self.transaction, stmt_handle, self.in_SQLDA )

        ## check status vector against errors!!!
        if status_vector.error():
            print '(4)',stmt_handle.value , status_vector
            print '---------------------------------------------------'
            m = self.error_message(status_vector)
            print m
            print '---------------------------------------------------'
            raise DatabaseError(m,status_vector.status_vector_ptr[1])
    # end of method2


    def method3(self, statement):
        status_vector = py_status_vector()
        #Declare and initialize an SQL statement handle
        stmt_handle = py_stmt_handle()

        py_dsql_allocate_statement(status_vector, self.connection.db_handle, stmt_handle)
        ## check status vector against errors!!!
        if status_vector.error():
            print '---------------------------------------------------'
            m = self.error_message(status_vector)
            print m
            print '---------------------------------------------------'
            raise DatabaseError(m,status_vector.status_vector_ptr[1])



        #Creating the input XSQLDA
        self.out_SQLDA = PyXSQLDA()
        # Parse the statement string
        py_dsql_prepare(status_vector, self.transaction, stmt_handle , statement, self.out_SQLDA)
        ## check status vector against errors!!!
        if status_vector.error():
            print '---------------------------------------------------'
            m = self.error_message(status_vector)
            print m
            print '---------------------------------------------------'
            raise DatabaseError(m,status_vector.status_vector_ptr[1])



        #Parse the statement string
        py_dsql_describe(status_vector, stmt_handle, self.out_SQLDA)

        ## check status vector against errors!!!
        if status_vector.error():
            print '---------------------------------------------------'
            m = self.error_message(status_vector)
            print m
            print '---------------------------------------------------'
            raise DatabaseError(m,status_vector.status_vector_ptr[1])

        #Compare the value of the sqln field of the XSQLDA to the value of the
        # sqld field to make sure enough XSQLVAR s are allocated to hold
        # information about each parameter.

        self.c_out_params=[] ## holds ctypes representation of params
        if(self.out_SQLDA.sqln < self.out_SQLDA.sqld):
            raise Exception('No room enough for parameters')
        for i in range(self.out_SQLDA.sqld):
            var = self.out_SQLDA.sqlvar[i]
            dtype = var.sqltype & ~ 1 ## remove NULL flag
            if dtype == SQL_VARYING :
                var.sqltype = SQL_TEXT
                charbuffer = c_char * var.sqllen
                self.c_out_params.append(charbuffer())
                var.sqldata = addressof(self.c_out_params[i])
            elif dtype == SQL_TEXT:
                charbuffer = c_char * var.sqllen
                self.c_out_params.append(charbuffer())
                var.sqldata = addressof(self.c_out_params[i])
            elif dtype == SQL_LONG:
                self.c_out_params.append(c_long(0))
                var.sqldata =  addressof(self.c_out_params[i])
            elif dtype == SQL_DOUBLE :
                self.c_out_params.append(c_double(0.0))
                var.sqldata =  addressof(self.c_out_params[i])

            if( var.sqltype & 1) != 0 :
                var.sqlind = addressof(c_short(0))

        self.describe()

        py_dsql_execute(status_vector, self.transaction , stmt_handle, self.out_SQLDA )

        ## check status vector against errors!!!
        if self.status_vector.error():
            print '---------------------------------------------------'
            m = self.error_message(status_vector)
            print m
            print '---------------------------------------------------'
            raise DatabaseError(m,status_vector.status_vector_ptr[1])

    def method4(self, statement, params):
        ### query with input and output parameters
        #Declare and initialize an SQL statement handle
        self.stmt = py_stmt_handle()
        py_dsql_allocate_statement(self.connection.status_vector, self.connection.db_handle, self.stmt)
        ## check status vector against errors!!!
        if (self.status_vector.error()):
            print '(1)',self.stmt,  self.stmt.value , self.connection.status_vector

        #Creating the input XSQLDA
        self.in_SQLDA = PyXSQLDA()
        #Creating the output XSQLDA
        self.out_SQLDA = PyXSQLDA()

        # Parse the statement string
        py_dsql_prepare(self.connection.status_vector, self.transaction, self.stmt , statement, self.out_SQLDA)

        print self.out_SQLDA
        print 'sizeof(PyXSQLDA): ' , sizeof(self.out_SQLDA)

        ## check status vector against errors!!!
        if self.status_vector.error():
            print '(2)', self.stmt,  self.stmt.value , self.connection.status_vector

        # Parse the statement string
##        py_dsql_prepare(self.connection.status_vector, self.transaction, self.stmt , statement, None ) # <- here is error

        ## check status vector against errors!!!
        if self.status_vector.error():
            print '(2)', self.stmt,  self.stmt.value , self.connection.status_vector
            print self.error_message()
            raise Error


        #Parse the statement string
        py_dsql_describe_bind(self.connection.status_vector, self.stmt, self.in_SQLDA)

        ## check status vector against errors!!!
        if self.status_vector.error():
            print '(3)', self.stmt,  self.stmt.value , self.connection.status_vector
            print self.error_message()
            raise Error

        #Compare the value of the sqln field of the XSQLDA to the value of the
        # sqld field to make sure enough XSQLVAR s are allocated to hold
        # information about each parameter.
        cparams=[]
        if(self.in_SQLDA.sqln < self.in_SQLDA.sqld):
            raise Exception('No room enough for parameters')
        for i in range(self.in_SQLDA.sqld):
            var = self.in_SQLDA.sqlvar[i]
            print i, var.sqltype
            dtype = var.sqltype & ~ 1 ## remove NULL flag
            if dtype == SQL_VARYING :
                var.sqltype = SQL_TEXT
                cparams.append(c_char_p(params[i]))
                var.sqldata = cparams[i]
            elif dtype == SQL_TEXT:
                cparams.append(c_char_p(params[i]))
                var.sqldata = cparams[i]
            elif dtype == SQL_LONG:
                cparams.append(c_long(params[i]))
                var.sqldata =  addressof(cparams[i])
            elif dtype == SQL_DOUBLE :
                cparams.append(c_double(params[i]))
                var.sqldata =  addressof(cparams[i])

##            if( var.sqltype & 1) != 0 :
##                var.sqlind = addressof(c_short(0))

        #Parse the statement string
        py_dsql_describe(self.connection.status_vector, self.stmt, self.out_SQLDA)

        ## check status vector against errors!!!
        if self.status_vector.error():
            print '(4)', self.stmt,  self.stmt.value , self.connection.status_vector

        #Compare the value of the sqln field of the XSQLDA to the value of the
        # sqld field to make sure enough XSQLVAR s are allocated to hold
        # information about each parameter.

        self.c_out_params=[] ## holds ctypes representation of params
        if(self.out_SQLDA.sqln < self.out_SQLDA.sqld):
            raise Exception('No room enough for parameters')
        for i in range(self.out_SQLDA.sqld):
            var = self.out_SQLDA.sqlvar[i]
            dtype = var.sqltype & ~ 1 ## remove NULL flag
            if dtype == SQL_VARYING :
                var.sqltype = SQL_TEXT
                charbuffer = c_char * var.sqllen
                self.c_out_params.append(charbuffer())
                var.sqldata = addressof(self.c_out_params[i])
            elif dtype == SQL_TEXT:
                charbuffer = c_char * var.sqllen
                self.c_out_params.append(charbuffer())
                var.sqldata = addressof(self.c_out_params[i])
            elif dtype == SQL_LONG:
                self.c_out_params.append(c_long(0))
                var.sqldata =  addressof(self.c_out_params[i])
            elif dtype == SQL_DOUBLE :
                self.c_out_params.append(c_double(0.0))
                var.sqldata =  addressof(self.c_out_params[i])

            if( var.sqltype & 1) != 0 :
                var.sqlind = addressof(c_short(0))

        self.describe()

        print  '[6] in_sqlda:\n', self.in_SQLDA
        print  '[7] out_sqlda\n', self.out_SQLDA

        py_dsql_execute2(self.connection.status_vector, self.transaction , self.stmt, self.in_SQLDA, self.out_SQLDA )
        py_dsql_set_cursor_name(self.connection.status_vector, self.stmt, "dyn_cursor")
          ## check status vector against errors!!!
        if self.status_vector.error():
            print '(4)',self.stmt,  self.stmt.value , self.connection.status_vector
            print '---------------------------------------------------'
            m = self.error_message()
            print m
            print '---------------------------------------------------'
            raise DatabaseError(m,self.status_vector.value(1))


        ret = py_dsql_fetch(self.status_vector,
                            self.stmt,
                            self.out_SQLDA)
        if self.status_vector.error():
            print '(4)',self.stmt,  self.stmt.value , self.connection.status_vector
            print '---------------------------------------------------'
            m = self.error_message()
            print m
            print '---------------------------------------------------'
            raise DatabaseError(m,self.status_vector.value(1))

        pass


    def error_message(self,status_vector):
        error_buffer = py_error_buffer()
        s = ''
        svp= cast(status_vector.status_vector_ptr, POINTER(c_long))
        while isc_interprete(byref(error_buffer.data_ptr), byref(svp))!=0 :
            s = s + str(error_buffer) + '\n'
        return s


    def fetchone(self):
        ret = py_dsql_fetch(self.status_vector,
                            self.stmt,
                            self.out_SQLDA)
        if(ret == 100):
            return None
        elif(ret==0):
            row = ()
            for i in range(self.out_SQLDA.sqld):
                value =self.c_out_params[i].value
                row = row + (value, )
            return row
        else:
            m = self.error_message()
            raise DatabaseError(m,self.status_vector.value(1))

        pass

    def describe(self):
        print '*describe*'
        self._description = ()

        for i in range(self.out_SQLDA.sqld):
            if( self.out_SQLDA.sqlvar[i].sqltype & 1 == 1):
                null_ok = self.out_SQLDA.sqlvar[i].nullable.value
##                null_ok = True
            else:
                null_ok = False

            col = (self.out_SQLDA.sqlvar[i].aliasname, #name
                   self.out_SQLDA.sqlvar[i].sqltype,   #type_code
                   None,                               #display_size
                   None,                               #internal_size
                   None,                               #precision
                   None,                               #scale
                   null_ok )                           #null_ok
            self._description = self._description + (col,)
        return

    def _statement_type(self, st_handle):
        print "_statement_type"
        items = py_info_items(1)
        items.data_ptr[0] = isc_info_sql_stmt_type
        status_vector = py_status_vector()
        return_buffer = py_return_buffer()
        py_dsql_sql_info(status_vector ,
                         st_handle,
                         items.length,
                         items,
                         return_buffer.length,
                         return_buffer )
        print return_buffer
        print "__"
        data_length = py_portable_integer(return_buffer,1, 2)
        print py_portable_integer(return_buffer, 3, data_length)
        print "__"

    # end of class cursor

