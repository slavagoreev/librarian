# encoding: utf-8
# module _dbus_bindings
# from /usr/lib/python3/dist-packages/_dbus_bindings.cpython-35m-x86_64-linux-gnu.so
# by generator 1.145
"""
Low-level Python bindings for libdbus. Don't use this module directly -
the public API is provided by the `dbus`, `dbus.service`, `dbus.mainloop`
and `dbus.mainloop.glib` modules, with a lower-level API provided by the
`dbus.lowlevel` module.
"""

# imports
import dbus.lowlevel as __dbus_lowlevel


from .object import object

class UnixFd(object):
    """
    An Unix Fd.
    
    Constructor::
    
        dbus.UnixFd(value: int or file object[, variant_level: int]) -> UnixFd
    
    ``value`` must be the integer value of a file descriptor, or an object that
    implements the fileno() method. Otherwise, `ValueError` will be
    raised.
    
    UnixFd keeps a dup() (duplicate) of the supplied file descriptor. The
    caller remains responsible for closing the original fd.
    
    ``variant_level`` must be non-negative; the default is 0.
    
    :IVariables:
      `variant_level` : int
        Indicates how many nested Variant containers this object
        is contained in: if a message's wire format has a variant containing a
        variant containing an Unix Fd, this is represented in Python by an
        Unix Fd with variant_level==2.
    """
    def take(self): # real signature unknown; restored from __doc__
        """
        take() -> int
        
        This method returns the file descriptor owned by UnixFd object.
        Note that, once this method is called, closing the file descriptor is
        the caller's responsibility.
        
        This method may be called at most once; UnixFd 'forgets' the file
        descriptor after it is taken.
        
        :Raises ValueError: if this method has already been called
        """
        return 0

    def __init__(self, value_or_file_object, variant_level=None): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass


