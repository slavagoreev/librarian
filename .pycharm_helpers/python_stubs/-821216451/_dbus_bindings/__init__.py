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


# Variables with simple values

BUS_DAEMON_IFACE = 'org.freedesktop.DBus'
BUS_DAEMON_NAME = 'org.freedesktop.DBus'
BUS_DAEMON_PATH = '/org/freedesktop/DBus'

BUS_SESSION = 0
BUS_STARTER = 2
BUS_SYSTEM = 1

DBUS_INTROSPECT_1_0_XML_DOCTYPE_DECL_NODE = '<!DOCTYPE node PUBLIC "-//freedesktop//DTD D-BUS Object Introspection 1.0//EN"\n"http://www.freedesktop.org/standards/dbus/1.0/introspect.dtd">\n'

DBUS_INTROSPECT_1_0_XML_PUBLIC_IDENTIFIER = '-//freedesktop//DTD D-BUS Object Introspection 1.0//EN'

DBUS_INTROSPECT_1_0_XML_SYSTEM_IDENTIFIER = 'http://www.freedesktop.org/standards/dbus/1.0/introspect.dtd'

DBUS_START_REPLY_ALREADY_RUNNING = 2

DBUS_START_REPLY_SUCCESS = 1

DICT_ENTRY_BEGIN = 123
DICT_ENTRY_END = 125

HANDLER_RESULT_HANDLED = 0

HANDLER_RESULT_NEED_MEMORY = 2

HANDLER_RESULT_NOT_YET_HANDLED = 1

INTROSPECTABLE_IFACE = 'org.freedesktop.DBus.Introspectable'

LOCAL_IFACE = 'org.freedesktop.DBus.Local'
LOCAL_PATH = '/org/freedesktop/DBus/Local'

MESSAGE_TYPE_ERROR = 3
MESSAGE_TYPE_INVALID = 0

MESSAGE_TYPE_METHOD_CALL = 1
MESSAGE_TYPE_METHOD_RETURN = 2

MESSAGE_TYPE_SIGNAL = 4

NAME_FLAG_ALLOW_REPLACEMENT = 1

NAME_FLAG_DO_NOT_QUEUE = 4

NAME_FLAG_REPLACE_EXISTING = 2

PEER_IFACE = 'org.freedesktop.DBus.Peer'

PROPERTIES_IFACE = 'org.freedesktop.DBus.Properties'

RELEASE_NAME_REPLY_NON_EXISTENT = 2

RELEASE_NAME_REPLY_NOT_OWNER = 3

RELEASE_NAME_REPLY_RELEASED = 1

REQUEST_NAME_REPLY_ALREADY_OWNER = 4

REQUEST_NAME_REPLY_EXISTS = 3

REQUEST_NAME_REPLY_IN_QUEUE = 2

REQUEST_NAME_REPLY_PRIMARY_OWNER = 1

STRUCT_BEGIN = 40
STRUCT_END = 41

TYPE_ARRAY = 97
TYPE_BOOLEAN = 98
TYPE_BYTE = 121

TYPE_DICT_ENTRY = 101

TYPE_DOUBLE = 100
TYPE_INT16 = 110
TYPE_INT32 = 105
TYPE_INT64 = 120
TYPE_INVALID = 0

TYPE_OBJECT_PATH = 111

TYPE_SIGNATURE = 103
TYPE_STRING = 115
TYPE_STRUCT = 114
TYPE_UINT16 = 113
TYPE_UINT32 = 117
TYPE_UINT64 = 116

TYPE_UNIX_FD = 104

TYPE_VARIANT = 118

WATCH_ERROR = 4
WATCH_HANGUP = 8
WATCH_READABLE = 1
WATCH_WRITABLE = 2

_python_version = 50659824

__docformat__ = 'restructuredtext'

__version__ = '1.2.0'

# functions

