# -*- coding: utf-8 -*-

from django.core.files.storage import FileSystemStorage

import random

class HexFileSystemStorage(FileSystemStorage):
    def get_available_name(self, name):
        base_name = name
        try:
            dot_index = base_name.rindex('.')
            if base_name[dot_index:].find('/') != -1 or base_name[dot_index:].find('\\') != -1:
                raise ValueError
        except ValueError: # filename has no dot
            dot_index = len(base_name)
        while self.exists(name):
            name = base_name[:dot_index] + ('_%08X' % random.randint(0, 0x100000000)) + base_name[dot_index:]
        return name
