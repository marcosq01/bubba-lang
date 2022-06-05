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
        # locales
        self.local_int_count = 10000
        self.local_int_free = 5000
        self.local_float_count = 15000
        self.local_float_free = 4000
        self.local_string_count = 19000
        self.local_string_free = 1000
        # temporales
        self.temp_int_count = 20000
        self.temp_int_free = 2000
        self.temp_float_count = 22000
        self.temp_float_free = 2000
        self.temp_string_count = 24000
        self.temp_string_free = 1000
        # constantes
        self.const_int_count = 25000
        self.const_int_free = 2000
        self.const_float_count = 27000
        self.const_float_free = 1000
        self.const_string_count = 28000
        self.const_string_free = 1000

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
        self.local_int_count = 10000
        self.local_int_free = 5000
        self.local_float_count = 15000
        self.local_float_free = 4000
        self.local_string_count = 19000
        self.local_string_free = 1000

        # temporales
        self.temp_int_count = 20000
        self.temp_int_free = 2000
        self.temp_float_count = 22000
        self.temp_float_free = 2000
        self.temp_string_count = 24000
        self.temp_string_free = 1000