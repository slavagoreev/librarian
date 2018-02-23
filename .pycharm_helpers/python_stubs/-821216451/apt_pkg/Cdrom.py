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

class Cdrom(object):
    """
    Cdrom()
    
    Cdrom objects can be used to identify Debian installation media and to
    add them to /etc/apt/sources.list.
    """
    def add(self, progress): # real signature unknown; restored from __doc__
        """
        add(progress: apt_pkg.CdromProgress) -> bool
        
        Add the given CD-ROM to the sources.list. Return True on success;
        raise an error on failure or return False.
        """
        return False

    def ident(self, progress): # real signature unknown; restored from __doc__
        """
        ident(progress: apt_pkg.CdromProgress) -> str
        
        Try to identify the CD-ROM and if successful return the hexadecimal
        CDROM-ID (and a integer version suffix separated by -) as a
        string. Otherwise, return None or raise an error.
        
        The ID is created by hashing all file and directory names on the
        CD-ROM and appending the version.
        """
        return ""

    def __init__(self): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass


