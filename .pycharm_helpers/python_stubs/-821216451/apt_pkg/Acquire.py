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

class Acquire(object):
    """
    Acquire([progress: apt.progress.base.AcquireProgress])
    
    Coordinate the retrieval of files via network or local file system
    (using 'copy:/path/to/file' style URIs). The optional argument
    'progress' takes an apt.progress.base.AcquireProgress object
    which may report progress information.
    """
    def run(self): # real signature unknown; restored from __doc__
        """
        run() -> int
        
        Run the fetcher and return one of RESULT_CANCELLED,
        RESULT_CONTINUE, RESULT_FAILED.
        
        RESULT_CONTINUE means that all items which where queued prior to
        calling run() have been fetched successfully or failed transiently.
        
        RESULT_CANCELLED means canceled by the progress class.
        
        RESULT_FAILED means a generic failure.
        """
        return 0

    def shutdown(self): # real signature unknown; restored from __doc__
        """
        shutdown()
        
        Shut the fetcher down, removing all items from it. Future access to
        queued AcquireItem objects will cause a segfault. The partial result
        is kept on the disk and not removed and APT might reuse it.
        """
        pass

    def __init__(self, progress=None): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    fetch_needed = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The total amount of data to be fetched (number of bytes)."""

    items = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """A list of all items as apt_pkg.AcquireItem objects, including already
fetched ones and to be fetched ones."""

    partial_present = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The amount of data which is already available (number of bytes)."""

    total_needed = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The amount of data that needs to fetched plus the amount of data
which has already been fetched (number of bytes)."""

    workers = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """A list of all active workers as apt_pkg.AcquireWorker objects."""


    RESULT_CANCELLED = 2
    RESULT_CONTINUE = 0
    RESULT_FAILED = 1


