#-------------------------------------------------------------------------------
# Name:        PyStructures
# Purpose:
#
# Author:      Boris
#
# Created:     08.03.2012
# Copyright:   (c) Boris 2012
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#!/usr/bin/env python

from ctypes import c_byte, c_int, c_long, addressof, POINTER
from fbconstants import isc_dpb_version1,isc_dpb_user_name,isc_dpb_password
from fbconstants import isc_tpb_write, isc_tpb_concurrency, isc_tpb_wait
from fbconstants import isc_tpb_version3, isc_tpb_read_committed,isc_tpb_no_rec_version
#from fbclient import isc_expand_dpb

class py_dpb:
    """
        database parameter buffer class
    """
    dpb_buffer_size = 255
    dpb_buffer = c_byte * 256
    dpb_ptr = dpb_buffer()
    dpb_length = 0

    def length(self):
        return self.dpb_length

    def address(self):
        return addressof(self.dpb_ptr)

    def __str__(self):
        s = []
        for i in range(self.dpb_length):
            val = self.dpb_ptr[i]
            if val<32 or val>127:
                c=str(val)
            else:
                c=chr(val)
            s=s+[c]
        return "|".join(s)

    def __init__(self, username, password):
        l=0
        for i in range(self.dpb_buffer_size):
            self.dpb_ptr[i] = 0

        self.dpb_ptr[l] = isc_dpb_version1
        l = l + 1
    # set up username
        if (username != ''):
            self.dpb_ptr[l] = isc_dpb_user_name
            l = l + 1
            self.dpb_ptr[l] = len(username )
            l = l + 1

            for i in username:
                self.dpb_ptr[l] = ord(i)
                l = l + 1
            print
    # set up password
        if (password != ''):
            self.dpb_ptr[l] = isc_dpb_password
            l = l + 1
            self.dpb_ptr[l] = len(password)
            l = l + 1

            for i in password:
                self.dpb_ptr[l] = ord(i)
                l = l + 1
            print

            self.dpb_length = l

#     def append_username(self, username):
#         username_ptr=c_char_p(username)
#         isc_expand_dpb(self.dpb_ptr,
#                        addressof(self.dpb_length),
#                        isc_dpb_user_name,
#                        username_ptr,
#                        None)

#     def append_password(self, password):
#         password_ptr=c_char_p(password)
#         isc_expand_dpb(self.dpb,
#                        addressof(self.dpb_length),
#                        isc_dpb_password,
#                        password_ptr,
#                        None)

class py_tpb:
    """
        transacion parameter buffer class
    """
    buffer_size = 255
    buffer = c_byte * buffer_size
    tpb_ptr = buffer()
    len = 0

    def length(self):
        return self.len

    def __str__(self):
        s = ''
        for i in range(self.buffer_size):
            c=str(self.tpb_ptr[i])
            s.join(c)
        return s

    def __init__(self, isolation_mode = isc_tpb_write,
                       lock_resolution = isc_tpb_concurrency,
                       conflict_resolution = isc_tpb_wait):
        self.tpb_ptr[0] = isc_tpb_version3
        self.tpb_ptr[1] = isc_tpb_read_committed #isolation_mode
        self.tpb_ptr[2] = isc_tpb_no_rec_version #lock_resolution
        self.tpb_ptr[3] = isc_tpb_wait #conflict_resolution
        self.len = c_int(4)

    def add_table_reservation(self,
                              access_method,
                              conflict_resolution,
                              table_name):
        self.len += 1
        self.tpb[self.len] = access_method
        self.len += 1
        self.tpb[self.len] = conflict_resolution
        self.len += 1
        for i in table_name :
            self.tpb[self.len] = ord(i)
            self.len += 1

        self.tpb[self.len] = 0
        self.len += 1


class py_status_vector:
    status_vector_len = 20
    status_vector = c_long * status_vector_len
    status_vector_ptr = status_vector()
        
    def __init__(self):
        for i in range(self.status_vector_len):
            self.status_vector_ptr[i] = c_long(0)

    def __str__(self):
        s = ''
        for i in range(self.status_vector_len):
            val=self.status_vector_ptr[i]
            c=str(val)
            s=s+' '+c
        return s

    def error(self):
        return (self.status_vector_ptr[0] == 1) and (self.status_vector_ptr[1] > 0)


class py_type_item:
    type_item_ptr = None
    type_item = None

    def __init__(self, size ):
        self.type_item = c_byte * size
        self.type_item_ptr = self.type_item()

    def address(self):
        return self.type_item

    def value(self, index):
        return self.type_item_ptr[index]

class py_buffer(object):
    length  = 0
    data_buffer_type = c_byte  * 1
    data_ptr = data_buffer_type()

    def __init__(self, size):
        self.length = size
        self.data_buffer_type = c_byte  * self.length
        self.data_ptr = self.data_buffer_type()

        for i in range(self.length):
            self.data_ptr[i] = 0

    def __str__(self):
        s = ''
        for i in range(self.length):
            code=self.data_ptr[i]
            s= s + ' ' + str(code)

        return s

    def address(self):
        return self.data_ptr

    def address2(self, offset=0):
        return addressof(self.data_ptr)+offset

class py_error_buffer(py_buffer):
    def __init__(self):
        super(py_error_buffer, self).__init__(512)

    def __str__(self):
        s = ''
        for i in range(self.length):
            code=self.data_ptr[i]
            if code== 0:
                break
            s= s  + chr(code)
        return s

class py_return_buffer(py_buffer):

    def __init__(self):
        super(py_return_buffer, self).__init__(32)

class py_info_items(py_buffer):

    def __init__(self, length):
        super(py_info_items, self).__init__(length)
