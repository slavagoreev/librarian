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

class DepCache(object):
    """
    DepCache(cache: apt_pkg.Cache)
    
    A DepCache() holds extra information on the state of the packages.
    
    The parameter 'cache' refers to an apt_pkg.Cache() object.
    """
    def commit(self, acquire_progress, install_progress): # real signature unknown; restored from __doc__
        """
        commit(acquire_progress, install_progress)
        
        Commit all the marked changes. This method takes two arguments,
        'acquire_progress' takes an apt.progress.base.AcquireProgress
        object and 'install_progress' an apt.progress.base.InstallProgress
        object.
        """
        pass

    def fix_broken(self): # real signature unknown; restored from __doc__
        """
        fix_broken() -> bool
        
        Fix broken packages.
        """
        return False

    def get_candidate_ver(self, pkg): # real signature unknown; restored from __doc__
        """
        get_candidate_ver(pkg: apt_pkg.Package) -> apt_pkg.Version
        
        Return the candidate version for the package, normally the version
        with the highest pin (changeable using set_candidate_ver).
        """
        pass

    def init(self, progress): # real signature unknown; restored from __doc__
        """
        init(progress: apt.progress.base.OpProgress)
        
        Initialize the depcache (done automatically when constructing
        the object).
        """
        pass

    def is_auto_installed(self, pkg): # real signature unknown; restored from __doc__
        """
        is_auto_installed(pkg: apt_pkg.Package) -> bool
        
        Check whether the package is marked as automatically installed.
        """
        return False

    def is_garbage(self, pkg): # real signature unknown; restored from __doc__
        """
        is_garbage(pkg: apt_pkg.Package) -> bool
        
        Check whether the package is garbage, i.e. whether it is automatically
        installed and the reverse dependencies are not installed anymore.
        """
        return False

    def is_inst_broken(self, pkg): # real signature unknown; restored from __doc__
        """
        is_inst_broken(pkg: apt_pkg.Package) -> bool
        
        Check whether the package is broken, ignoring marked changes.
        """
        return False

    def is_now_broken(self, pkg): # real signature unknown; restored from __doc__
        """
        is_now_broken(pkg: apt_pkg.Package) -> bool
        
        Check whether the package is broken, taking marked changes into account.
        """
        return False

    def is_upgradable(self, pkg): # real signature unknown; restored from __doc__
        """
        is_upgradable(pkg: apt_pkg.Package) -> bool
        
        Check whether the package is upgradable.
        """
        return False

    def marked_delete(self, pkg): # real signature unknown; restored from __doc__
        """
        marked_delete(pkg: apt_pkg.Package) -> bool
        
        Check whether the package is marked for removal.
        """
        return False

    def marked_downgrade(self, pkg): # real signature unknown; restored from __doc__
        """
        marked_downgrade(pkg: apt_pkg.Package) -> bool
        
        Check whether the package is marked for downgrade.
        """
        return False

    def marked_install(self, pkg): # real signature unknown; restored from __doc__
        """
        marked_install(pkg: apt_pkg.Package) -> bool
        
        Check whether the package is marked for installation.
        """
        return False

    def marked_keep(self, pkg): # real signature unknown; restored from __doc__
        """
        marked_keep(pkg: apt_pkg.Package) -> bool
        
        Check whether the package should be kept.
        """
        return False

    def marked_reinstall(self, pkg): # real signature unknown; restored from __doc__
        """
        marked_reinstall(pkg: apt_pkg.Package) -> bool
        
        Check whether the package is marked for re-installation.
        """
        return False

    def marked_upgrade(self, pkg): # real signature unknown; restored from __doc__
        """
        marked_upgrade(pkg: apt_pkg.Package) -> bool
        
        Check whether the package is marked for upgrade.
        """
        return False

    def mark_auto(self, pkg, auto): # real signature unknown; restored from __doc__
        """
        mark_auto(pkg: apt_pkg.Package, auto: bool)
        
        Mark package as automatically installed (if auto=True),
        or as not automatically installed (if auto=False).
        """
        pass

    def mark_delete(self, pkg, purge=False): # real signature unknown; restored from __doc__
        """
        mark_delete(pkg: apt_pkg.Package[, purge: bool = False])
        
        Mark package for deletion, and if 'purge' is True also for purging.
        """
        pass

    def mark_install(self, pkg, auto_inst=True, from_user=True): # real signature unknown; restored from __doc__
        """
        mark_install(pkg: apt_pkg.Package[, auto_inst=True, from_user=True])
        
        Mark the package for installation. The parameter 'auto_inst' controls
        whether the dependencies of the package are marked for installation
        as well. The parameter 'from_user' controls whether the package is
        registered as NOT automatically installed.
        """
        pass

    def mark_keep(self, pkg): # real signature unknown; restored from __doc__
        """
        mark_keep(pkg: apt_pkg.Package)
        
        Mark package to be kept.
        """
        pass

    def minimize_upgrade(self): # real signature unknown; restored from __doc__
        """
        minimize_upgrade() -> bool
        
        Go over the entire set of packages and try to keep each package
        marked for upgrade. If a conflict is generated then the package
        is restored.
        """
        return False

    def read_pinfile(self, file=None): # real signature unknown; restored from __doc__
        """
        read_pinfile([file: str])
        
        Read the pin policy
        """
        pass

    def set_candidate_release(self, pkg, ver, rel): # real signature unknown; restored from __doc__
        """
        set_candidate_release(pkg: apt_pkg.Package, ver: apt_pkg.Version, rel: string) -> bool
        
        Sets not only the candidate version 'ver' for package 'pkg', but walks also down the dependency tree and checks if it is required to set the candidate of the dependency to a version from the given release string 'rel', too.
        """
        return False

    def set_candidate_ver(self, pkg, ver): # real signature unknown; restored from __doc__
        """
        set_candidate_ver(pkg: apt_pkg.Package, ver: apt_pkg.Version) -> bool
        
        Set the candidate version of 'pkg' to 'ver'.
        """
        return False

    def set_reinstall(self, pkg, reinstall): # real signature unknown; restored from __doc__
        """
        set_reinstall(pkg: apt_pkg.Package, reinstall: bool)
        
        Set whether the package should be reinstalled (reinstall = True or False).
        """
        pass

    def upgrade(self, dist_upgrade=True): # real signature unknown; restored from __doc__
        """
        upgrade([dist_upgrade: bool = True]) -> bool
        
        Mark the packages for upgrade under the same conditions apt-get
        upgrade does. If 'dist_upgrade' is True, also allow packages to
        be upgraded if they require installation/removal of other packages;
        just like apt-get dist-upgrade.
        """
        return False

    def __init__(self, cache): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    broken_count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The number of packages with broken dependencies in the cache."""

    deb_size = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The size of the packages which are needed for the changes to be
applied."""

    del_count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The number of packages marked for removal."""

    inst_count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The number of packages marked for installation."""

    keep_count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The number of packages marked for keep."""

    policy = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The apt_pkg.Policy object used by this cache."""

    usr_size = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The amount of space required for installing/removing the packages,
i.e. the Installed-Size of all packages marked for installation
minus the Installed-Size of all packages for removal."""