def get_default_main_loop(): # real signature unknown; restored from __doc__
    """
    get_default_main_loop() -> object
    
    Return the global default dbus-python main loop wrapper, which is used
    when no main loop wrapper is passed to the Connection constructor.
    
    If None, there is no default and you should always pass the mainloop
    parameter to the constructor - if you don't, then asynchronous calls,
    connecting to signals and exporting objects will raise an exception.
    There is no default until set_default_main_loop is called.
    """
    return object()

def set_default_main_loop(p_object): # real signature unknown; restored from __doc__
    """
    set_default_main_loop(object)
    
    Change the global default dbus-python main loop wrapper, which is used
    when no main loop wrapper is passed to the Connection constructor.
    
    If None, return to the initial situation: there is no default, and you
    must always pass the mainloop parameter to the constructor.
    
    Two types of main loop wrapper are planned in dbus-python.
    Native main-loop wrappers are instances of `dbus.mainloop.NativeMainLoop`
    supplied by extension modules like `dbus.mainloop.glib`: they have no
    Python API, but connect themselves to ``libdbus`` using native code.
    Python main-loop wrappers are not yet implemented. They will be objects
    supporting the interface defined by `dbus.mainloop.MainLoop`, with an
    API entirely based on Python methods.
    """
    pass

def validate_bus_name(name, allow_unique=True, allow_well_known=True): # real signature unknown; restored from __doc__
    """
    validate_bus_name(name, allow_unique=True, allow_well_known=True)
    
    Raise ValueError if the argument is not a valid bus name.
    
    By default both unique and well-known names are accepted.
    
    :Parameters:
       `name` : str
           The name to be validated
       `allow_unique` : bool
           If False, unique names of the form :1.123 will be rejected
       `allow_well_known` : bool
           If False, well-known names of the form com.example.Foo
           will be rejected
    :Since: 0.80
    """
    pass

def validate_error_name(name): # real signature unknown; restored from __doc__
    """
    validate_error_name(name)
    
    Raise ValueError if the given string is not a valid error name.
    
    :Since: 0.80
    """
    pass

def validate_interface_name(name): # real signature unknown; restored from __doc__
    """
    validate_interface_name(name)
    
    Raise ValueError if the given string is not a valid interface name.
    
    :Since: 0.80
    """
    pass

def validate_member_name(name): # real signature unknown; restored from __doc__
    """
    validate_member_name(name)
    
    Raise ValueError if the argument is not a valid member (signal or method) name.
    
    :Since: 0.80
    """
    pass

def validate_object_path(name): # real signature unknown; restored from __doc__
    """
    validate_object_path(name)
    
    Raise ValueError if the given string is not a valid object path.
    
    :Since: 0.80
    """
    pass

# classes

from .Array import Array
from ._LongBase import _LongBase
from .Boolean import Boolean
from .Byte import Byte
from ._BytesBase import _BytesBase
from .ByteArray import ByteArray
from .Connection import Connection
from .Dictionary import Dictionary
from ._FloatBase import _FloatBase
from .Double import Double
from .Message import Message
from .ErrorMessage import ErrorMessage
from .Int16 import Int16
from .Int32 import Int32
from .Int64 import Int64
from .MethodCallMessage import MethodCallMessage
from .MethodReturnMessage import MethodReturnMessage
from .NativeMainLoop import NativeMainLoop
from ._StrBase import _StrBase
from .ObjectPath import ObjectPath
from .PendingCall import PendingCall
from .SignalMessage import SignalMessage
from .Signature import Signature
from .String import String
from .Struct import Struct
from .UInt16 import UInt16
from .UInt32 import UInt32
from .UInt64 import UInt64
from .UnixFd import UnixFd
from ._LibDBusConnection import _LibDBusConnection
from ._Server import _Server
from ._SignatureIter import _SignatureIter
# variables with complex values

NULL_MAIN_LOOP = None # (!) real value is ''

_C_API = None # (!) real value is ''

__loader__ = None # (!) real value is ''

__spec__ = None # (!) real value is ''

