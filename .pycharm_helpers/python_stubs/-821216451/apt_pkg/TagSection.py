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

class TagSection(object):
    """
    TagSection(text: str, [bytes: bool = False])
    
    Provide methods to access RFC822-style header sections, like those
    found in debian/control or Packages files.
    
    TagSection() behave like read-only dictionaries and also provide access
    to the functions provided by the C++ class (e.g. find).
    
    By default, text read from files is treated as strings (binary data in
    Python 2, Unicode strings in Python 3). Use bytes=True to cause all
    header values read from this TagSection to be bytes even in Python 3.
    Header names are always treated as Unicode.
    """
    def bytes(self): # real signature unknown; restored from __doc__
        """
        bytes() -> int
        
        Return the number of bytes this section is large.
        """
        return 0

    def find(self, name, default=None): # real signature unknown; restored from __doc__
        """
        find(name: str[, default = None]) -> str
        
        Find the key given by 'name' and return the value. If the key can
        not be found, return 'default'.
        """
        return ""

    def find_flag(self, name): # real signature unknown; restored from __doc__
        """
        find_flag(name: str) -> int
        
        Return 1 if the key's value is 'yes' or a similar value describing
        a boolean true. If the field does not exist, or does not have such a
        value, return 0.
        """
        return 0

    def find_raw(self, name, default=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        find_raw(name: str[, default = None] -> str
        
        Same as find(), but returns the complete 'key: value' field; instead of
        just the value.
        """
        pass

    def get(self, *args, **kwargs): # real signature unknown
        """
        find(name: str[, default = None]) -> str
        
        Find the key given by 'name' and return the value. If the key can
        not be found, return 'default'.
        """
        pass

    def keys(self): # real signature unknown; restored from __doc__
        """
        keys() -> list
        
        Return a list of all keys.
        """
        return []

    def __contains__(self, *args, **kwargs): # real signature unknown
        """ Return key in self. """
        pass

    def __getitem__(self, *args, **kwargs): # real signature unknown
        """ Return self[key]. """
        pass

    def __init__(self, text, bytes=False): # real signature unknown; restored from __doc__
        pass

    def __len__(self, *args, **kwargs): # real signature unknown
        """ Return len(self). """
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __str__(self, *args, **kwargs): # real signature unknown
        """ Return str(self). """
        pass


