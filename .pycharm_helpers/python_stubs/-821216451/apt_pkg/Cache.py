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

class Cache(object):
    """
    Cache([progress]) -> Cache() object.
    
    The APT cache file contains a hash table mapping names of binary
    packages to their metadata. A Cache object is the in-core
    representation of the same. It provides access to APT’s idea of the
    list of available packages.
    The optional parameter *progress* can be used to specify an 
    apt.progress.base.OpProgress() object (or similar) which reports
    progress information while the cache is being opened.  If this
    parameter is not supplied, the progress will be reported in simple,
    human-readable text to standard output. If it is None, no output
    will be made.
    
    The cache can be used like a mapping from package names to Package
    objects (although only getting items is supported). Instead of a name,
    a tuple of a name and an architecture may be used.
    """
    def update(self, progress, sources, pulse_interval): # real signature unknown; restored from __doc__
        """
        update(progress, sources: SourceList, pulse_interval: int) -> bool
        
        Update the index files used by the cache. A call to this method
        does not affect the current Cache object; instead, a new one
        should be created in order to use the changed index files.
        
        The parameter 'progress' can be used to specify an
        apt.progress.base.AcquireProgress() object , which will report
        progress information while the index files are being fetched.
        The parameter 'sources', if provided, is an apt_pkg.SourcesList
        object listing the remote repositories to be used.
        The 'pulse_interval' parameter indicates how long (in microseconds)
        to wait between calls to the pulse() method of the 'progress' object.
        The default is 500000 microseconds.
        """
        return False

    def __contains__(self, *args, **kwargs): # real signature unknown
        """ Return key in self. """
        pass

    def __getitem__(self, *args, **kwargs): # real signature unknown
        """ Return self[key]. """
        pass

    def __init__(self, progress=None): # real signature unknown; restored from __doc__
        pass

    def __len__(self, *args, **kwargs): # real signature unknown
        """ Return len(self). """
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    depends_count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The number of apt_pkg.Dependency objects stored in the cache."""

    file_list = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """A list of apt_pkg.PackageFile objects stored in the cache."""

    groups = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """A list of Group objects in the cache"""

    group_count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The number of apt_pkg.Group objects stored in the cache."""

    is_multi_arch = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Whether the cache supports multi-arch."""

    packages = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """A list of apt_pkg.Package objects stored in the cache."""

    package_count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The number of apt_pkg.Package objects stored in the cache."""

    package_file_count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The number of apt_pkg.PackageFile objects stored in the cache."""

    policy = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The PkgPolicy for the cache"""

    provides_count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Number of Provides relations described in the cache."""

    version_count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The number of apt_pkg.Version objects stored in the cache."""

    ver_file_count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The number of (Version, PackageFile) relations."""



