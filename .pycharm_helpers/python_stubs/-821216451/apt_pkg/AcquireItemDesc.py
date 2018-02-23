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

class AcquireItemDesc(object):
    """
    Provide the description of an item and the URI the item is
    fetched from. Progress classes make use of such objects to
    retrieve description and other information about an item.
    """
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    description = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """A string describing the item."""

    owner = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The owner of the item, an apt_pkg.AcquireItem object."""

    shortdesc = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """A short string describing the item (e.g. package name)."""

    uri = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The URI from which this item would be downloaded."""



