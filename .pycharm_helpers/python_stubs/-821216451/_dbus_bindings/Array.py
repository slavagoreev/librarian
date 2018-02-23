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


from .list import list

class Array(list):
    """
    An array of similar items, implemented as a subtype of list.
    
    As currently implemented, an Array behaves just like a list, but
    with the addition of a ``signature`` property set by the constructor;
    conversion of its items to D-Bus types is only done when it's sent in
    a Message. This might change in future so validation is done earlier.
    
    Constructor::
    
        dbus.Array([iterable][, signature][, variant_level])
    
    ``variant_level`` must be non-negative; the default is 0.
    
    ``signature`` is the D-Bus signature string for a single element of the
    array, or None. If not None it must represent a single complete type, the
    type of a single array item; the signature of the whole Array may be
    obtained by prepending ``a`` to the given signature.
    
    If None (the default), when the Array is sent over
    D-Bus, the item signature will be guessed from the first element.
    
    :IVariables:
      `variant_level` : int
        Indicates how many nested Variant containers this object
        is contained in: if a message's wire format has a variant containing a
        variant containing an array, this is represented in Python by an
        Array with variant_level==2.
    """
    def __init__(self, iterable=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    signature = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The D-Bus signature of each element of this Array (a Signature instance)"""

    variant_level = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The number of nested variants wrapping the real data. 0 if not in a variant."""



