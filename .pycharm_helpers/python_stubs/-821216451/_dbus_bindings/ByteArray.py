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


from ._BytesBase import _BytesBase

class ByteArray(_BytesBase):
    """
    ByteArray is a subtype of str which can be used when you want an
    efficient immutable representation of a D-Bus byte array (signature 'ay').
    
    By default, when byte arrays are converted from D-Bus to Python, they
    come out as a `dbus.Array` of `dbus.Byte`. This is just for symmetry with
    the other D-Bus types - in practice, what you usually want is the byte
    array represented as a string, using this class. To get this, pass the
    ``byte_arrays=True`` keyword argument to any of these methods:
    
    * any D-Bus method proxy, or ``connect_to_signal``, on the objects returned
      by `Bus.get_object`
    * any D-Bus method on a `dbus.Interface`
    * `dbus.Interface.connect_to_signal`
    * `Bus.add_signal_receiver`
    
    Import via::
    
       from dbus import ByteArray
    
    Constructor::
    
       ByteArray(str)
    """
    def __init__(self, p_str): # real signature unknown; restored from __doc__
        pass


