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


from ._LongBase import _LongBase

class UInt32(_LongBase):
    """
    An unsigned 32-bit integer between 0 and 0xFFFF FFFF, represented as a
    subtype of `long`.
    
    Note that this may be changed in future to be a subtype of `int` on
    64-bit platforms; applications should not rely on either behaviour.
    
    Constructor::
    
        dbus.UInt32(value: long[, variant_level: int]) -> UInt32
    
    ``value`` must be within the allowed range, or `OverflowError` will be
    raised.
    
    ``variant_level`` must be non-negative; the default is 0.
    
    :IVariables:
      `variant_level` : int
        Indicates how many nested Variant containers this object
        is contained in: if a message's wire format has a variant containing a
        variant containing a uint32, this is represented in Python by a
        UInt32 with variant_level==2.
    """
    def __init__(self, value, variant_level=None): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass


