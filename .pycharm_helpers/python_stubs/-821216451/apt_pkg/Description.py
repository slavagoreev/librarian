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

class Description(object):
    """
    Represent a package description and some attributes. Needed for
    things like translated descriptions.
    """
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    file_list = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """A list of all apt_pkg.PackageFile objects related to this description."""

    language_code = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The language code of the description. Empty string for untranslated
descriptions."""

    md5 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The MD5 hash of the description."""



