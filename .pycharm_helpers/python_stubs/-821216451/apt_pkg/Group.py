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

class Group(object):
    """
    Group(cache, name)
    
    Group of packages with the same name.
    
    Provides access to all packages sharing a name. Can be used this
    like a list, or by using the special find_*() methods. If you use
    it as a sequence, make sure to access it linearly, as this uses a
    linked list internally.
    """
    def find_package(self, architecture): # real signature unknown; restored from __doc__
        """
        find_package(architecture: str) -> Package
        
        Return a package for the given architecture, or None if none exists
        """
        return Package

    def find_preferred_package(self, prefer_non_virtual=True): # real signature unknown; restored from __doc__
        """
        find_preferred_package(prefer_non_virtual: bool = True) -> Package
        
        Return a package for the best architecture, either the native one
        or the first found one. If none exists, return None. If non_virtual
        is True, prefer non-virtual packages over virtual ones.
        """
        return Package

    def __getitem__(self, *args, **kwargs): # real signature unknown
        """ Return self[key]. """
        pass

    def __init__(self, cache, name): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass


