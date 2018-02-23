# encoding: utf-8
# module systemd._daemon
# from /usr/lib/python3/dist-packages/systemd/_daemon.cpython-35m-x86_64-linux-gnu.so
# by generator 1.145
"""
Python interface to the libsystemd-daemon library.

Provides _listen_fds, notify, booted, and is_* functions
which wrap sd_listen_fds, sd_notify, sd_booted, sd_is_* and
useful for socket activation and checking if the system is
running under systemd.
"""
# no imports

# Variables with simple values

LISTEN_FDS_START = 3

__version__ = '231'

# functions

def booted(): # real signature unknown; restored from __doc__
    """
    booted() -> bool
    
    Return True iff this system is running under systemd.
    Wraps sd_booted(3).
    """
    return False

def notify(status, unset_environment=False, pid=0, fds=None): # real signature unknown; restored from __doc__
    """
    notify(status, unset_environment=False, pid=0, fds=None) -> bool
    
    Send a message to the init system about a status change.
    Wraps sd_notify(3).
    """
    return False

def _is_fifo(fd, path): # real signature unknown; restored from __doc__
    """
    _is_fifo(fd, path) -> bool
    
    Returns True iff the descriptor refers to a FIFO or a pipe.
    Wraps sd_is_fifo(3).
    """
    return False

def _is_mq(fd, path): # real signature unknown; restored from __doc__
    """
    _is_mq(fd, path) -> bool
    
    Returns True iff the descriptor refers to a POSIX message queue.
    Wraps sd_is_mq(3).
    """
    return False

def _is_socket(fd, family=None, type=0, listening=-1): # real signature unknown; restored from __doc__
    """
    _is_socket(fd, family=AF_UNSPEC, type=0, listening=-1) -> bool
    
    Returns True iff the descriptor refers to a socket.
    Wraps sd_is_socket(3).
    
    Constants for `family` are defined in the socket module.
    """
    return False

def _is_socket_inet(fd, family=None, type=0, listening=-1, port=0): # real signature unknown; restored from __doc__
    """
    _is_socket_inet(fd, family=AF_UNSPEC, type=0, listening=-1, port=0) -> bool
    
    Wraps sd_is_socket_inet(3).
    
    Constants for `family` are defined in the socket module.
    """
    return False

def _is_socket_unix(fd, type, listening, path): # real signature unknown; restored from __doc__
    """
    _is_socket_unix(fd, type, listening, path) -> bool
    
    Wraps sd_is_socket_unix(3).
    """
    return False

def _listen_fds(unset_environment=True): # real signature unknown; restored from __doc__
    """
    _listen_fds(unset_environment=True) -> int
    
    Return the number of descriptors passed to this process by the init system
    as part of the socket-based activation logic.
    Wraps sd_listen_fds(3).
    """
    return 0

# no classes
# variables with complex values

__loader__ = None # (!) real value is ''

__spec__ = None # (!) real value is ''

