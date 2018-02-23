# encoding: utf-8
# module systemd.id128
# from /usr/lib/python3/dist-packages/systemd/id128.cpython-35m-x86_64-linux-gnu.so
# by generator 1.145
"""
Python interface to the libsystemd-id128 library.

Provides SD_MESSAGE_* constants and functions to query and generate
128-bit unique identifiers.
"""
# no imports

# Variables with simple values

__version__ = '231'

# functions

def get_boot(): # real signature unknown; restored from __doc__
    """
    get_boot() -> UUID
    
    Return a 128-bit unique identifier for this boot.
    Wraps sd_id128_get_boot(3).
    """
    pass

def get_machine(): # real signature unknown; restored from __doc__
    """
    get_machine() -> UUID
    
    Return a 128-bit unique identifier for this machine.
    Wraps sd_id128_get_machine(3).
    """
    pass

def randomize(): # real signature unknown; restored from __doc__
    """
    randomize() -> UUID
    
    Return a new random 128-bit unique identifier.
    Wraps sd_id128_randomize(3).
    """
    pass

# no classes
# variables with complex values

SD_MESSAGE_BOOTCHART = None # (!) real value is ''

SD_MESSAGE_COREDUMP = None # (!) real value is ''

SD_MESSAGE_FORWARD_SYSLOG_MISSED = None # (!) real value is ''

SD_MESSAGE_HIBERNATE_KEY = None # (!) real value is ''

SD_MESSAGE_INVALID_CONFIGURATION = None # (!) real value is ''

SD_MESSAGE_JOURNAL_DROPPED = None # (!) real value is ''

SD_MESSAGE_JOURNAL_MISSED = None # (!) real value is ''

SD_MESSAGE_JOURNAL_START = None # (!) real value is ''

SD_MESSAGE_JOURNAL_STOP = None # (!) real value is ''

SD_MESSAGE_JOURNAL_USAGE = None # (!) real value is ''

SD_MESSAGE_LID_CLOSED = None # (!) real value is ''

SD_MESSAGE_LID_OPENED = None # (!) real value is ''

SD_MESSAGE_MACHINE_START = None # (!) real value is ''

SD_MESSAGE_MACHINE_STOP = None # (!) real value is ''

SD_MESSAGE_OVERMOUNTING = None # (!) real value is ''

SD_MESSAGE_POWER_KEY = None # (!) real value is ''

SD_MESSAGE_SEAT_START = None # (!) real value is ''

SD_MESSAGE_SEAT_STOP = None # (!) real value is ''

SD_MESSAGE_SESSION_START = None # (!) real value is ''

SD_MESSAGE_SESSION_STOP = None # (!) real value is ''

SD_MESSAGE_SHUTDOWN = None # (!) real value is ''

SD_MESSAGE_SLEEP_START = None # (!) real value is ''

SD_MESSAGE_SLEEP_STOP = None # (!) real value is ''

SD_MESSAGE_SPAWN_FAILED = None # (!) real value is ''

SD_MESSAGE_STARTUP_FINISHED = None # (!) real value is ''

SD_MESSAGE_SUSPEND_KEY = None # (!) real value is ''

SD_MESSAGE_SYSTEM_DOCKED = None # (!) real value is ''

SD_MESSAGE_SYSTEM_UNDOCKED = None # (!) real value is ''

SD_MESSAGE_TIMEZONE_CHANGE = None # (!) real value is ''

SD_MESSAGE_TIME_CHANGE = None # (!) real value is ''

SD_MESSAGE_UNIT_FAILED = None # (!) real value is ''

SD_MESSAGE_UNIT_RELOADED = None # (!) real value is ''

SD_MESSAGE_UNIT_RELOADING = None # (!) real value is ''

SD_MESSAGE_UNIT_STARTED = None # (!) real value is ''

SD_MESSAGE_UNIT_STARTING = None # (!) real value is ''

SD_MESSAGE_UNIT_STOPPED = None # (!) real value is ''

SD_MESSAGE_UNIT_STOPPING = None # (!) real value is ''

__loader__ = None # (!) real value is ''

__spec__ = None # (!) real value is ''

