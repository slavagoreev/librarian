# encoding: utf-8
# module grp
# from (built-in)
# by generator 1.145
"""
Access to the Unix group database.

Group entries are reported as 4-tuples containing the following fields
from the group database, in order:

  gr_name   - name of the group
  gr_passwd - group password (encrypted); often empty
  gr_gid    - numeric ID of the group
  gr_mem    - list of members

The gid is an integer, name and password are strings.  (Note that most
users are not explicitly listed as members of the groups they are in
according to the password database.  Check both databases to get
complete membership information.)
"""
# no imports

# functions

def getgrall(*args, **kwargs): # real signature unknown
    """
    Return a list of all available group entries, in arbitrary order.
    
    An entry whose name starts with '+' or '-' represents an instruction
    to use YP/NIS and may not be accessible via getgrnam or getgrgid.
    """
    pass

def getgrgid(*args, **kwargs): # real signature unknown
    """
    Return the group database entry for the given numeric group ID.
    
    If id is not valid, raise KeyError.
    """
    pass

def getgrnam(*args, **kwargs): # real signature unknown
    """
    Return the group database entry for the given group name.
    
    If name is not valid, raise KeyError.
    """
    pass

# classes

class struct_group(tuple):
    """
    grp.struct_group: Results from getgr*() routines.
    
    This object may be accessed either as a tuple of
      (gr_name,gr_passwd,gr_gid,gr_mem)
    or via the object attributes as named in the above tuple.
    """
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    gr_gid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """group id"""

    gr_mem = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """group members"""

    gr_name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """group name"""

    gr_passwd = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """password"""


    n_fields = 4
    n_sequence_fields = 4
    n_unnamed_fields = 0


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

