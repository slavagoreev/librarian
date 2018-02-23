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

class SystemLock(object):
    """
    SystemLock()
    
    Context manager for locking the package system. The lock is established
    as soon as the method __enter__() is called. It is released when
    __exit__() is called.
    
    This should be used via the 'with' statement, for example:
    
       with apt_pkg.SystemLock():
           ...
    
    Once the block is left, the lock is released automatically. The object
    can be used multiple times:
    
       lock = apt_pkg.SystemLock()
       with lock:
           ...
       with lock:
           ...
    """
    def __enter__(self, *args, **kwargs): # real signature unknown
        """ Lock the system. """
        pass

    def __exit__(self, *args, **kwargs): # real signature unknown
        """ Unlock the system. """
        pass

    def __init__(self): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass


