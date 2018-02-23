# encoding: utf-8
# module apt_pkg
# from /usr/lib/python3/dist-packages/apt_pkg.cpython-35m-x86_64-linux-gnu.so
# by generator 1.145
"""
Classes and functions wrapping the apt-pkg library.

The apt_pkg module provides several classes and functions for accessing
the functionality provided by the apt-pkg library. Typical uses might
include reading APT index files and configuration files and installing
or removing packages.
"""
# no imports

# Variables with simple values

CURSTATE_CONFIG_FILES = 5

CURSTATE_HALF_CONFIGURED = 2
CURSTATE_HALF_INSTALLED = 4

CURSTATE_INSTALLED = 6

CURSTATE_NOT_INSTALLED = 0

CURSTATE_UNPACKED = 1

DATE = 'Jan 19 2016'

INSTSTATE_HOLD = 2

INSTSTATE_HOLD_REINSTREQ = 3

INSTSTATE_OK = 0
INSTSTATE_REINSTREQ = 1

LIB_VERSION = '5.0.0'

PRI_EXTRA = 5
PRI_IMPORTANT = 2
PRI_OPTIONAL = 4
PRI_REQUIRED = 1
PRI_STANDARD = 3

SELSTATE_DEINSTALL = 3
SELSTATE_HOLD = 2
SELSTATE_INSTALL = 1
SELSTATE_PURGE = 4
SELSTATE_UNKNOWN = 0

TIME = '11:46:03'

VERSION = '1.2.24'

# functions

def base64_encode(value): # real signature unknown; restored from __doc__
    """
    base64_encode(value: bytes) -> str
    
    Encode the given bytestring into Base64. The input may not
    contain a null byte character (use the base64 module for this).
    """
    return ""

def check_dep(pkg_ver, dep_op, dep_ver): # real signature unknown; restored from __doc__
    """
    check_dep(pkg_ver: str, dep_op: str, dep_ver: str) -> bool
    
    Check that the given requirement is fulfilled; i.e. that the version
    string given by 'pkg_ver' matches the version string 'dep_ver' under
    the condition specified by the operator 'dep_op' (<,<=,=,>=,>).
    
    Return True if 'pkg_ver' matches 'dep_ver' under the
    condition 'dep_op'; for example, this returns True:
    
        apt_pkg.check_dep('1', '<=', '2')
    """
    return False

def check_domain_list(host, domains): # real signature unknown; restored from __doc__
    """
    check_domain_list(host: str, domains: str) -> bool
    
    Check if the host given by 'host' belongs to one of the domains
    specified in the comma separated string 'domains'. An example
    would be:
    
        check_domain_list('alioth.debian.org','debian.net,debian.org')
    
    which would return True because alioth belongs to debian.org.
    """
    return False

def dequote_string(string): # real signature unknown; restored from __doc__
    """
    dequote_string(string: str) -> str
    
    Dequote the given string by replacing all HTTP encoded values such
    as '%20' with their decoded value (in this case, ' ').
    """
    return ""

def gettext(msg, domain='python-apt'): # real signature unknown; restored from __doc__
    """
    gettext(msg: str[, domain: str = 'python-apt']) -> str
    
    Translate the given string. This is much faster than Python's version
    and only does translations after setlocale() has been called.
    """
    return ""

def get_architectures(): # real signature unknown; restored from __doc__
    """
    get_architectures() -> list
    
    Return the list of supported architectures on this system. On a 
    multiarch system this can be more than one. The main architectures
    is the first item in the list.
    """
    return []

def get_lock(file, errors): # real signature unknown; restored from __doc__
    """
    get_lock(file: str, errors: bool) -> int
    
    Create an empty file of the given name and lock it. If the locking
    succeeds, return the file descriptor of the lock file. Afterwards,
    locking the file from another process will fail and thus cause
    get_lock() to return -1 or raise an Error (if 'errors' is True).
    
    From Python 2.6 on, it is recommended to use the context manager
    provided by apt_pkg.FileLock instead using the with-statement.
    """
    return 0

