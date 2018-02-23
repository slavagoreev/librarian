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

class AcquireItem(object):
    """
    Represent a single item to be fetched by an Acquire object.
    
    It is not possible to construct instances of this class directly.
    Prospective users should construct instances of a subclass such as
    AcquireFile instead. It is not possible to create subclasses on the
    Python level, only on the C++ level.
    """
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    active_subprocess = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The name of the active subprocess (for instance, 'gzip', 'rred' or 'gpgv')."""

    complete = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """A boolean value determining whether the item has been fetched
completely"""

    desc_uri = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """A string describing the URI from which the item is acquired."""

    destfile = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The path to the file where the item will be stored."""

    error_text = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """If an error occured, a string describing the error; empty string
otherwise."""

    filesize = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The size of the file (number of bytes). If unknown, it is set to 0."""

    id = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The ID of the item. An integer which can be set by progress classes."""

    is_trusted = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Whether the item is trusted or not. Only True for packages
which come from a repository signed with one of the keys in
APT's keyring."""

    local = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Whether we are fetching a local item (copy:/) or not."""

    mode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Old name for active_subprocess"""

    partialsize = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The amount of data which has already been fetched (number of bytes)."""

    status = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """An integer representing the item's status which can be compared
against one of the STAT_* constants defined in this class."""


    STAT_AUTH_ERROR = 4
    STAT_DONE = 2
    STAT_ERROR = 3
    STAT_FETCHING = 1
    STAT_IDLE = 0
    STAT_TRANSIENT_NETWORK_ERROR = 5


