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


from .dict import dict

class Dictionary(dict):
    """
    An mapping whose keys are similar and whose values are similar,
    implemented as a subtype of dict.
    
    As currently implemented, a Dictionary behaves just like a dict, but
    with the addition of a ``signature`` property set by the constructor;
    conversion of its items to D-Bus types is only done when it's sent in
    a Message. This may change in future so validation is done earlier.
    
    Constructor::
    
        Dictionary(mapping_or_iterable=(), signature=None, variant_level=0)
    
    ``variant_level`` must be non-negative; the default is 0.
    
    ``signature`` is either a string or None. If a string, it must consist
    of exactly two complete type signatures, representing the 'key' type
    (which must be a primitive type, i.e. one of "bdginoqstuxy")
    and the 'value' type. The signature of the whole Dictionary will be
    ``a{xx}`` where ``xx`` is replaced by the given signature.
    
    If it is None (the default), when the Dictionary is sent over
    D-Bus, the key and value signatures will be guessed from an arbitrary
    element of the Dictionary.
    
    :IVariables:
      `variant_level` : int
        Indicates how many nested Variant containers this object
        is contained in: if a message's wire format has a variant containing a
        variant containing an array of DICT_ENTRY, this is represented in
        Python by a Dictionary with variant_level==2.
    """
    def __init__(self, mapping_or_iterable=(), signature=None, variant_level=0): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    signature = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The D-Bus signature of each key in this Dictionary, followed by that of each value in this Dictionary, as a Signature instance."""

    variant_level = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The number of nested variants wrapping the real data. 0 if not in a variant."""