def init(): # real signature unknown; restored from __doc__
    """
    init()
    
    Shorthand for doing init_config() and init_system(). When working
    with command line arguments, first call init_config() then parse
    the command line and finally call init_system().
    """
    pass

def init_config(): # real signature unknown; restored from __doc__
    """
    init_config()
    
    Load the default configuration and the config file.
    """
    pass

def init_system(): # real signature unknown; restored from __doc__
    """
    init_system()
    
    Construct the apt_pkg system.
    """
    pass

def md5sum(p_object): # real signature unknown; restored from __doc__
    """
    md5sum(object) -> str
    
    Return the md5sum of the object. 'object' may either be a string, in
    which case the md5sum of the string is returned, or a file() object
    (or file descriptor), in which case the md5sum of its contents is
    returned.
    """
    return ""

def open_maybe_clear_signed_file(file): # real signature unknown; restored from __doc__
    """
    open_maybe_clear_signed_file(file: str) -> int
    
    Open a file and ignore a PGP clear signature.
    Return a open file descriptor or a error.
    """
    return 0

def parse_commandline(*args, **kwargs): # real signature unknown
    """
    parse_commandLine(config: Configuration, options: list, argv: list) -> list
    
    Parse the command line in 'argv' into the configuration space. The
    list 'options' contains a list of 3-tuples or 4-tuples in the form:
    
       (short_option: str, long_option: str, variable: str[, type: str])
    
    The element 'short_option' is one character, the 'long_option' element
    is the name of the long option, the element 'variable' the name of the
    configuration option the result will be stored in and type is one of
    'HasArg', 'IntLevel', 'Boolean', 'InvBoolean', 'ConfigFile',
    'ArbItem'. The default type is 'Boolean'. Read the online documentation
    in python-apt-doc and its tutorial on writing an apt-cdrom clone for more
    details.
    """
    pass

def parse_depends(s, strip_multi_arch=True): # real signature unknown; restored from __doc__
    """
    parse_depends(s: str[, strip_multi_arch : bool = True]) -> list
    
    Parse the dependencies given by 's' and return a list of lists. Each of
    these lists represents one or more options for an 'or' dependency in
    the form of '(pkg, ver, comptype)' tuples. The tuple element 'pkg'
    is the name of the package; the element 'ver' is the version, or ''
    if no version was requested. The element 'ver' is a comparison
    operator ('<', '<=', '=', '>=', or '>').
    
    If 'strip_multi_arch' is True, :any (and potentially other special values)
    will be stripped from the full package name
    """
    return []

def parse_src_depends(s, strip_multi_arch=True): # real signature unknown; restored from __doc__
    """
    parse_src_depends(s: str[, strip_multi_arch : bool = True]) -> list
    
    Parse the dependencies given by 's' and return a list of lists. Each of
    these lists represents one or more options for an 'or' dependency in
    the form of '(pkg, ver, comptype)' tuples. The tuple element 'pkg'
    is the name of the package; the element 'ver' is the version, or ''
    if no version was requested. The element 'ver' is a comparison
    operator ('<', '<=', '=', '>=', or '>').
    
    Dependencies may be restricted to certain architectures and the result
    only contains those dependencies for the architecture set in the
    configuration variable APT::Architecture
    
    If 'strip_multi_arch' is True, :any (and potentially other special values)
    will be stripped from the full package name
    """
    return []

def pkgsystem_lock(): # real signature unknown; restored from __doc__
    """
    pkgsystem_lock() -> bool
    
    Acquire the global lock for the package system by using /var/lib/dpkg/lock
    to do the locking. From Python 2.6 on, the apt_pkg.SystemLock context
    manager is available and should be used instead.
    """
    return False

def pkgsystem_unlock(): # real signature unknown; restored from __doc__
    """
    pkgsystem_unlock() -> bool
    
    Release the global lock for the package system.
    """
    return False

def quote_string(string, repl): # real signature unknown; restored from __doc__
    """
    quote_string(string: str, repl: str) -> str
    
    Escape the string 'string', replacing any character not allowed in a URLor specified by 'repl' with its ASCII value preceded by a percent sign(so for example ' ' becomes '%20').
    """
    return ""

