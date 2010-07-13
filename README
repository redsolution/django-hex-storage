==================
django-hex-storage
==================

File system storage with support of international file names and same file names.

For example:

1. You can upload to your server files with russian or turkish names. Such files will be urlified.

2. You can upload files with same names. Such files will have names with different random hex postfixes.


Installation:
=============

1. Put ``hex_storage`` to your ``INSTALLED_APPS`` in your ``settings.py`` within your django project.

2. Set your default file storage in your ``settings.py``::

    DEFAULT_FILE_STORAGE = 'hex_storage.HexFileSystemStorage'
