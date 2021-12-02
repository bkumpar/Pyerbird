#-------------------------------------------------------------------------------
# Name:        fbclient
# Purpose:     interface to fbclient functions
#
# Author:      Boris
#
# Created:     25.02.2012
# Copyright:   (c) Boris 2012
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#

from ctypes import cdll, c_long, pointer, c_short, c_char_p
from fbconstants import firebird_dll

#
# load fbclient library for importing foreign functions
# which use 'stdcall' calling convention
#
fbclient_dll = cdll.LoadLibrary(firebird_dll)

isc_attach_database     = getattr(fbclient_dll,'isc_attach_database')
#isc_attach_database.argtypes = [pointer(c_long), c_short, c_char_p, pointer(c_long), c_short, c_char_p ]
# isc_attach_database.restype = c_long 

isc_detach_database     = getattr(fbclient_dll,'isc_detach_database')
isc_drop_database       = getattr(fbclient_dll,'isc_drop_database')

isc_print_status            = getattr(fbclient_dll,'isc_print_status')
isc_interprete              = getattr(fbclient_dll,'isc_interprete')

isc_commit_retaining        = getattr(fbclient_dll,'isc_commit_retaining')
isc_commit_transaction      = getattr(fbclient_dll,'isc_commit_transaction')
isc_rollback_transaction    = getattr(fbclient_dll,'isc_rollback_transaction')

isc_dsql_execute_immediate  = getattr(fbclient_dll,'isc_dsql_execute_immediate')
isc_dsql_execute            = getattr(fbclient_dll,'isc_dsql_execute')
isc_dsql_execute2           = getattr(fbclient_dll,'isc_dsql_execute2')

isc_get_client_version      = getattr(fbclient_dll,'isc_get_client_version')
isc_get_client_major_version= getattr(fbclient_dll,'isc_get_client_major_version')
isc_get_client_minor_version= getattr(fbclient_dll,'isc_get_client_minor_version')

isc_dsql_allocate_statement = getattr(fbclient_dll,'isc_dsql_allocate_statement')
isc_dsql_prepare            = getattr(fbclient_dll,'isc_dsql_prepare')
isc_dsql_describe           = getattr(fbclient_dll,'isc_dsql_describe')
isc_dsql_describe_bind      = getattr(fbclient_dll,'isc_dsql_describe_bind')
isc_dsql_fetch              = getattr(fbclient_dll,'isc_dsql_fetch')
isc_dsql_set_cursor_name    = getattr(fbclient_dll,'isc_dsql_set_cursor_name')

isc_dsql_sql_info = getattr(fbclient_dll,'isc_dsql_sql_info')
isc_portable_integer = getattr(fbclient_dll,'isc_portable_integer')

# because of different calling convention (cdecl) for functions
# which accept undefined number of arguments
fbclient_dll_cdcl       = cdll.LoadLibrary(firebird_dll)
isc_expand_dpb          = getattr(fbclient_dll_cdcl,'isc_expand_dpb')
isc_start_transaction   = getattr(fbclient_dll_cdcl,'isc_start_transaction')

