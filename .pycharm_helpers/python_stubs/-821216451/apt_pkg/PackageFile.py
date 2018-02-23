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

class PackageFile(object):
    """
    A package file is an index file stored in the cache with some
    additional pieces of information.
    """
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    architecture = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The architecture of the package file. Unused, empty string nowadays."""

    archive = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The archive of the package file (i.e. 'Suite' in the Release file)."""

    codename = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The codename of this package file (e.g. squeeze-updates)."""

    component = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The component of this package file (e.g. 'main')."""

    filename = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The path to the file."""

    id = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The numeric ID of this PackageFile object."""

    index_type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """A string describing the type of index. Known values are
'Debian Package Index', 'Debian Translation Index', and
'Debian dpkg status file'."""

    label = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The label set in the release file (e.g. 'Debian')."""

    not_automatic = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Whether the NotAutomatic flag is set in the Release file."""

    not_source = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Whether this package file lacks an active (sources.list) source;packages listed in such a file cannot be downloaded."""

    origin = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The origin set in the release file."""

    site = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The hostname of the location this file comes from."""

    size = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The size of the file."""

    version = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The version set in the release file (e.g. '5.0.X' for lenny, where X
is a point release)."""