def read_config_dir(configuration, dirname): # real signature unknown; restored from __doc__
    """
    read_config_dir(configuration: apt_pkg.Configuration, dirname: str)
    
    Read all configuration files in the dir given by 'dirname' in the
    correct order.
    """
    pass

def read_config_file(configuration, filename): # real signature unknown; restored from __doc__
    """
    read_config_file(configuration: apt_pkg.Configuration, filename: str)
    
    Read the configuration file 'filename' and set the appropriate
    options in the configuration object.
    """
    pass

def read_config_file_isc(*args, **kwargs): # real signature unknown
    """
    read_config_file(configuration: apt_pkg.Configuration, filename: str)
    
    Read the configuration file 'filename' and set the appropriate
    options in the configuration object.
    """
    pass

def rewrite_section(section, order, rewrite_list): # real signature unknown; restored from __doc__
    """
    rewrite_section(section: TagSection, order: list, rewrite_list: list) -> str
    
    Rewrite the section given by 'section' using 'rewrite_list', and order the
    fields according to 'order'.
    
    The parameter 'order' is a list object containing the names of the fields
    in the order they should appear in the rewritten section.
    apt_pkg.REWRITE_PACKAGE_ORDER and apt_pkg.REWRITE_SOURCE_ORDER are two
    predefined lists for rewriting package and source sections, respectively
    
    The parameter 'rewrite_list' is a list of tuples of the form
    '(tag, newvalue[, renamed_to])', where 'tag' describes the field which
    should be changed, 'newvalue' the value which should be inserted or None
    to delete the field, and the optional renamed_to can be used to rename the
    field.
    """
    return ""

def sha1sum(p_object): # real signature unknown; restored from __doc__
    """
    sha1sum(object) -> str
    
    Return the sha1sum of the object. 'object' may either be a string, in
    which case the sha1sum of the string is returned, or a file() object
    (or file descriptor), in which case the sha1sum of its contents is
    returned.
    """
    return ""

def sha256sum(p_object): # real signature unknown; restored from __doc__
    """
    sha256sum(object) -> str
    
    Return the sha256sum of the object. 'object' may either be a string, in
    which case the sha256sum of the string is returned, or a file() object
    (or file descriptor), in which case the sha256sum of its contents is
    returned.
    """
    return ""

def sha512sum(p_object): # real signature unknown; restored from __doc__
    """
    sha512sum(object) -> str
    
    Return the sha512sum of the object. 'object' may either be a string, in
    which case the sha512sum of the string is returned, or a file() object
    (or file descriptor), in which case the sha512sum of its contents is
    returned.
    """
    return ""

def size_to_str(bytes): # real signature unknown; restored from __doc__
    """
    size_to_str(bytes: int) -> str
    
    Return a string describing the size in a human-readable manner using
    SI prefix and base-10 units, e.g. '1k' for 1000, '1M' for 1000000, etc.
    """
    return ""

def string_to_bool(string): # real signature unknown; restored from __doc__
    """
    string_to_bool(string: str) -> int
    
    Return 1 if the string is a value such as 'yes', 'true', '1';
    0 if the string is a value such as 'no', 'false', '0'; -1 if
    the string is not recognized.
    """
    return 0

def str_to_time(rfc_time): # real signature unknown; restored from __doc__
    """
    str_to_time(rfc_time: str) -> int
    
    Convert the given RFC 1123 formatted string to a Unix timestamp.
    """
    return 0

def time_rfc1123(unixtime): # real signature unknown; restored from __doc__
    """
    time_rfc1123(unixtime: int) -> str
    
    Format the given Unix time according to the requirements of
    RFC 1123.
    """
    return ""

def time_to_str(seconds): # real signature unknown; restored from __doc__
    """
    time_to_str(seconds: int) -> str
    
    Return a string describing the number of seconds in a human
    readable manner using days, hours, minutes and seconds.
    """
    return ""

def upstream_version(ver): # real signature unknown; restored from __doc__
    """
    upstream_version(ver: str) -> str
    
    Return the upstream version for the package version given by 'ver'.
    """
    return ""

