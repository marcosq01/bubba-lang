import tempfile
from .utils.constants import *

class AddressManager:

    def __init__(self) -> None:
        # globales
        self.global_int_count = GLOBAL_INT_START
        self.global_int_free = GLOBAL_INT_FREE
        self.global_float_count = GLOBAL_FLOAT_START
        self.global_float_free = GLOBAL_FLOAT_FREE
        self.global_string_count = GLOBAL_STRING_START
        self.global_string_free = GLOBAL_STRING_FREE

        # objetos globales
        self.global_object_attr_count = GLOBAL_OBJECT_START
        self.global_object_attr_free = GLOBAL_OBJECT_FREE

        # locales
        self.local_int_count = LOCAL_INT_START
        self.local_int_free = LOCAL_INT_FREE
        self.local_float_count = LOCAL_FLOAT_START
        self.local_float_free = LOCAL_FLOAT_FREE
        self.local_string_count = LOCAL_STRING_START
        self.local_string_free = LOCAL_STRING_FREE

        # objetos locales
        self.local_object_attr_count = LOCAL_OBJECT_FREE
        self.local_object_attr_free = LOCAL_OBJECT_FREE

        # temporales
        self.temp_int_count = TEMP_INT_START
        self.temp_int_free = TEMP_INT_FREE
        self.temp_float_count = TEMP_FLOAT_START
        self.temp_float_free = TEMP_FLOAT_FREE
        self.temp_string_count = TEMP_STRING_START
        self.temp_string_free = TEMP_STRING_FREE
        # constantes
        self.const_int_count = CONST_INT_START
        self.const_int_free = CONST_INT_FREE
        self.const_float_count = CONST_FLOAT_START
        self.const_float_free = CONST_FLOAT_FREE
        self.const_string_count = CONST_STRING_START
        self.const_string_free = CONST_STRING_FREE

    def get_global_int(self, n):
        if self.global_int_free >= n:
            temp = self.global_int_count
            self.global_int_count += n
            self.global_int_free -= n
            return temp
        else:
            return -1

    def get_global_float(self, n):
        if self.global_float_free >= n:
            temp = self.global_float_count
            self.global_float_count += n
            self.global_float_free -= n
            return temp
        else:
            return -1

    def get_global_string(self, n):
        if self.global_string_free >= n:
            temp = self.global_string_count
            self.global_string_count += n
            self.global_string_free -= n
            return temp
        else:
            return -1

    def get_global_object_attr(self, n):
        if self.global_object_attr_free >= n:
            temp = self.global_object_attr_count
            self.global_object_attr_count += n
            self.global_object_attr_free -= n
            return temp
        else:
            return -1

    def get_local_int(self, n):
        if self.local_int_free >= n:
            temp = self.local_int_count
            self.local_int_count += n
            self.local_int_free -= n
            return temp
        else:
            return -1

    def get_local_float(self, n):
        if self.local_float_free >= n:
            temp = self.local_float_count
            self.local_float_count += n
            self.local_float_free -= n
            return temp
        else:
            return -1

    def get_local_string(self, n):
        if self.local_string_free >= n:
            temp = self.local_string_count
            self.local_string_count += n
            self.local_string_free -= n
            return temp
        else:
            return -1

    def get_local_object_attr(self, n):
        if self.local_object_attr_free >= n:
            temp = self.local_object_attr_count
            self.local_object_attr_count += n
            self.local_object_attr_free -= n
            return temp
        else:
            return -1

    def get_temp_int(self, n):
        if self.temp_int_free >= n:
            temp = self.temp_int_count
            self.temp_int_count += n
            self.temp_int_free -= n
            return temp
        else:
            return -1


    def get_temp_float(self, n):
        if self.temp_float_free >= n:
            temp = self.temp_float_count
            self.temp_float_count += n
            self.temp_float_free -= n
            return temp
        else:
            return -1

    def get_temp_string(self, n):
        if self.temp_string_free >= n:
            temp = self.temp_string_count
            self.temp_string_count += n
            self.temp_string_free -= n
            return temp
        else:
            return -1

    def get_const_int(self, n):
        if self.const_int_free >= n:
            temp = self.const_int_count
            self.const_int_count += n
            self.const_int_free -= n
            return temp
        else:
            return -1


    def get_const_float(self, n):
        if self.const_float_free >= n:
            temp = self.const_float_count
            self.const_float_count += n
            self.const_float_free -= n
            return temp
        else:
            return -1

    def get_const_string(self, n):
        if self.const_string_free >= n:
            temp = self.const_string_count
            self.const_string_count += n
            self.const_string_free -= n
            return temp
        else:
            return -1

    def reset(self):
        # locales
        self.local_int_count = LOCAL_INT_START
        self.local_int_free = LOCAL_INT_FREE
        self.local_float_count = LOCAL_FLOAT_START
        self.local_float_free = LOCAL_FLOAT_FREE
        self.local_string_count = LOCAL_STRING_START
        self.local_string_free = LOCAL_STRING_FREE

        # objetos locales
        self.local_object_attr_count = LOCAL_OBJECT_START
        self.local_float_free = LOCAL_OBJECT_FREE

        # temporales
        self.temp_int_count = TEMP_INT_START
        self.temp_int_free = TEMP_INT_FREE
        self.temp_float_count = TEMP_FLOAT_START
        self.temp_float_free = TEMP_FLOAT_FREE
        self.temp_string_count = TEMP_STRING_START
        self.temp_string_free = TEMP_STRING_FREE