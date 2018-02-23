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


class MethodReturnMessage(__dbus_lowlevel.Message):
    """
    A method-return message.
    
    Constructor::
    
        dbus.lowlevel.MethodReturnMessage(method_call: MethodCallMessage)
    """
    def __init__(self, method_call): # real signature unknown; restored from __doc__
        pass


