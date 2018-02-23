# encoding: utf-8
# module _posixsubprocess
# from /usr/local/lib/python3.5/dist-packages/zmq/devices/monitoredqueue.cpython-35m-x86_64-linux-gnu.so
# by generator 1.145
""" A POSIX helper for the subprocess module. """
# no imports

# functions

def fork_exec(args, executable_list, close_fds, cwd, env, p2cread, p2cwrite, c2pread, c2pwrite, errread, errwrite, errpipe_read, errpipe_write, restore_signals, call_setsid, preexec_fn): # real signature unknown; restored from __doc__
    """
    fork_exec(args, executable_list, close_fds, cwd, env,
              p2cread, p2cwrite, c2pread, c2pwrite,
              errread, errwrite, errpipe_read, errpipe_write,
              restore_signals, call_setsid, preexec_fn)
    
    Forks a child process, closes parent file descriptors as appropriate in the
    child and dups the few that are needed before calling exec() in the child
    process.
    
    The preexec_fn, if supplied, will be called immediately before exec.
    WARNING: preexec_fn is NOT SAFE if your application uses threads.
             It may trigger infrequent, difficult to debug deadlocks.
    
    If an error occurs in the child process before the exec, it is
    serialized and written to the errpipe_write fd per subprocess.py.
    
    Returns: the child process's PID.
    
    Raises: Only on an error in the parent process.
    """
    pass

# classes

class __loader__(object):
    """
    Meta path import for built-in modules.
    
        All methods are either class or static methods to avoid the need to
        instantiate the class.
    """
    @classmethod
    def create_module(cls, *args, **kwargs): # real signature unknown
        """ Create a built-in module """
        pass

    @classmethod
    def exec_module(cls, *args, **kwargs): # real signature unknown
        """ Exec a built-in module """
        pass

    @classmethod
    def find_module(cls, *args, **kwargs): # real signature unknown
        """
        Find the built-in module.
        
                If 'path' is ever specified then the search is considered a failure.
        
                This method is deprecated.  Use find_spec() instead.
        """
        pass

    @classmethod
    def find_spec(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def get_code(cls, *args, **kwargs): # real signature unknown
        """ Return None as built-in modules do not have code objects. """
        pass

    @classmethod
    def get_source(cls, *args, **kwargs): # real signature unknown
        """ Return None as built-in modules do not have source code. """
        pass

    @classmethod
    def is_package(cls, *args, **kwargs): # real signature unknown
        """ Return False as built-in modules are never packages. """
        pass

    @classmethod
    def load_module(cls, *args, **kwargs): # real signature unknown
        """
        Load the specified module into sys.modules and return it.
        
            This method is deprecated.  Use loader.exec_module instead.
        """
        pass

    def module_repr(module): # reliably restored by inspect
        """
        Return repr for the module.
        
                The method is deprecated.  The import machinery does the job itself.
        """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    __dict__ = None # (!) real value is ''


# variables with complex values

__spec__ = None # (!) real value is ''

