# -*- coding: utf-8 -*-

import os
import random

from django.core.files.storage import FileSystemStorage
from django.utils.encoding import smart_unicode
from pinyin.urlify import urlify

class FileWasFound(BaseException):
    pass

class HexFileSystemStorage(FileSystemStorage):
    def get_available_name(self, full_name):
        path, tail = os.path.split(full_name)
        name, ext = os.path.splitext(tail)
        name = urlify(name, max_length=None, remove_dots=False)
        if ext:
            ext = urlify(ext, max_length=None, remove_dots=False)
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
                    if smart_unicode(os.path.splitext(file)[0]) == name:
                        raise FileWasFound()
                break
            except FileWasFound:
                name = source_name + ('-%04x' % random.randint(0, 0x10000))
        return os.path.join(path, name + ext)
