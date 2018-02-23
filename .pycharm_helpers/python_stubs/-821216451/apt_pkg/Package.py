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

class Package(object):
    """
    Represent a package. A package is uniquely identified by its name
    and each package can have zero or more versions which can be
    accessed via the version_list property. Packages can be installed
    and removed by apt_pkg.DepCache.
    """
    def get_fullname(self, pretty=False): # real signature unknown; restored from __doc__
        """
        get_fullname([pretty: bool = False]) -> str
        
        Get the full name of the package, including the architecture. If
        'pretty' is True, the architecture is omitted for native packages,
        that is, and amd64 apt package on an amd64 system would give 'apt'.
        """
        return ""

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    architecture = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The architecture of the package."""

    current_state = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The current state, which can be compared against the constants
CURSTATE_CONFIG_FILES, CURSTATE_HALF_CONFIGURED,
CURSTATE_HALF_INSTALLED, CURSTATE_INSTALLED, CURSTATE_NOT_INSTALLED,
CURSTATE_UNPACKED of the apt_pkg module."""

    current_ver = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The version of the package currently installed or None."""

    essential = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Boolean value determining whether the package is essential."""

    has_provides = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Whether the package is provided by at least one other package."""

    has_versions = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Whether the package has at least one version in the cache."""

    id = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The numeric ID of the package"""

    important = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Boolean value determining whether the package has the 'important'
flag set ('Important: yes' in the Packages file). No longer used."""

    inst_state = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The state of the install, which be compared against the constants
INSTSTATE_HOLD, INSTSTATE_HOLD_REINSTREQ, INSTSTATE_OK,
INSTSTATE_REINSTREQ of the apt_pkg module."""

    name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The name of the package."""

    provides_list = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """A list of all packages providing this package. The list contains
tuples in the format (providesname, providesver, version)
where 'version' is an apt_pkg.Version object."""

    rev_depends_list = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """An apt_pkg.DependencyList object of all reverse dependencies."""

    section = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The section of the package."""

    selected_state = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The state of the selection, which can be compared against the constants
SELSTATE_DEINSTALL, SELSTATE_HOLD, SELSTATE_INSTALL, SELSTATE_PURGE,
SELSTATE_UNKNOWN of the apt_pkg module."""

    version_list = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """A list of all apt_pkg.Version objects for this package."""



