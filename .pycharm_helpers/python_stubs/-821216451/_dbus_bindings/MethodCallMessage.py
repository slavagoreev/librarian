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


class MethodCallMessage(__dbus_lowlevel.Message):
    """
    A method-call message.
    
    Constructor::
    
        dbus.lowlevel.MethodCallMessage(destination: str or None, path: str,
                                        interface: str or None, method: str)
    
    ``destination`` is the destination bus name, or None to send the
    message directly to the peer (usually the bus daemon).
    
    ``path`` is the object-path of the object whose method is to be called.
    
    ``interface`` is the interface qualifying the method name, or None to omit
    the interface from the message header.
    
    ``method`` is the method name (member name).
    """
    def __init__(self, destination_or_None, path, interface_or_None, method): # real signature unknown; restored from __doc__
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass


