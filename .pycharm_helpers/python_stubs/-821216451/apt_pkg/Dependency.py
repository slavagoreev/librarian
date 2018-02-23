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

class Dependency(object):
    """
    Represent a dependency from one package version to a package,
    and (optionally) a version relation (e.g. >= 1). Dependency
    objects also provide useful functions like all_targets() or
    smart_target_pkg() for selecting packages to satisfy the
    dependency.
    """
    def all_targets(self): # real signature unknown; restored from __doc__
        """
        all_targets() -> list
        
        A list of all possible apt_pkg.Version objects which satisfy this
        dependency.
        """
        return []

    def smart_target_pkg(self): # real signature unknown; restored from __doc__
        """
        smart_target_pkg() -> apt_pkg.Package
        
        Return the first package which provides a package with the name
        of the target package.
        """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    comp_type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The type of comparison in mathematical notation, as a string, namely one of:
'<', '<=', '=', '!=', '>=', '>', ''.
The empty string will be returned in case of an unversioned dependency."""

    comp_type_deb = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The type of comparison in Debian notation, as a string, namely one of:
'<<', '<=', '=', '!=', '>=', '>>', ''.
The empty string will be returned in case of an unversioned dependency.
For details see the Debian Policy Manual on the syntax of relationship fields:
https://www.debian.org/doc/debian-policy/ch-relationships.html#s-depsyntax"""

    dep_type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The type of the dependency; may be translated"""

    dep_type_enum = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Same as dep_type, but with a numeric value instead of a string. Can
be compared against the TYPE_ constants defined in this class."""

    dep_type_untranslated = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Same as dep_type, but guaranteed to be untranslated."""

    id = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The numeric ID of this dependency object."""

    parent_pkg = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The apt_pkg.Package object of the package which depends."""

    parent_ver = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The apt_pkg.Version object of the package which depends."""

    target_pkg = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The apt_pkg.Package object of the package depended upon"""

    target_ver = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The version of the package depended upon as a string"""


    TYPE_CONFLICTS = 5
    TYPE_DEPENDS = 1
    TYPE_DPKG_BREAKS = 8
    TYPE_ENHANCES = 9
    TYPE_OBSOLETES = 7
    TYPE_PREDEPENDS = 2
    TYPE_RECOMMENDS = 4
    TYPE_REPLACES = 6
    TYPE_SUGGESTS = 3


