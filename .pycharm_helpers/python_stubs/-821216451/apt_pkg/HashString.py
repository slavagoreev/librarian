# encoding: utf-8
# module apt_pkg
# from /usr/lib/python3/dist-packages/apt_pkg.cpython-35m-x86_64-linux-gnu.so
# by generator 1.145
"""
Classes and functions wrapping the apt-pkg library.

The apt_pkg module provides several classes and functions for accessing
the functionality provided by the apt-pkg library. Typical uses might
include reading APT index files and configuration files and installing
or removing packages.
"""
# no imports

from .object import object

class HashString(object):
    """
    HashString(type, hash) OR HashString('type:hash')
    
    Create a new HashString object. The first form allows you to specify
    a type and a hash, and the second form a single string where type and
    hash are separated by a colon, e.g.::
    
       HashString('MD5Sum', '6cc1b6e6655e3555ac47e5b5fe26d04e')
    
    Valid options for 'type' are: MD5Sum, SHA1, SHA256.
    """
    def verify_file(self, filename): # real signature unknown; restored from __doc__
        """
        verify_file(filename: str) -> bool
        
        Verify that the file indicated by filename matches the hash.
        """
        return False

    def __init__(self, type, hash): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    def __str__(self, *args, **kwargs): # real signature unknown
        """ Return str(self). """
        pass

    hashtype = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The type of the hash, as a string (possible: MD5Sum,SHA1,SHA256)."""



