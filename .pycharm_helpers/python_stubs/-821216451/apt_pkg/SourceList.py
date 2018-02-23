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

class SourceList(object):
    """
    SourceList()
    
    Represent the list of sources stored in /etc/apt/sources.list and
    similar files.
    """
    def find_index(self, pkgfile): # real signature unknown; restored from __doc__
        """
        find_index(pkgfile: apt_pkg.PackageFile) -> apt_pkg.IndexFile
        
        Return the index file for the given package file, or None if none
        could be found.
        """
        pass

    def get_indexes(self, acquire, all=False): # real signature unknown; restored from __doc__
        """
        get_indexes(acquire: apt_pkg.Acquire[, all: bool=False]) -> bool
        
        Add all indexes (i.e. stuff like Release files, Packages files)
        to the Acquire object 'acquire'. If 'all' is True, all indexes
        will be added, otherwise only changed indexes will be added.
        """
        return False

    def read_main_list(self): # real signature unknown; restored from __doc__
        """
        read_main_list() -> bool
        
        Read /etc/apt/sources.list and similar files to populate the list
        of indexes.
        """
        return False

    def __init__(self): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    list = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """A list of MetaIndex() objects."""



