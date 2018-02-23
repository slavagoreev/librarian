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


from ._StrBase import _StrBase

class ObjectPath(_StrBase):
    """
    A D-Bus object path, such as '/com/example/MyApp/Documents/abc'.
    
    ObjectPath is a subtype of str, and object-paths behave like strings.
    
    Constructor::
    
        dbus.ObjectPath(path: str, variant_level: int) -> ObjectPath
    
    path must be an ASCII string following the syntax of object paths.
    variant_level must be non-negative; the default is 0.
    
    :IVariables:
      `variant_level` : int
        Indicates how many nested Variant containers this object
        is contained in: if a message's wire format has a variant containing a
        variant containing an object path, this is represented in Python by an
        ObjectPath with variant_level==2.
    """
    def __init__(self, path, variant_level): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass


