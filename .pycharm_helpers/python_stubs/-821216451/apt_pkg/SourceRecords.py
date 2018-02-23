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

class SourceRecords(object):
    """
    SourceRecords()
    
    Provide an easy way to look up the records of source packages and
    provide easy attributes for some widely used fields of the record.
    """
    def lookup(self, name): # real signature unknown; restored from __doc__
        """
        lookup(name: str) -> bool
        
        Look up the source package with the given name. Each call moves
        the position of the records parser forward. If there are no
        more records, return None. If the lookup failed this way,
        access to any of the attributes will result in an AttributeError.
        """
        return False

    def restart(self): # real signature unknown; restored from __doc__
        """
        restart()
        
        Restart the lookup process. This moves the parser to the first
        package and lookups can now be made just like on a new object.
        """
        pass

    def step(self): # real signature unknown; restored from __doc__
        """
        step() -> bool
        
        Go to the source package. Each call moves
        the position of the records parser forward. If there are no
        more records, return None. If the lookup failed this way,
        access to any of the attributes will result in an AttributeError.
        """
        return False

    def __init__(self): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    binaries = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """A list of the names of the binaries produced by this source package."""

    build_depends = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """A dictionary describing the build-time dependencies of the package;
the format is the same as used for apt_pkg.Version.depends_list_str."""

    files = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """A list of tuples (md5: str, size: int, path: str, type: str), whereas
'type' can be 'diff' (includes .debian.tar.gz), 'dsc', 'tar'."""

    index = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The index file associated with this record as a list of
apt_pkg.IndexFile objects."""

    maintainer = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The maintainer of the package."""

    package = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The name of the source package."""

    record = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The raw record, suitable for parsing using apt_pkg.TagSection."""

    section = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The section of the source package."""

    version = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The version of the source package."""



