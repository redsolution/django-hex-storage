# -*- coding: utf-8 -*-

import os
import random

from django.core.files.storage import FileSystemStorage
from django.utils.encoding import smart_unicode
from pinyin.urlify import urlify

class HexFileSystemStorage(FileSystemStorage):
    def get_obfuscated_name(self, name):
        return '%s-%04x' % (name, random.randint(0, 0x10000))

    def get_first_name(self, name):
        return name

    def get_available_name(self, full_name):
        path, tail = os.path.split(full_name)
        source_name, ext = os.path.splitext(tail)
        source_name = urlify(source_name, max_length=None, remove_dots=False, default='noname', stop_words=[])
        if ext:
            ext = urlify(ext, max_length=None, remove_dots=False, default='', stop_words=[])
        name = self.get_first_name(source_name)

        while True:
            if not self.exists(path):
                break
            directories, files = self.listdir(path)
            for value in directories + files:
                if smart_unicode(os.path.splitext(value)[0]) == name:
                    break
            else:
                break
            name = self.get_obfuscated_name(source_name)
        return os.path.join(path, name + ext)
