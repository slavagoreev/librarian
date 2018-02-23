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

class PendingCall(object):
    """
    Object representing a pending D-Bus call, returned by
    Connection.send_message_with_reply(). Cannot be instantiated directly.
    """
    def block(self): # real signature unknown; restored from __doc__
        """
        block()
        
        Block until this pending call has completed and the associated
        reply handler has been called.
        
        This can lead to a deadlock, if the called method tries to make a
        synchronous call to a method in this application.
        """
        pass

    def cancel(self): # real signature unknown; restored from __doc__
        """
        cancel()
        
        Cancel this pending call. Its reply will be ignored and the associated
        reply handler will never be called.
        """
        pass

    def get_completed(self): # real signature unknown; restored from __doc__
        """
        get_completed() -> bool
        
        Return true if this pending call has completed.
        
        If so, its associated reply handler has been called and it is no
        longer meaningful to cancel it.
        """
        return False

    def __init__(self, *args, **kwargs): # real signature unknown
        pass


