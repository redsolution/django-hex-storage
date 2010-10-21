==================
django-hex-storage
==================

File system storage with support of international file names and same file names.

For example:

1. You can upload to your server files with russian or turkish names. Such files will be urlified.
    
    ``Документ 1.doc`` becomes ``document_1.doc``

2. You can upload files with same names. Such files will have names with different random hex postfixes.

    Different files ``1.png`` and ``1.png`` becomes ``1.png`` and ``1_1BAC45.png`` rather than 
    ``1.png`` and ``1_.png`` in Django default filestorage

Installation:
=============

1. Put ``hex_storage`` to your ``INSTALLED_APPS`` in your ``settings.py`` within your django project. ::

    INSTALLED_APPS = [
        ...
        'hex_storage',
        ...
    ]

2. Set your default file storage in your ``settings.py``::

    DEFAULT_FILE_STORAGE = 'hex_storage.HexFileSystemStorage'

    
Classifiers:
-------------

`Utilities`_

.. _`Utilities`: http://www.redsolutioncms.org/classifiers/utilities