def uri_to_filename(uri): # real signature unknown; restored from __doc__
    """
    uri_to_filename(uri: str) -> str
    
    Return a filename based on the given URI after replacing some
    parts not suited for filenames (e.g. '/').
    """
    return ""

def version_compare(a, b): # real signature unknown; restored from __doc__
    """
    version_compare(a: str, b: str) -> int
    
    Compare the given versions; return a strictly negative value if 'a' is 
    smaller than 'b', 0 if they are equal, and a strictly positive value if
    'a' is larger than 'b'.
    """
    return 0

# classes

from .Acquire import Acquire
from .AcquireItem import AcquireItem
from .AcquireFile import AcquireFile
from .AcquireItemDesc import AcquireItemDesc
from .AcquireWorker import AcquireWorker
from .ActionGroup import ActionGroup
from .Cache import Cache
from .Cdrom import Cdrom
from .Configuration import Configuration
from .DepCache import DepCache
from .Dependency import Dependency
from .DependencyList import DependencyList
from .Description import Description
from .FileLock import FileLock
from .Group import Group
from .GroupList import GroupList
from .Hashes import Hashes
from .HashString import HashString
from .IndexFile import IndexFile
from .MetaIndex import MetaIndex
from .OrderList import OrderList
from .Package import Package
from .PackageFile import PackageFile
from .PackageList import PackageList
from ._PackageManager import _PackageManager
from .PackageManager import PackageManager
from .PackageRecords import PackageRecords
from .Policy import Policy
from .ProblemResolver import ProblemResolver
from .SourceList import SourceList
from .SourceRecords import SourceRecords
from .SystemLock import SystemLock
from .TagFile import TagFile
from .TagSection import TagSection
from .Version import Version
# variables with complex values

config = None # (!) real value is ''

REWRITE_PACKAGE_ORDER = [
    'Package',
    'Package-Type',
    'Architecture',
    'Subarchitecture',
    'Version',
    'Revision',
    'Package-Revision',
    'Package_Revision',
    'Kernel-Version',
    'Built-Using',
    'Built-For-Profiles',
    'Multi-Arch',
    'Status',
    'Priority',
    'Class',
    'Essential',
    'Installer-Menu-Item',
    'Section',
    'Source',
    'Origin',
    'Maintainer',
    'Original-Maintainer',
    'Bugs',
    'Config-Version',
    'Conffiles',
    'Triggers-Awaited',
    'Triggers-Pending',
    'Installed-Size',
    'Provides',
    'Pre-Depends',
    'Depends',
    'Recommends',
    'Recommended',
    'Suggests',
    'Optional',
    'Conflicts',
    'Breaks',
    'Replaces',
    'Enhances',
    'Filename',
    'MSDOS-Filename',
    'Size',
    'MD5sum',
    'SHA1',
    'SHA256',
    'SHA512',
    'Homepage',
    'Description',
    'Tag',
    'Task',
]

REWRITE_SOURCE_ORDER = [
    'Package',
    'Source',
    'Format',
    'Binary',
    'Architecture',
    'Version',
    'Priority',
    'Class',
    'Section',
    'Origin',
    'Maintainer',
    'Original-Maintainer',
    'Uploaders',
    'Dm-Upload-Allowed',
    'Standards-Version',
    'Build-Depends',
    'Build-Depends-Arch',
    'Build-Depends-Indep',
    'Build-Conflicts',
    'Build-Conflicts-Arch',
    'Build-Conflicts-Indep',
    'Testsuite',
    'Homepage',
    'Vcs-Browser',
    'Vcs-Browse',
    'Vcs-Arch',
    'Vcs-Bzr',
    'Vcs-Cvs',
    'Vcs-Darcs',
    'Vcs-Git',
    'Vcs-Hg',
    'Vcs-Mtn',
    'Vcs-Svn',
    'Directory',
    'Package-List',
    'Files',
    'Checksums-Md5',
    'Checksums-Sha1',
    'Checksums-Sha256',
    'Checksums-Sha512',
]

_C_API = None # (!) real value is ''

__loader__ = None # (!) real value is ''

__spec__ = None # (!) real value is ''

