#-------------------------------------------------------------------------------
# Name:        exceptions
# Purpose:     definitions of exceptions, following PEP249
#
# Author:      Boris
#
# Created:     26.02.2012
# Copyright:   (c) Boris 2012
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#!/usr/bin/env python


class Warning(StandardError):
    """
        Exception raised for important warnings like data
        truncations while inserting, etc. It must be a subclass of
        the Python StandardError (defined in the module
        exceptions).
    """
    pass

class Error(StandardError):
    """
        Exception that is the base class of all other error
        exceptions. You can use this to catch all errors with one
        single 'except' statement. Warnings are not considered
        errors and thus should not use this class as base. It must
        be a subclass of the Python StandardError (defined in the
        module exceptions).
    """

class InterfaceError(Error):
    """
        Exception raised for errors that are related to the
        database interface rather than the database itself.  It
        must be a subclass of Error.
    """
    pass

class DatabaseError(Error):
    """
        Exception raised for errors that are related to the
        database.  It must be a subclass of Error.
    """
    gdscode = 0
    message = ''
    def __init__(self, message, code):
        self.gdscode = code
        self.message = message
        print '__init__'
        pass

    pass

class DataError(DatabaseError):
    """
        Exception raised for errors that are due to problems with
        the processed data like division by zero, numeric value
        out of range, etc. It must be a subclass of DatabaseError.
    """
    pass

class OperationalError(DatabaseError):
    """
        Exception raised for errors that are related to the
        database's operation and not necessarily under the control
        of the programmer, e.g. an unexpected disconnect occurs,
        the data source name is not found, a transaction could not
        be processed, a memory allocation error occurred during
        processing, etc.  It must be a subclass of DatabaseError.
    """
    pass

class IntegrityError(DatabaseError):
    """
        Exception raised when the relational integrity of the
        database is affected, e.g. a foreign key check fails.  It
        must be a subclass of DatabaseError.
    """

class InternalError(DatabaseError):
    """
        Exception raised when the database encounters an internal
        error, e.g. the cursor is not valid anymore, the
        transaction is out of sync, etc.  It must be a subclass of
        DatabaseError.
    """
    pass


class ProgrammingError(DatabaseError):
    """
        Exception raised for programming errors, e.g. table not
        found or already exists, syntax error in the SQL
        statement, wrong number of parameters specified, etc.  It
        must be a subclass of DatabaseError.
    """
    pass


class NotSupportedError(DatabaseError):
    """
        Exception raised in case a method or database API was used
        which is not supported by the database, e.g. requesting a
        .rollback() on a connection that does not support
        transaction or has transactions turned off.  It must be a
        subclass of DatabaseError.
    """
    pass


