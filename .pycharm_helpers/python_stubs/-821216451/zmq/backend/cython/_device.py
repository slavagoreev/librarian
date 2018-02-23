# encoding: utf-8
# module zmq.backend.cython._device
# from /usr/local/lib/python3.5/dist-packages/zmq/backend/cython/_device.cpython-35m-x86_64-linux-gnu.so
# by generator 1.145
""" Python binding for 0MQ device function. """

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>
import zmq.error as __zmq_error


# functions

def device(device_type, frontend, backend): # real signature unknown; restored from __doc__
    """
    device(device_type, frontend, backend)
    
        Start a zeromq device.
        
        .. deprecated:: libzmq-3.2
            Use zmq.proxy
    
        Parameters
        ----------
        device_type : (QUEUE, FORWARDER, STREAMER)
            The type of device to start.
        frontend : Socket
            The Socket instance for the incoming traffic.
        backend : Socket
            The Socket instance for the outbound traffic.
    """
    pass

def proxy(frontend, backend, capture): # real signature unknown; restored from __doc__
    """
    proxy(frontend, backend, capture)
        
        Start a zeromq proxy (replacement for device).
        
        .. versionadded:: libzmq-3.2
        .. versionadded:: 13.0
        
        Parameters
        ----------
        frontend : Socket
            The Socket instance for the incoming traffic.
        backend : Socket
            The Socket instance for the outbound traffic.
        capture : Socket (optional)
            The Socket instance for capturing traffic.
    """
    pass

# classes

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
    'device',
    'proxy',
]

__loader__ = None # (!) real value is ''

__spec__ = None # (!) real value is ''

__test__ = {}

