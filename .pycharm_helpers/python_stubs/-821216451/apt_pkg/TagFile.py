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

class TagFile(object):
    """
    TagFile(file, [bytes: bool = False])
    
    TagFile() objects provide access to debian control files, which consist
    of multiple RFC822-style sections.
    
    To provide access to those sections, TagFile objects provide an iterator
    which yields TagSection objects for each section.
    
    TagFile objects also provide another API which uses a shared TagSection
    object in the 'section' member. The functions step() and jump() can be
    used to navigate within the file; offset() returns the current
    position.
    
    It is important to not mix the use of both APIs, because this can have
    unwanted effects.
    
    The parameter 'file' refers to an object providing a fileno() method or
    a file descriptor (an integer).
    
    By default, text read from files is treated as strings (binary data in
    Python 2, Unicode strings in Python 3). Use bytes=True to cause all
    header values read from this TagFile to be bytes even in Python 3.
    Header names are always treated as Unicode.
    """
    def close(self): # real signature unknown; restored from __doc__
        """
        close()
        
        Close the file.
        """
        pass

    def jump(self, offset): # real signature unknown; restored from __doc__
        """
        jump(offset: int) -> bool
        
        Jump to the given offset; return True on success. Note that jumping to
        an offset is not very reliable, and the 'section' attribute may point
        to an unexpected section.
        """
        return False

    def offset(self): # real signature unknown; restored from __doc__
        """
        offset() -> int
        
        Return the current offset.
        """
        return 0

    def step(self): # real signature unknown; restored from __doc__
        """
        step() -> bool
        
        Step forward in the file
        """
        return False

    def __enter__(self, *args, **kwargs): # real signature unknown
        """ Context manager entry, return self. """
        pass

    def __exit__(self, *args, **kwargs): # real signature unknown
        """ Context manager exit, calls close. """
        pass

    def __init__(self, file, bytes=False): # real signature unknown; restored from __doc__
        pass

    def __iter__(self, *args, **kwargs): # real signature unknown
        """ Implement iter(self). """
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __next__(self, *args, **kwargs): # real signature unknown
        """ Implement next(self). """
        pass

    section = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The current section, as a TagSection object."""



