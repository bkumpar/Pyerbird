#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Boris
#
# Created:     08.03.2012
# Copyright:   (c) Boris 2012
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#!/usr/bin/env python

from ctypes import c_long, addressof

def main():
    pass

if __name__ == '__main__':
    main()

# base class for all handles
class py_handle:
    value = c_long(0)
    
    def __init__(self):
        self.value= c_long(0)

    def __str__(self):
        return str(self.value)
    
    def clear(self):
        self.value = c_long(0)

# database handle
class py_db_handle(py_handle):
    pass # end of py_db_handle

# transaction handle
class py_tr_handle(py_handle):
    pass # end of py_db_handle

# statement handle
class py_stmt_handle(py_handle):
    pass # end of py_db_handle

