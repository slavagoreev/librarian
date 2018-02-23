# encoding: utf-8
# module zmq.devices.monitoredqueue
# from /usr/local/lib/python3.5/dist-packages/zmq/devices/monitoredqueue.cpython-35m-x86_64-linux-gnu.so
# by generator 1.145
"""
MonitoredQueue classes and functions.

Authors
-------
* MinRK
* Brian Granger
"""

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>
import zmq.error as __zmq_error


# Variables with simple values

ROUTER = 6

# functions

def monitored_queue(in_socket, out_socket, mon_socket, in_prefix=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    monitored_queue(in_socket, out_socket, mon_socket,
                           in_prefix=b'in', out_prefix=b'out')
        
        Start a monitored queue device.
        
        A monitored queue is very similar to the zmq.proxy device (monitored queue came first).
        
        Differences from zmq.proxy:
        
        - monitored_queue supports both in and out being ROUTER sockets
          (via swapping IDENTITY prefixes).
        - monitor messages are prefixed, making in and out messages distinguishable.
        
        Parameters
        ----------
        in_socket : Socket
            One of the sockets to the Queue. Its messages will be prefixed with
            'in'.
        out_socket : Socket
            One of the sockets to the Queue. Its messages will be prefixed with
            'out'. The only difference between in/out socket is this prefix.
        mon_socket : Socket
            This socket sends out every message received by each of the others
            with an in/out prefix specifying which one it was.
        in_prefix : str
            Prefix added to broadcast messages from in_socket.
        out_prefix : str
            Prefix added to broadcast messages from out_socket.
    """
    pass

# classes

class ZMQError(__zmq_error.ZMQBaseError):
    """
    Wrap an errno style error.
    
        Parameters
        ----------
        errno : int
            The ZMQ errno or None.  If None, then ``zmq_errno()`` is called and
            used.
        msg : string
            Description of the error or None.
    """
    def __init__(self, errno=None, msg=None): # reliably restored by inspect
        """
        Wrap an errno style error.
        
                Parameters
                ----------
                errno : int
                    The ZMQ errno or None.  If None, then ``zmq_errno()`` is called and
                    used.
                msg : string
                    Description of the error or None.
        """
        pass

    def __repr__(self): # reliably restored by inspect
        # no doc
        pass

    def __str__(self): # reliably restored by inspect
        # no doc
        pass

    errno = None


class InterruptedSystemCall(__zmq_error.ZMQError, InterruptedError):
    """
    Wrapper for EINTR
        
        This exception should be caught internally in pyzmq
        to retry system calls, and not propagate to the user.
        
        .. versionadded:: 14.7
    """
    def __init__(self, errno=None, msg=None): # reliably restored by inspect
        # no doc
        pass

    def __str__(self): # reliably restored by inspect
        # no doc
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



# variables with complex values

__all__ = [
    'monitored_queue',
]

__loader__ = None # (!) real value is ''

__spec__ = None # (!) real value is ''

__test__ = {}

