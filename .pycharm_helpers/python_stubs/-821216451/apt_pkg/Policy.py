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

class Policy(object):
    """
    Policy(cache)
    
    Representation of the policy of the Cache object given by cache. This
    provides a superset of policy-related functionality compared to the
    DepCache class. The DepCache can be used for most purposes, but there
    may be some cases where a special policy class is needed.
    """
    def create_pin(self, type, pkg, data, priority): # real signature unknown; restored from __doc__
        """
        create_pin(type: str, pkg: str, data: str, priority: int)
        
        Create a pin for the policy. The parameter 'type' refers to one of the
        strings 'Version', 'Release', or 'Origin'. The argument 'pkg' is the
        name of the package. The parameter 'data' refers to the value
        (e.g. 'unstable' for type='Release') and the other possible options.
        The parameter 'priority' gives the priority of the pin.
        """
        pass

    def get_candidate_ver(self, *args, **kwargs): # real signature unknown
        """
        get_match(package: apt_pkg.Package) -> apt_pkg.Version
        
        Get the best package for the job.
        """
        pass

    def get_match(self, package): # real signature unknown; restored from __doc__
        """
        get_match(package: apt_pkg.Package) -> apt_pkg.Version
        
        Return a matching version for the given package.
        """
        pass

    def get_priority(self, package): # real signature unknown; restored from __doc__
        """
        get_priority(package: apt_pkg.Package) -> int
        
        Return the priority of the package.
        """
        return 0

    def read_pindir(self, dirname): # real signature unknown; restored from __doc__
        """
        read_pindir(dirname: str) -> bool
        
        Read the pin files in the given dir (e.g. '/etc/apt/preferences.d')
        and add them to the policy.
        """
        return False

    def read_pinfile(self, filename): # real signature unknown; restored from __doc__
        """
        read_pinfile(filename: str) -> bool
        
        Read the pin file given by filename (e.g. '/etc/apt/preferences')
        and add it to the policy.
        """
        return False

    def __init__(self, cache): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass


