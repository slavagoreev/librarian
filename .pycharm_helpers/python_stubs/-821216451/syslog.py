# encoding: utf-8
# module syslog
# from (built-in)
# by generator 1.145
# no doc
# no imports

# Variables with simple values

LOG_ALERT = 1
LOG_AUTH = 32
LOG_AUTHPRIV = 80
LOG_CONS = 2
LOG_CRIT = 2
LOG_CRON = 72
LOG_DAEMON = 24
LOG_DEBUG = 7
LOG_EMERG = 0
LOG_ERR = 3
LOG_INFO = 6
LOG_KERN = 0
LOG_LOCAL0 = 128
LOG_LOCAL1 = 136
LOG_LOCAL2 = 144
LOG_LOCAL3 = 152
LOG_LOCAL4 = 160
LOG_LOCAL5 = 168
LOG_LOCAL6 = 176
LOG_LOCAL7 = 184
LOG_LPR = 48
LOG_MAIL = 16
LOG_NDELAY = 8
LOG_NEWS = 56
LOG_NOTICE = 5
LOG_NOWAIT = 16
LOG_ODELAY = 4
LOG_PERROR = 32
LOG_PID = 1
LOG_SYSLOG = 40
LOG_USER = 8
LOG_UUCP = 64
LOG_WARNING = 4

# functions

def closelog(*args, **kwargs): # real signature unknown
    pass

def LOG_MASK(*args, **kwargs): # real signature unknown
    pass

def LOG_UPTO(*args, **kwargs): # real signature unknown
    pass

def openlog(*args, **kwargs): # real signature unknown
    pass

def setlogmask(*args, **kwargs): # real signature unknown
    pass

def syslog(*args, **kwargs): # real signature unknown
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

