#-------------------------------------------------------------------------------
# Name:        XSQLDA
# Purpose:     defiinition od XSQLDA structures
#
# Author:      Boris
#
# Created:     28.02.2012
# Copyright:   (c) Boris 2012
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#!/usr/bin/env python

from ctypes import Structure, addressof
from ctypes import c_short, c_char_p, c_char,  c_int, sizeof
from fbconstants import SQLDA_CURRENT_VERSION

METADATALENGTH = 32

name_buffer = c_char * METADATALENGTH

class PyXSQLVAR(Structure ):
    _pack_ = 1
    _fields_ = [
    ('sqltype',         c_short),       # datatype of field
    ('sqlscale',        c_short),       # scale factor
    ('sqlsubtype',      c_short),       # datatype subtype - BLOBs & text types only
    ('sqllen',          c_short),       # length of data area
    ('sqldata',         c_char_p),      # address of data
    ('sqlind',          c_short),        # address of indicator variable
    ('sqlname_length',  c_short),       # length of sqlname field
    ('sqlname',         name_buffer),   # name of field, name length + space for NULL
    ('relname_length',  c_short),       # length of relation name
    ('relname',         name_buffer),   # field's relation name + space for NULL
    ('ownname_length',  c_short),       # length of owner name
    ('ownname',         name_buffer),   # relation's owner name + space for NULL
    ('aliasname_length',c_short),       # length of alias name
    ('aliasname',       name_buffer)    # relation's alias name + space for NULL
                ]
    nullable = c_short(0)

    def __init__(self):
        self.sqlind = addressof(self.nullable)
        pass

    def __str__(self):
        s =     'sqltype: ' + str(self.sqltype)
        s = s + '\nsqlscale: ' + str(self.sqlscale)
        s = s + '\nsqlsubtype: ' + str(self.sqlsubtype)
        s = s + '\nsqllen: ' + str(self.sqllen)
        s = s + '\nsqldata: ' + str(self.sqldata)
        s = s + '\nsqlind: ' + str(self.nullable.value)
        s = s + '\nsqlname_length: ' + str(self.sqlname_length)
        s = s + '\nsqlname: ' + str(self.sqlname)
        s = s + '\nrelname_length: ' + str(self.relname_length)
        s = s + '\nrelname: ' + str(self.relname)
        s = s + '\nownname_length: ' + str(self.ownname_length)
        s = s + '\nownname: ' + str(self.ownname)
        s = s + '\naliasname_length: ' + str(self.aliasname_length)
        s = s + '\naliasname: ' + str(self.aliasname)
        return s

DEFAULT_FIELDS_NUM_ALLOCATED = 10

XSQLDA_name = c_char * 8
PyXSQLVAR_array = PyXSQLVAR * DEFAULT_FIELDS_NUM_ALLOCATED
#define XSQLDA_LENGTH(n)        (sizeof (XSQLDA) + (n - 1) * sizeof (XSQLVAR))

class PyXSQLDA(Structure):
    _pack_ = 1
    _fields_ = [
        ('version', c_short ),          # Short;    version of this XSQLDA
        ('sqldaid', XSQLDA_name),       # array[0..7] of Char; XSQLDA name field
        ('sqldabc', c_int),            # ISC_LONG; length in bytes of SQLDA
        ('sqln', c_short ),             # Short;    number of fields allocated
        ('sqld', c_short ),             # Short;    actual number of fields
        ('sqlvar', PyXSQLVAR_array)     # array[0..DEFAULT_FIELDS_NUM_ALLOCATED] of XSQLVAR; first field address
                ]

    def __init__(self):
        self.version = SQLDA_CURRENT_VERSION
        self.sqldaid = 'xxxxxxxx'           # array[0..7] of Char; XSQLDA name field
        self.sqln = c_short(DEFAULT_FIELDS_NUM_ALLOCATED)  # Short;    number of fields allocated
        self.sqld = c_short(0)              # Short;    actual number of fields
        self.sqldabc= sizeof(PyXSQLDA) - sizeof(PyXSQLVAR)                    # ISC_LONG; length in bytes of SQLDA
        self.sqlvar =  PyXSQLVAR_array()    # array[0..DEFAULT_FIELDS_NUM_ALLOCATED] of XSQLVAR; first field address

 
    def __str__(self):
        s = 'version: ' + str(self.version)
        s = s + '\nsqldaid: ' + str(self.sqldaid)
        s = s + '\nsqldabc: ' + str(self.sqldabc)
        s = s + '\nsqln: ' + str(self.sqln)
        s = s + '\nsqld ' + str(self.sqld)
        for i in range(self.sqld ):
            s = s + '\n--------------[%d]----------------------\n' % i
            s = s + str(self.sqlvar[i])

        return s

