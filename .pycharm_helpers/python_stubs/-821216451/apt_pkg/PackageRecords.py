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

class PackageRecords(object):
    """
    PackageRecords(cache: apt_pkg.Cache)
    
    Package Records contain information about packages. Those objects
    can be used to retrieve information such as maintainer or filename
    of a package. They can also be used to retrieve the raw records
    of the packages (i.e. those stanzas stored in Packages files).
    """
    def lookup(self, (packagefile, index)): # real signature unknown; restored from __doc__
        """
        lookup((packagefile: apt_pkg.PackageFile, index: int)) -> bool
        
        Changes to a new package
        """
        return False

    def __init__(self, cache): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    filename = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The filename of the package, as stored in the 'Filename' field."""

    homepage = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The homepage of the package, as stored in the 'Homepage' field."""

    long_desc = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The long description of the packages; i.e. all lines in the
'Description' field except for the first one."""

    maintainer = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The maintainer of the package, as stored in the 'Maintainer' field."""

    md5_hash = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The MD5 hash value of the package, as stored in the 'MD5Sum' field."""

    name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The name of the package, as stored in the 'Package' field."""

    record = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The raw record, suitable for parsing by apt_pkg.TagSection."""

    sha1_hash = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The SHA1 hash value, as stored in the 'SHA1' field."""

    sha256_hash = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The SHA256 hash value, as stored in the 'SHA256' field."""

    short_desc = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The short description of the package, i.e. the first line of the
'Description' field."""

    source_pkg = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The name of the source package, if different from the name of the
binary package. This information is retrieved from the 'Source' field."""

    source_ver = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The version of the source package, if it differs from the version
of the binary package. Just like 'source_pkg', this information
is retrieved from the 'Source' field."""



