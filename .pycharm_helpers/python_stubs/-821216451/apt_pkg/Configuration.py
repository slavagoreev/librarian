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

class Configuration(object):
    """
    Configuration()
    
    Represent the configuration of APT by mapping option keys to
    values and storing configuration parsed from files like
    /etc/apt/apt.conf. The most important Configuration object
    is apt_pkg.config which points to the global configuration
    object. Other top-level Configuration objects can be created
    by calling the constructor, but there is usually no reason to.
    """
    def clear(self, key): # real signature unknown; restored from __doc__
        """
        clear(key: str)
        
        Remove the specified option and all sub-options.
        """
        pass

    def dump(self): # real signature unknown; restored from __doc__
        """
        dump() -> str
        
        Return a string dump this Configuration object.
        """
        return ""

    def exists(self, key): # real signature unknown; restored from __doc__
        """
        exists(key: str) -> bool
        
        Check whether the given key exists.
        """
        return False

    def find(self, key, default=''): # real signature unknown; restored from __doc__
        """
        find(key: str[, default: str = '']) -> str
        
        Find the value for the given key and return it. If the
        given key does not exist, return default instead.
        """
        return ""

    def find_b(self, *args, **kwargs): # real signature unknown
        """
        find_i(key: str[, default: bool = False]) -> bool
        
        Same as find, but for boolean values; returns False on unknown values.
        """
        pass

    def find_dir(self, key, default=''): # real signature unknown; restored from __doc__
        """
        find_dir(key: str[, default: str = '']) -> str
        
        Same as find_file(), but for directories. The difference is
        that this function adds a trailing slash to the result.
        """
        return ""

    def find_file(self, key, default=''): # real signature unknown; restored from __doc__
        """
        find_file(key: str[, default: str = '']) -> str
        
        Same as find(), but for filenames. In the APT configuration, there
        is a special section Dir:: for storing filenames. find_file() locates
        the given key and then goes up and prepends the directory names to the
        return value. For example, for:
        
            apt_pkg.config['Dir'] = 'a'
            apt_pkg.config['Dir::D'] = 'b'
            apt_pkg.config['Dir::D::F'] = 'c'
        
        find_file('Dir::D::F') returns 'a/b/c'. There is also a special
        configuration setting RootDir which will always be prepended to the
        result (the default being ''). Thus, if RootDir is 'x', the example
        would return 'x/a/b/c'.
        """
        return ""

    def find_i(self, key, default=0): # real signature unknown; restored from __doc__
        """
        find_i(key: str[, default: int = 0]) -> int
        
        Same as find, but for integer values.
        """
        return 0

    def get(self, *args, **kwargs): # real signature unknown
        """
        find(key: str[, default: str = '']) -> str
        
        Find the value for the given key and return it. If the
        given key does not exist, return default instead.
        """
        pass

    def keys(self, root=None): # real signature unknown; restored from __doc__
        """
        keys([root: str]) -> list
        
        Return a list of all keys in the configuration object. If 'root'
        is given, limit the list to those below the root.
        """
        return []

    def list(self, root=None): # real signature unknown; restored from __doc__
        """
        list([root: str]) -> list
        
        Return a list of all items at the given root, using their full
        name. For example, in a configuration object where the options A,
        B, and B::C are set, the following expressions evaluate to True:
        
           conf.list() == ['A', 'B']
           conf.list('A') == ['']
           conf.list('B') == ['B::C']
        """
        return []

    def my_tag(self): # real signature unknown; restored from __doc__
        """
        my_tag() -> str
        
        Return the tag of the root of this Configuration object. For the
        default object, this is an empty string. For a subtree('APT') of
        such an object, it would be 'APT' (given as an example).
        """
        return ""

    def set(self, key, value): # real signature unknown; restored from __doc__
        """
        set(key: str, value: str)
        
        Set the given key to the given value. To set int or bool values,
        encode them using str(value) and then use find_i()/find_b()
        to retrieve their value again.
        """
        pass

    def subtree(self, key): # real signature unknown; restored from __doc__
        """
        subtree(key: str) -> apt_pkg.Configuration
        
        Return a new apt_pkg.Configuration object with the given option
        as its root. Example:
        
            apttree = config.subtree('APT')
            apttree['Install-Suggests'] = config['APT::Install-Suggests']
        """
        pass

    def value_list(self, root=None): # real signature unknown; restored from __doc__
        """
        value_list([root: str]) -> list
        
        Same as list(), but instead of returning the keys, return the values.
        """
        return []

    def __contains__(self, *args, **kwargs): # real signature unknown
        """ Return key in self. """
        pass

    def __delitem__(self, *args, **kwargs): # real signature unknown
        """ Delete self[key]. """
        pass

    def __getitem__(self, *args, **kwargs): # real signature unknown
        """ Return self[key]. """
        pass

    def __init__(self): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __setitem__(self, *args, **kwargs): # real signature unknown
        """ Set self[key] to value. """
        pass


