# encoding: utf-8
# module apt_inst
# from /usr/lib/python3/dist-packages/apt_inst.cpython-35m-x86_64-linux-gnu.so
# by generator 1.145
"""
Functions for working with ar/tar archives and .deb packages.

This module provides useful classes and functions to work with
archives, modelled after the 'TarFile' class in the 'tarfile' module.
"""
# no imports

# no functions
# classes

class ArArchive(object):
    """
    ArArchive(file: str/int/file)
    
    Represent an archive in the 4.4 BSD ar format,
    which is used for e.g. deb packages.
    
    The parameter 'file' may be a string specifying the path of a file, or
    a file-like object providing the fileno() method. It may also be an int
    specifying a file descriptor (returned by e.g. os.open()).
    The recommended way of using it is to pass in the path to the file.
    """
    def extract(self, name, target=None): # real signature unknown; restored from __doc__
        """
        extract(name: str[, target: str]) -> bool
        
        Extract the member given by 'name' into the directory given
        by 'target'. If the extraction fails, raise OSError. In case
        of success, return True if the file owner could be set or
        False if this was not possible. If the requested member
        does not exist, raise LookupError.
        """
        return False

    def extractall(self, target=None): # real signature unknown; restored from __doc__
        """
        extractall([target: str]) -> bool
        
        Extract all archive contents into the directory given by 'target'. If
        the extraction fails, raise an error. Otherwise, return True if the
        owner could be set or False if the owner could not be changed.
        """
        return False

    def extractdata(self, name): # real signature unknown; restored from __doc__
        """
        extractdata(name: str) -> bytes
        
        Return the contents of the member, as a bytes object. Raise
        LookupError if there is no ArMember with the given name.
        """
        return b""

    def getmember(self, name): # real signature unknown; restored from __doc__
        """
        getmember(name: str) -> ArMember
        
        Return an ArMember object for the member given by 'name'. Raise
        LookupError if there is no ArMember with the given name.
        """
        return ArMember

    def getmembers(self): # real signature unknown; restored from __doc__
        """
        getmembers() -> list
        
        Return a list of all members in the archive.
        """
        return []

    def getnames(self): # real signature unknown; restored from __doc__
        """
        getnames() -> list
        
        Return a list of the names of all members in the archive.
        """
        return []

    def gettar(self, name, comp): # real signature unknown; restored from __doc__
        """
        gettar(name: str, comp: str) -> TarFile
        
        Return a TarFile object for the member given by 'name' which will be
        decompressed using the compression algorithm given by 'comp'.
        This is almost equal to:
        
           member = arfile.getmember(name)
           tarfile = TarFile(file, member.start, member.size, 'gzip')'
        
        It just opens a new TarFile on the given position in the stream.
        """
        return TarFile

    def __contains__(self, *args, **kwargs): # real signature unknown
        """ Return key in self. """
        pass

    def __getitem__(self, *args, **kwargs): # real signature unknown
        """ Return self[key]. """
        pass

    def __init__(self, file, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        pass

    def __iter__(self, *args, **kwargs): # real signature unknown
        """ Implement iter(self). """
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass


class ArMember(object):
    """
    Represent a single file within an AR archive. For
    Debian packages this can be e.g. control.tar.gz. This class provides
    information about this file, such as the mode and size.
    """
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    gid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The group id of the owner."""

    mode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The mode of the file."""

    mtime = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Last time of modification."""

    name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The name of the file."""

    size = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The size of the files."""

    start = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The offset in the archive where the file starts."""

    uid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The user ID of the owner."""



class DebFile(ArArchive):
    """
    DebFile(file: str/int/file)
    
    A DebFile object represents a file in the .deb package format.
    
    The parameter 'file' may be a string specifying the path of a file, or
    a file-like object providing the fileno() method. It may also be an int
    specifying a file descriptor (returned by e.g. os.open()).
    The recommended way of using it is to pass in the path to the file.
    
    It differs from ArArchive by providing the members 'control', 'data'
    and 'version' for accessing the control.tar.gz, data.tar.$compression 
    (all apt compression methods are supported), and debian-binary members 
    in the archive.
    """
    def __init__(self, file, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    control = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The TarFile object associated with the control.tar.gz member."""

    data = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The TarFile object associated with the data.tar.$compression member. All apt compression methods are supported. """

    debian_binary = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The package version, as contained in debian-binary."""



class TarFile(object):
    """
    TarFile(file: str/int/file[, min: int, max: int, comp: str])
    
    The parameter 'file' may be a string specifying the path of a file, or
    a file-like object providing the fileno() method. It may also be an int
    specifying a file descriptor (returned by e.g. os.open()).
    
    The parameter 'min' describes the offset in the file where the archive
    begins and the parameter 'max' is the size of the archive.
    
    The compression of the archive is set by the parameter 'comp'. It can
    be set to any program supporting the -d switch, the default being gzip.
    """
    def extractall(self, rootdir=None): # real signature unknown; restored from __doc__
        """
        extractall([rootdir: str]) -> True
        
        Extract the archive in the current directory. The argument 'rootdir'
        can be used to change the target directory.
        """
        return False

    def extractdata(self, member): # real signature unknown; restored from __doc__
        """
        extractdata(member: str) -> bytes
        
        Return the contents of the member, as a bytes object. Raise
        LookupError if there is no member with the given name.
        """
        return b""

    def go(self, callback, member=None): # real signature unknown; restored from __doc__
        """
        go(callback: callable[, member: str]) -> True
        
        Go through the archive and call the callable 'callback' for each
        member with 2 arguments. The first argument is the TarMember and
        the second one is the data, as bytes.
        
        The optional parameter 'member' can be used to specify the member for
        which to call the callback. If not specified, it will be called for all
        members. If specified and not found, LookupError will be raised.
        """
        return False

    def __init__(self, file, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass


class TarMember(object):
    """
    Represent a single member of a 'tar' archive.
    
    This class, which has been modelled after 'tarfile.TarInfo', represents
    information about a given member in an archive.
    """
    def isblk(self, *args, **kwargs): # real signature unknown
        """ Determine whether the member is a block device. """
        pass

    def ischr(self, *args, **kwargs): # real signature unknown
        """ Determine whether the member is a character device. """
        pass

    def isdev(self, *args, **kwargs): # real signature unknown
        """ Determine whether the member is a device (block, character or FIFO). """
        pass

    def isdir(self, *args, **kwargs): # real signature unknown
        """ Determine whether the member is a directory. """
        pass

    def isfifo(self, *args, **kwargs): # real signature unknown
        """ Determine whether the member is a FIFO. """
        pass

    def isfile(self, *args, **kwargs): # real signature unknown
        """ Determine whether the member is a regular file. """
        pass

    def islnk(self, *args, **kwargs): # real signature unknown
        """ Determine whether the member is a hardlink. """
        pass

    def isreg(self, *args, **kwargs): # real signature unknown
        """ Determine whether the member is a regular file, same as isfile(). """
        pass

    def issym(self, *args, **kwargs): # real signature unknown
        """ Determine whether the member is a symbolic link. """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    gid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The owner's group ID."""

    linkname = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The target of the link."""

    major = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The major ID of the device."""

    minor = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The minor ID of the device."""

    mode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The mode (permissions)."""

    mtime = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Last time of modification."""

    name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The name of the file."""

    size = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The size of the file."""

    uid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The owner's user ID."""



# variables with complex values

__loader__ = None # (!) real value is ''

__spec__ = None # (!) real value is ''

