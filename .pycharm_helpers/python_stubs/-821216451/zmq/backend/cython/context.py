# encoding: utf-8
# module zmq.backend.cython.context
# from /usr/local/lib/python3.5/dist-packages/zmq/backend/cython/context.cpython-35m-x86_64-linux-gnu.so
# by generator 1.145
""" 0MQ Context class. """

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>
import zmq.error as __zmq_error


# Variables with simple values

_instance = None

# functions

def __reduce_cython__(*args, **kwargs): # real signature unknown
    pass

def __setstate_cython__(*args, **kwargs): # real signature unknown
    pass

# classes

class Context(object):
    """
    Context(io_threads=1)
    
        Manage the lifecycle of a 0MQ context.
    
        Parameters
        ----------
        io_threads : int
            The number of IO threads.
    """
    def destroy(self, linger=None): # real signature unknown; restored from __doc__
        """
        ctx.destroy(linger=None)
                
                Close all sockets associated with this context, and then terminate
                the context. If linger is specified,
                the LINGER sockopt of the sockets will be set prior to closing.
                
                .. warning::
                
                    destroy involves calling ``zmq_close()``, which is **NOT** threadsafe.
                    If there are active sockets in other threads, this must not be called.
        """
        pass

    def get(self, option): # real signature unknown; restored from __doc__
        """
        ctx.get(option)
        
                Get the value of a context option.
        
                See the 0MQ API documentation for zmq_ctx_get
                for details on specific options.
                
                .. versionadded:: libzmq-3.2
                .. versionadded:: 13.0
        
                Parameters
                ----------
                option : int
                    The option to get.  Available values will depend on your
                    version of libzmq.  Examples include::
                    
                        zmq.IO_THREADS, zmq.MAX_SOCKETS
                    
                Returns
                -------
                optval : int
                    The value of the option as an integer.
        """
        pass

    def set(self, option, optval): # real signature unknown; restored from __doc__
        """
        ctx.set(option, optval)
        
                Set a context option.
        
                See the 0MQ API documentation for zmq_ctx_set
                for details on specific options.
                
                .. versionadded:: libzmq-3.2
                .. versionadded:: 13.0
        
                Parameters
                ----------
                option : int
                    The option to set.  Available values will depend on your
                    version of libzmq.  Examples include::
                    
                        zmq.IO_THREADS, zmq.MAX_SOCKETS
                
                optval : int
                    The value of the option to set.
        """
        pass

    def term(self): # real signature unknown; restored from __doc__
        """
        ctx.term()
        
                Close or terminate the context.
                
                This can be called to close the context by hand. If this is not called,
                the context will automatically be closed when it is garbage collected.
        """
        pass

    def __init__(self, io_threads=1): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        pass

    closed = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    underlying = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The address of the underlying libzmq context"""


    __pyx_vtable__ = None # (!) real value is ''


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
    'Context',
]

__loader__ = None # (!) real value is ''

__spec__ = None # (!) real value is ''

__test__ = {}

