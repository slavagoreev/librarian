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


class ErrorMessage(__dbus_lowlevel.Message):
    """
    An error message.
    
    Constructor::
    
       dbus.lowlevel.ErrorMessage(reply_to: Message, error_name: str,
                                  error_message: str or None)
    """
    def __init__(self, reply_to, error_name, error_message_or_None): # real signature unknown; restored from __doc__
        pass


