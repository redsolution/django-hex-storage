# -*- coding: utf-8 -*-

from django.core.files.storage import FileSystemStorage
from pinyin.urlify import urlify

import random
import os

class HexFileSystemStorage(FileSystemStorage):
    def get_available_name(self, full_name):
        path, tail = os.path.split(full_name)
        name, ext = os.path.splitext(tail)
        name = urlify(name)
        if ext:
            if ext.startswith('.'):
                ext = '.' + urlify(ext[1:])
            else:
                ext = urlify(ext)
        source_name = name

        while True:
            result = os.path.join(path, name + ext)
            if not self.exists(result):
                break
            name = source_name + ('-%08x' % random.randint(0, 0x100000000))
        return result
