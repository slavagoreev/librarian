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

class AcquireWorker(object):
    """
    Represent a sub-process responsible for fetching files from
    remote locations. This sub-process uses 'methods' located in
    the directory specified by the configuration option
    Dir::Bin::Methods.
    """
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    current_item = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The item currently being fetched, as an apt_pkg.AcquireItemDesc object."""

    current_size = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The amount of data fetched so far for the current item."""

    resumepoint = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The amount of data which was already available when the download was
started."""

    status = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The status of the worker, as a string."""

    total_size = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The total size of the item."""



