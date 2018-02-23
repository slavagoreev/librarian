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

class Message(object):
    """ A message to be sent or received over a D-Bus Connection. """
    def append(self, *args, **kwargs): # real signature unknown
        """
        set_args(*args[, **kwargs])
        
        Set the message's arguments from the positional parameter, according to
        the signature given by the ``signature`` keyword parameter.
        
        The following type conversions are supported:
        
        =============================== ===========================
        D-Bus (in signature)            Python
        =============================== ===========================
        boolean (b)                     any object (via bool())
        byte (y)                        string of length 1
                                        any integer
        any integer type                any integer
        double (d)                      any float
        object path                     anything with a __dbus_object_path__ attribute
        string, signature, object path  str (must be UTF-8) or unicode
        dict (a{...})                   any mapping
        array (a...)                    any iterable over appropriate objects
        struct ((...))                  any iterable over appropriate objects
        variant                         any object above (guess type as below)
        =============================== ===========================
        
        Here 'any integer' means anything on which int() or long()
        (as appropriate) will work, except for basestring subclasses.
        'Any float' means anything on which float() will work, except
        for basestring subclasses.
        
        If there is no signature, guess from the arguments using
        the static method `Message.guess_signature`.
        """
        pass

    def copy(self): # real signature unknown; restored from __doc__
        """
        message.copy() -> Message (or subclass)
        Deep-copy the message, resetting the serial number to zero.
        """
        return Message

    def get_args_list(self, **kwargs): # real signature unknown; restored from __doc__
        """
        get_args_list(**kwargs) -> list
        
        Return the message's arguments. Keyword arguments control the translation
        of D-Bus types to Python:
        
        :Keywords:
           `byte_arrays` : bool
               If true, convert arrays of byte (signature 'ay') into dbus.ByteArray,
               a str subclass. In practice, this is usually what you want, but
               it's off by default for consistency.
        
               If false (default), convert them into a dbus.Array of Bytes.
        
        Most of the type mappings should be fairly obvious:
        
        ===============  ===================================================
        D-Bus            Python
        ===============  ===================================================
        byte (y)         dbus.Byte (int subclass)
        bool (b)         dbus.Boolean (int subclass)
        Signature (g)    dbus.Signature (str subclass)
        intNN, uintNN    dbus.IntNN, dbus.UIntNN (int or long subclasses)
        double (d)       dbus.Double
        string (s)       dbus.String (unicode subclass)
                         (or dbus.UTF8String, str subclass, if utf8_strings set)
        Object path (o)  dbus.ObjectPath (str subclass)
        dict (a{...})    dbus.Dictionary
        array (a...)     dbus.Array (list subclass) containing appropriate types
        byte array (ay)  dbus.ByteArray (str subclass) if byte_arrays set; or
                         list of Byte
        struct ((...))   dbus.Struct (tuple subclass) of appropriate types
        variant (v)      contained type, but with variant_level > 0
        ===============  ===================================================
        """
        return []

    def get_auto_start(self): # real signature unknown; restored from __doc__
        """
        message.get_auto_start() -> bool
        Return true if this message will cause an owner for the destination name
        to be auto-started.
        """
        return False

    def get_destination(self): # real signature unknown; restored from __doc__
        """
        get_destination() -> str or None
        
        Return the message's destination bus name, or None if none.
        """
        return ""

    def get_error_name(self): # real signature unknown; restored from __doc__
        """ get_error_name() -> str or None """
        return ""

    def get_interface(self): # real signature unknown; restored from __doc__
        """ get_interface() -> str or None """
        return ""

    def get_member(self): # real signature unknown; restored from __doc__
        """ get_member() -> str or None """
        return ""

    def get_no_reply(self): # real signature unknown; restored from __doc__
        """
        message.get_no_reply() -> bool
        Return true if this message need not be replied to.
        """
        return False

    def get_path(self): # real signature unknown; restored from __doc__
        """
        get_path() -> ObjectPath or None
        
        Return the message's destination object path (if it's a method call) or
        source object path (if it's a method reply or a signal) or None (if it
        has no path).
        """
        return ObjectPath

    def get_path_decomposed(self): # real signature unknown; restored from __doc__
        """
        get_path_decomposed() -> list of str, or None
        
        Return a list of path components (e.g. /foo/bar -> ['foo','bar'], / -> [])
        or None if the message has no associated path.
        """
        return []

    def get_reply_serial(self): # real signature unknown; restored from __doc__
        """
        message.get_reply_serial() -> long
        Returns the serial that the message is a reply to or 0 if none.
        """
        return 0

    def get_sender(self): # real signature unknown; restored from __doc__
        """
        get_sender() -> str or None
        
        Return the message's sender unique name, or None if none.
        """
        return ""

    def get_serial(self): # real signature unknown; restored from __doc__
        """
        message.get_serial() -> long
        Returns the serial of a message or 0 if none has been specified.
        
        The message's serial number is provided by the application sending the
        message and is used to identify replies to this message. All messages
        received on a connection will have a serial, but messages you haven't
        sent yet may return 0.
        """
        return 0

    def get_signature(self): # real signature unknown; restored from __doc__
        """ get_signature() -> Signature or None """
        return Signature

    def get_type(self): # real signature unknown; restored from __doc__
        """
        message.get_type() -> int
        
        Returns the type of the message.
        """
        return 0

    def guess_signature(self, *args): # real signature unknown; restored from __doc__
        """
        guess_signature(*args) -> Signature [static method]
        
        Guess a D-Bus signature which should be used to encode the given
        Python objects.
        
        The signature is constructed as follows:
        
        +-------------------------------+---------------------------+
        |Python                         |D-Bus                      |
        +===============================+===========================+
        |D-Bus type, variant_level > 0  |variant (v)                |
        +-------------------------------+---------------------------+
        |D-Bus type, variant_level == 0 |the corresponding type     |
        +-------------------------------+---------------------------+
        |anything with a                |object path                |
        |__dbus_object_path__ attribute |                           |
        +-------------------------------+---------------------------+
        |bool                           |boolean (y)                |
        +-------------------------------+---------------------------+
        |any other int subclass         |int32 (i)                  |
        +-------------------------------+---------------------------+
        |any other long subclass        |int64 (x)                  |
        +-------------------------------+---------------------------+
        |any other float subclass       |double (d)                 |
        +-------------------------------+---------------------------+
        |any other str subclass         |string (s)                 |
        +-------------------------------+---------------------------+
        |any other unicode subclass     |string (s)                 |
        +-------------------------------+---------------------------+
        |any other tuple subclass       |struct ((...))             |
        +-------------------------------+---------------------------+
        |any other list subclass        |array (a...), guess        |
        |                               |contents' type according to|
        |                               |type of first item         |
        +-------------------------------+---------------------------+
        |any other dict subclass        |dict (a{...}), guess key,  |
        |                               |value type according to    |
        |                               |types for an arbitrary item|
        +-------------------------------+---------------------------+
        |anything else                  |raise TypeError            |
        +-------------------------------+---------------------------+
        """
        return Signature

    def has_destination(self, bus_name): # real signature unknown; restored from __doc__
        """ has_destination(bus_name: str) -> bool """
        return False

    def has_interface(self, interface_or_None): # real signature unknown; restored from __doc__
        """ has_interface(interface: str or None) -> bool """
        return False

    def has_member(self, name_or_None): # real signature unknown; restored from __doc__
        """ has_member(name: str or None) -> bool """
        return False

    def has_path(self, name_or_None): # real signature unknown; restored from __doc__
        """ has_path(name: str or None) -> bool """
        return False

    def has_sender(self, unique_name): # real signature unknown; restored from __doc__
        """ has_sender(unique_name: str) -> bool """
        return False

    def has_signature(self, signature): # real signature unknown; restored from __doc__
        """ has_signature(signature: str) -> bool """
        return False

    def is_error(self, error): # real signature unknown; restored from __doc__
        """ is_error(error: str) -> bool """
        return False

    def is_method_call(self, interface, member): # real signature unknown; restored from __doc__
        """ is_method_call(interface: str, member: str) -> bool """
        return False

    def is_signal(self, interface, member): # real signature unknown; restored from __doc__
        """ is_signal(interface: str, member: str) -> bool """
        return False

    def set_auto_start(self, bool): # real signature unknown; restored from __doc__
        """
        message.set_auto_start(bool) -> None
        Set whether this message will cause an owner for the destination name
        to be auto-started.
        """
        pass

    def set_destination(self, bus_name_or_None): # real signature unknown; restored from __doc__
        """ set_destination(bus_name: str or None) """
        pass

    def set_error_name(self, name_or_None): # real signature unknown; restored from __doc__
        """ set_error_name(name: str or None) """
        pass

    def set_interface(self, name_or_None): # real signature unknown; restored from __doc__
        """ set_interface(name: str or None) """
        pass

    def set_member(self, unique_name_or_None): # real signature unknown; restored from __doc__
        """ set_member(unique_name: str or None) """
        pass

    def set_no_reply(self, bool): # real signature unknown; restored from __doc__
        """
        message.set_no_reply(bool) -> None
        Set whether no reply to this message is required.
        """
        pass

    def set_path(self, name_or_None): # real signature unknown; restored from __doc__
        """ set_path(name: str or None) """
        pass

    def set_reply_serial(self, bool): # real signature unknown; restored from __doc__
        """
        message.set_reply_serial(bool) -> None
        Set the serial that this message is a reply to.
        """
        pass

    def set_sender(self, unique_name_or_None): # real signature unknown; restored from __doc__
        """ set_sender(unique_name: str or None) """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass


