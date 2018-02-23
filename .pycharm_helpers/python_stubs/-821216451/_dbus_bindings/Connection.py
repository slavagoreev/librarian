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

class Connection(object):
    """
    A D-Bus connection.
    
    ::
    
       Connection(address, mainloop=None) -> Connection
    """
    def add_message_filter(self, callable): # real signature unknown; restored from __doc__
        """
        add_message_filter(callable)
        
        Add the given message filter to the internal list.
        
        Filters are handlers that are run on all incoming messages, prior to the
        objects registered to handle object paths.
        
        Filters are run in the order that they were added. The same handler can
        be added as a filter more than once, in which case it will be run more
        than once. Filters added during a filter callback won't be run on the
        message being processed.
        """
        pass

    def close(self): # real signature unknown; restored from __doc__
        """
        close()
        
        Close the connection.
        """
        pass

    def flush(self): # real signature unknown; restored from __doc__
        """
        flush()
        
        Block until the outgoing message queue is empty.
        """
        pass

    def get_is_authenticated(self): # real signature unknown; restored from __doc__
        """
        get_is_authenticated() -> bool
        
        Return true if this Connection was ever authenticated.
        """
        return False

    def get_is_connected(self): # real signature unknown; restored from __doc__
        """
        get_is_connected() -> bool
        
        Return true if this Connection is connected.
        """
        return False

    def get_peer_unix_process_id(self): # real signature unknown; restored from __doc__
        """
        get_peer_unix_process_id() -> long or None
        
        Get the UNIX process ID at the other end of the connection, if it has been
        authenticated. Return None if this is a non-UNIX platform or the
        connection has not been authenticated.
        """
        return 0

    def get_peer_unix_user(self): # real signature unknown; restored from __doc__
        """
        get_peer_unix_user() -> long or None
        
        Get the UNIX user ID at the other end of the connection, if it has been
        authenticated. Return None if this is a non-UNIX platform or the
        connection has not been authenticated.
        """
        return 0

    def get_unique_name(self): # real signature unknown; restored from __doc__
        """
        get_unique_name() -> str
        
        Return this application's unique name on this bus.
        
        :Raises DBusException: if the connection has no unique name yet
           (for Bus objects this can't happen, for peer-to-peer connections
           this means you haven't called `set_unique_name`)
        """
        return ""

    def get_unix_fd(self): # real signature unknown; restored from __doc__
        """
        get_unix_fd() -> int or None
        
        Get the connection's UNIX file descriptor, if any.
        
        This can be used for SELinux access control checks with ``getpeercon()``
        for example. **Do not** read or write to the file descriptor, or try to
        ``select()`` on it.
        """
        return 0

    def list_exported_child_objects(self, path): # real signature unknown; restored from __doc__
        """
        list_exported_child_objects(path: str) -> list of str
        
        Return a list of the names of objects exported on this Connection as
        direct children of the given object path.
        
        Each name returned may be converted to a valid object path using
        ``dbus.ObjectPath('%s%s%s' % (path, (path != '/' and '/' or ''), name))``.
        For the purposes of this function, every parent or ancestor of an exported
        object is considered to be an exported object, even if it's only an object
        synthesized by the library to support introspection.
        """
        return []

    def remove_message_filter(self, callable): # real signature unknown; restored from __doc__
        """
        remove_message_filter(callable)
        
        Remove the given message filter (see `add_message_filter` for details).
        
        :Raises LookupError:
           The given callable is not among the registered filters
        """
        pass

    def send_message(self, msg): # real signature unknown; restored from __doc__
        """
        send_message(msg) -> long
        
        Queue the given message for sending, and return the message serial number.
        
        :Parameters:
           `msg` : dbus.lowlevel.Message
               The message to be sent.
        """
        return 0

    def send_message_with_reply(self, msg, reply_handler, timeout_s=-1, require_main_loop=False): # real signature unknown; restored from __doc__
        """
        send_message_with_reply(msg, reply_handler, timeout_s=-1, require_main_loop=False) -> dbus.lowlevel.PendingCall
        
        Queue the message for sending; expect a reply via the returned PendingCall,
        which can also be used to cancel the pending call.
        
        :Parameters:
           `msg` : dbus.lowlevel.Message
               The message to be sent
           `reply_handler` : callable
               Asynchronous reply handler: will be called with one positional
               parameter, a Message instance representing the reply.
           `timeout_s` : float
               If the reply takes more than this many seconds, a timeout error
               will be created locally and raised instead. If this timeout is
               negative (default), a sane default (supplied by libdbus) is used.
           `require_main_loop` : bool
               If True, raise RuntimeError if this Connection does not have a main
               loop configured. If False (default) and there is no main loop, you are
               responsible for calling block() on the PendingCall.
        """
        pass

    def send_message_with_reply_and_block(self, msg, timeout_s=-1): # real signature unknown; restored from __doc__
        """
        send_message_with_reply_and_block(msg, timeout_s=-1) -> dbus.lowlevel.Message
        
        Send the message and block while waiting for a reply.
        
        This does not re-enter the main loop, so it can lead to a deadlock, if
        the called method tries to make a synchronous call to a method in this
        application. As such, it's probably a bad idea.
        
        :Parameters:
           `msg` : dbus.lowlevel.Message
               The message to be sent
           `timeout_s` : float
               If the reply takes more than this many seconds, a timeout error
               will be created locally and raised instead. If this timeout is
               negative (default), a sane default (supplied by libdbus) is used.
        :Returns:
           A `dbus.lowlevel.Message` instance (probably a `dbus.lowlevel.MethodReturnMessage`) on success
        :Raises dbus.DBusException:
           On error (including if the reply arrives but is an
           error message)
        """
        pass

    def set_allow_anonymous(self, bool): # real signature unknown; restored from __doc__
        """
        set_allow_anonymous(bool)
        
        Allows anonymous clients. Call this on the server side of a connection in a on_connection_added callback
        """
        pass

    def set_exit_on_disconnect(self, bool): # real signature unknown; restored from __doc__
        """
        set_exit_on_disconnect(bool)
        
        Set whether the C function ``_exit`` will be called when this Connection
        becomes disconnected. This will cause the program to exit without calling
        any cleanup code or exit handlers.
        
        The default is for this feature to be disabled for Connections and enabled
        for Buses.
        """
        pass

    def set_unique_name(self, p_str): # real signature unknown; restored from __doc__
        """
        set_unique_name(str)
        
        Set this application's unique name on this bus. Raise ValueError if it has
        already been set.
        """
        pass

    @classmethod
    def _new_for_bus(cls, address_or_int=None): # real signature unknown; restored from __doc__
        """
        Connection._new_for_bus([address: str or int]) -> Connection
        
        If the address is an int it must be one of the constants BUS_SESSION,
        BUS_SYSTEM, BUS_STARTER; if a string, it must be a D-Bus address.
        The default is BUS_SESSION.
        """
        return Connection

    def _register_object_path(self, *args, **kwargs): # real signature unknown
        """
        register_object_path(path, on_message, on_unregister=None, fallback=False)
        
        Register a callback to be called when messages arrive at the given
        object-path. Used to export objects' methods on the bus in a low-level
        way. For the high-level interface to this functionality (usually
        recommended) see the `dbus.service.Object` base class.
        
        :Parameters:
           `path` : str
               Object path to be acted on
           `on_message` : callable
               Called when a message arrives at the given object-path, with
               two positional parameters: the first is this Connection,
               the second is the incoming `dbus.lowlevel.Message`.
           `on_unregister` : callable or None
               If not None, called when the callback is unregistered.
           `fallback` : bool
               If True (the default is False), when a message arrives for a
               'subdirectory' of the given path and there is no more specific
               handler, use this handler. Normally this handler is only run if
               the paths match exactly.
        """
        pass

    def _require_main_loop(self): # real signature unknown; restored from __doc__
        """
        _require_main_loop()
        
        Raise an exception if this Connection is not bound to any main loop -
        in this state, asynchronous calls, receiving signals and exporting objects
        will not work.
        
        `dbus.mainloop.NULL_MAIN_LOOP` is treated like a valid main loop - if you're
        using that, you presumably know what you're doing.
        """
        pass

    def _unregister_object_path(self, *args, **kwargs): # real signature unknown
        """
        unregister_object_path(path)
        
        Remove a previously registered handler for the given object path.
        
        :Parameters:
           `path` : str
               The object path whose handler is to be removed
        :Raises KeyError: if there is no handler registered for exactly that
           object path.
        """
        pass

    def __init__(self, address, mainloop=None): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass


