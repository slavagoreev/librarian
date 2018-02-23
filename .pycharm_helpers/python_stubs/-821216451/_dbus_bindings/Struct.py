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


from .tuple import tuple

class Struct(tuple):
    """
    An structure containing items of possibly distinct types.
    
    Constructor::
    
        dbus.Struct(iterable, signature=None, variant_level=0) -> Struct
    
    D-Bus structs may not be empty, so the iterable argument is required and
    may not be an empty iterable.
    
    ``signature`` is either None, or a string representing the contents of the
    struct as one or more complete type signatures. The overall signature of
    the struct will be the given signature enclosed in parentheses, ``()``.
    
    If the signature is None (default) it will be guessed
    from the types of the items during construction.
    
    ``variant_level`` must be non-negative; the default is 0.
    
    :IVariables:
      `variant_level` : int
        Indicates how many nested Variant containers this object
        is contained in: if a message's wire format has a variant containing a
        variant containing a struct, this is represented in Python by a
        Struct with variant_level==2.
    """
    def __delattr__(self, *args, **kwargs): # real signature unknown
        """ Implement delattr(self, name). """
        pass

    def __getattribute__(self, *args, **kwargs): # real signature unknown
        """ Return getattr(self, name). """
        pass

    def __init__(self, iterable, signature=None, variant_level=0): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    def __setattr__(self, *args, **kwargs): # real signature unknown
        """ Implement setattr(self, name, value). """
        pass


