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

from .AcquireItem import AcquireItem

class AcquireFile(AcquireItem):
    """
    AcquireFile(owner, uri[, md5, size, descr, short_descr, destdir,destfile])
    
    Represent a file to be fetched. The parameter 'owner' points to
    an apt_pkg.Acquire object and the parameter 'uri' to the source
    location. Normally, the file will be stored in the current directory
    using the file name given in the URI. This directory can be changed
    by passing the name of a directory to the 'destdir' parameter. It is
    also possible to set a path to a file using the 'destfile' parameter,
    but both cannot be specified together.
    
    The parameters 'short_descr' and 'descr' can be used to specify
    a short description and a longer description for the item. This
    information is used by progress classes to refer to the item and
    should be short, for example, package name as 'short_descr' and
    and something like 'http://localhost sid/main python-apt 0.7.94.2'
    as 'descr'.
    The parameters 'md5' and 'size' are used to verify the resulting
    file. The parameter 'size' is also to calculate the total amount
    of data to be fetched and is useful for resuming a interrupted
    download.
    
    All parameters can be given by name (i.e. as keyword arguments).
    """
    def __init__(self, owner, uri, md5=None, size=None, descr=None, short_descr=None, destdir=None, destfile=None): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass


