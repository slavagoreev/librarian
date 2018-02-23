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

class Hashes(object):
    """
    Hashes([object: (bytes, file)])
    
    Calculate hashes for the given object. It can be used to create all
    supported hashes for a file.
    
    The parameter 'object' can be a bytestring, an object providing the
    fileno() method, or an integer describing a file descriptor.
    """
    def __init__(self, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    md5 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The MD5Sum of the file as a string."""

    sha1 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The SHA1Sum of the file as a string."""

    sha256 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The SHA256Sum of the file as a string."""



