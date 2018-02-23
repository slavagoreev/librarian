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

from ._PackageManager import _PackageManager

class PackageManager(_PackageManager):
    """
    PackageManager(depcache: apt_pkg.DepCache)
    
    PackageManager objects allow the fetching of packages marked for
    installation and the installation of those packages. The parameter
    'depcache' specifies an apt_pkg.DepCache object where information
    about the package selections is retrieved from.
    
    Methods in this class can be overridden in sub classes
    to implement behavior different from APT's dpkg implementation.
    """
    def configure(self, pkg): # real signature unknown; restored from __doc__
        """
        configure(pkg: Package) -> bool 
        
        Add a configure action. Can be overridden in subclasses.
        
        New in version 0.8.0.
        """
        return False

    def go(self, status_fd): # real signature unknown; restored from __doc__
        """
        go(status_fd: int) -> bool 
        
        Start dpkg. Can be overridden in subclasses.
        
        New in version 0.8.0.
        """
        return False

    def install(self, pkg, filename): # real signature unknown; restored from __doc__
        """
        install(pkg: Package, filename: str) -> bool 
        
        Add a install action. Can be overridden in subclasses.
        
        New in version 0.8.0.
        """
        return False

    def remove(self, pkg, purge): # real signature unknown; restored from __doc__
        """
        remove(pkg: Package, purge: bool) -> bool 
        
        Add a removal action. Can be overridden in subclasses.
        
        New in version 0.8.0.
        """
        return False

    def reset(self): # real signature unknown; restored from __doc__
        """
        reset()
        
        Reset the package manager for a new round.
        Can be overridden in subclasses.
        
        New in version 0.8.0.
        """
        pass

    def __init__(self, depcache): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass


