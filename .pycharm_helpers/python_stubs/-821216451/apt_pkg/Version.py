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

class Version(object):
    """ Version Object """
    def __eq__(self, *args, **kwargs): # real signature unknown
        """ Return self==value. """
        pass

    def __ge__(self, *args, **kwargs): # real signature unknown
        """ Return self>=value. """
        pass

    def __gt__(self, *args, **kwargs): # real signature unknown
        """ Return self>value. """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __le__(self, *args, **kwargs): # real signature unknown
        """ Return self<=value. """
        pass

    def __lt__(self, *args, **kwargs): # real signature unknown
        """ Return self<value. """
        pass

    def __ne__(self, *args, **kwargs): # real signature unknown
        """ Return self!=value. """
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    arch = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The architecture of this specific version of the package."""

    depends_list = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """A dictionary mapping dependency types to lists (A) of lists (B) of
apt_pkg.Dependency objects. The lists (B) represent or dependencies
like 'a || b'."""

    depends_list_str = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Same as depends_list, except that the apt_pkg.Dependency objects
are 3-tuples of the form (name, version, operator); where operator
is one of '<', '<=', '=', '>=', '>'."""

    downloadable = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Whether the version can be downloaded."""

    file_list = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """A list of tuples (packagefile: apt_pkg.PackageFile, index: int) for the
PackageFile objects related to this package. The index can be used
to retrieve the record of this package version."""

    hash = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The numeric hash of the version used in the internal storage."""

    id = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The numeric ID of the package."""

    installed_size = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The installed size of this package version."""

    multi_arch = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Multi-arch state of this package, as an integer. See
the various MULTI_ARCH_* members."""

    parent_pkg = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The parent package of this version."""

    priority = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The priority of the package as an integer, which can be compared to
the constants PRI_EXTRA, PRI_IMPORTANT, PRI_OPTIONAL, PRI_REQUIRED,
PRI_STANDARD of the apt_pkg module."""

    priority_str = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The priority of the package, as a string."""

    provides_list = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """A list of all packages provided by this version. The list contains
tuples in the format (providesname, providesver, version)
where 'version' is an apt_pkg.Version object."""

    section = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The section of this package version."""

    size = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The size of the package file."""

    translated_description = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """An apt_pkg.Description object for the translated description if
available or the untranslated fallback."""

    ver_str = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The version string."""


    MULTI_ARCH_ALL = 1
    MULTI_ARCH_ALLOWED = 8
    MULTI_ARCH_ALL_ALLOWED = 9
    MULTI_ARCH_ALL_FOREIGN = 3
    MULTI_ARCH_FOREIGN = 2
    MULTI_ARCH_NO = 0
    MULTI_ARCH_NONE = 0
    MULTI_ARCH_SAME = 4
    __hash__ = None


