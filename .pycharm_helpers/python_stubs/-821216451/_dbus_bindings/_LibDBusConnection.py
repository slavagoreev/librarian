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

class _LibDBusConnection(object):
    """
    A reference to a ``DBusConnection`` from ``libdbus``, which might not
    have been attached to a `dbus.connection.Connection` yet.
    
    Cannot be instantiated from Python. The only use of this object is to
    pass it to the ``dbus.connection.Connection`` constructor instead of an
    address.
    """
    def __init__(self, *args, **kwargs): # real signature unknown
        pass


