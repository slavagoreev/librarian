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


from .str import str

class String(str):
    """
    A string represented using Unicode - a subtype of `unicode`.
    
    All strings on D-Bus are required to be valid Unicode; in the "wire
    protocol" they're transported as UTF-8.
    
    By default, when strings are converted from D-Bus to Python, they
    come out as this class. If you prefer to get UTF-8 strings (as instances
    of a subtype of `str`) or you want to avoid the conversion overhead of
    going from UTF-8 to Python's internal Unicode representation, see the
    documentation for `dbus.UTF8String`.
    
    Constructor::
    
        String(value: str or unicode[, variant_level: int]) -> String
    
    variant_level must be non-negative; the default is 0.
    
    :IVariables:
      `variant_level` : int
        Indicates how many nested Variant containers this object
        is contained in: if a message's wire format has a variant containing a
        variant containing a string, this is represented in Python by a
        String or UTF8String with variant_level==2.
    """
    def __delattr__(self, *args, **kwargs): # real signature unknown
        """ Implement delattr(self, name). """
        pass

    def __getattribute__(self, *args, **kwargs): # real signature unknown
        """ Return getattr(self, name). """
        pass

    def __init__(self, value_or_unicode, variant_level=None): # real signature unknown; restored from __doc__
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

    variant_level = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The number of nested variants wrapping the real data. 0 if not in a variant"""



