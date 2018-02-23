# encoding: utf-8
# module systemd.login
# from /usr/lib/python3/dist-packages/systemd/login.cpython-35m-x86_64-linux-gnu.so
# by generator 1.145
""" Python interface to the libsystemd-login library. """
# no imports

# Variables with simple values

__version__ = '231'

# functions

def machine_names(): # real signature unknown; restored from __doc__
    """
    machine_names() -> list
    
    Returns a list of currently running virtual machines
    and containers on the system.
    Wraps sd_get_machine_names(3).
    """
    return []

def seats(): # real signature unknown; restored from __doc__
    """
    seats() -> list
    
    Returns a list of currently available local seats.
    Wraps sd_get_seats(3).
    """
    return []

def sessions(): # real signature unknown; restored from __doc__
    """
    sessions() -> list
    
    Returns a list of current login sessions.
    Wraps sd_get_sessions(3).
    """
    return []

def uids(): # real signature unknown; restored from __doc__
    """
    uids() -> list
    
    Returns a list of uids of users who currently have login sessions.
    Wraps sd_get_uids(3).
    """
    return []

# classes

class Monitor(object):
    """
    Monitor([category]) -> ...
    
    Monitor may be used to monitor login sessions, users, seats,
    and virtual machines/containers. Monitor provides a file
    descriptor which can be integrated in an external event loop.
    See man:sd_login_monitor_new(3) for the details about what
    can be monitored.
    """
    def close(self): # real signature unknown; restored from __doc__
        """
        close() -> None
        
        Free resources allocated by this Monitor object.
        This method invokes sd_login_monitor_unref().
        See man:sd_login_monitor_unref(3).
        """
        pass

    def fileno(self): # real signature unknown; restored from __doc__
        """
        fileno() -> int
        
        Get a file descriptor to poll for events.
        This method wraps sd_login_monitor_get_fd(3).
        """
        return 0

    def flush(self): # real signature unknown; restored from __doc__
        """
        flush() -> None
        
        Reset the wakeup state of the monitor object.
        This method invokes sd_login_monitor_flush().
        See man:sd_login_monitor_flush(3).
        """
        pass

    def get_events(self): # real signature unknown; restored from __doc__
        """
        get_events() -> int
        
        Returns a mask of poll() events to wait for on the file
        descriptor returned by .fileno().
        
        See man:sd_login_monitor_get_events(3) for further discussion.
        """
        return 0

    def get_timeout(self): # real signature unknown; restored from __doc__
        """
        get_timeout() -> int or None
        
        Returns a timeout value for usage in poll(), the time since the
        epoch of clock_gettime(2) in microseconds, or None if no timeout
        is necessary.
        
        The return value must be converted to a relative timeout in
        milliseconds if it is to be used as an argument for poll().
        See man:sd_login_monitor_get_timeout(3) for further discussion.
        """
        return 0

    def get_timeout_ms(self): # real signature unknown; restored from __doc__
        """
        get_timeout_ms() -> int
        
        Returns a timeout value suitable for usage in poll(), the value
        returned by .get_timeout() converted to relative ms, or -1 if
        no timeout is necessary.
        """
        return 0

    def __enter__(self): # real signature unknown; restored from __doc__
        """
        __enter__() -> self
        
        Part of the context manager protocol.
        Returns self.
        """
        return self

    def __exit__(self, type, value, traceback): # real signature unknown; restored from __doc__
        """
        __exit__(type, value, traceback) -> None
        
        Part of the context manager protocol.
        Closes the monitor..
        """
        pass

    def __init__(self, category=None): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass


# variables with complex values

__loader__ = None # (!) real value is ''

__spec__ = None # (!) real value is ''

