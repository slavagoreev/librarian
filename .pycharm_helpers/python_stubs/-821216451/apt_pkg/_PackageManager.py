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

class _PackageManager(object):
    """
    _PackageManager objects allow the fetching of packages marked for
    installation and the installation of those packages.
    This is an abstract base class that cannot be subclassed
    in Python. The only subclass is apt_pkg.PackageManager. This
    class is an implementation-detail and not part of the API.
    """
    def do_install(self, status_fd): # real signature unknown; restored from __doc__
        """
        do_install(status_fd: int) -> int
        
        Install the packages and return one of the class constants
        RESULT_COMPLETED, RESULT_FAILED, RESULT_INCOMPLETE. The argument
        status_fd can be used to specify a file descriptor that APT will
        write status information on (see README.progress-reporting in the
        apt source code for information on what will be written there).
        """
        return 0

    def fix_missing(self): # real signature unknown; restored from __doc__
        """
        fix_missing() -> bool
        
        Fix the installation if a package could not be downloaded.
        """
        return False

    def get_archives(self, fetcher, p_list, recs): # real signature unknown; restored from __doc__
        """
        get_archives(fetcher: Acquire, list: SourceList, recs: PackageRecords) -> bool
        
        Download the packages marked for installation via the Acquire object
        'fetcher', using the information found in 'list' and 'recs'.
        """
        return False

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    RESULT_COMPLETED = 0
    RESULT_FAILED = 1
    RESULT_INCOMPLETE = 2


