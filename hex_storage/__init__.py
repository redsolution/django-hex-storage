# -*- coding: utf-8 -*-

from django.core.files.storage import FileSystemStorage
from pinyin.urlify import urlify

import random
import os

class FileWasFound(BaseException):
    pass

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
            try:
                if not self.exists(path):
                    break
                directories, files = self.listdir(path)
                for directory in directories:
                    if directory == name + ext:
                        raise FileWasFound()
                for file in files:
                    if unicode(os.path.splitext(file)[0]) == name:
                        raise FileWasFound()
                break
            except FileWasFound:
                name = source_name + ('-%08x' % random.randint(0, 0x100000000))
        return os.path.join(path, name + ext)
