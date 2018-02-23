# encoding: utf-8
# module systemd._reader
# from /usr/lib/python3/dist-packages/systemd/_reader.cpython-35m-x86_64-linux-gnu.so
# by generator 1.145
""" Class to reads the systemd journal similar to journalctl. """
# no imports

# Variables with simple values

APPEND = 1

CURRENT_USER = 8

INVALIDATE = 2

LOCAL_ONLY = 1

NOP = 0

RUNTIME_ONLY = 2

SYSTEM = 4

SYSTEM_ONLY = 4

__version__ = '231'

# functions

def _get_catalog(*args, **kwargs): # real signature unknown
    """
    get_catalog(id128) -> str
    
    Retrieve a message catalog entry for the given id.
    Wraps man:sd_journal_get_catalog_for_message_id(3).
    """
    pass

# classes

class Monotonic(tuple):
    """ A tuple of (timestamp, bootid) for holding monotonic timestamps """
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

    bootid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Unique identifier of the boot"""

    timestamp = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Time"""


    n_fields = 2
    n_sequence_fields = 2
    n_unnamed_fields = 0


class _Reader(object):
    """
    _Reader([flags | path | files]) -> ...
    
    _Reader allows filtering and retrieval of Journal entries.
    Note: this is a low-level interface, and probably not what you
    want, use systemd.journal.Reader instead.
    
    Argument `flags` sets open flags of the journal, which can be one
    of, or ORed combination of constants: LOCAL_ONLY (default) opens
    journal on local machine only; RUNTIME_ONLY opens only
    volatile journal files; and SYSTEM opens journal files of
    system services and the kernel, and CURRENT_USER opens files
    of the current user.
    
    Argument `path` is the directory of journal files.
    Argument `files` is a list of files. Note that
    `flags`, `path`, and `files` are exclusive.
    
    _Reader implements the context manager protocol: the journal
    will be closed when exiting the block.
    """
    def add_conjunction(self): # real signature unknown; restored from __doc__
        """
        add_conjunction() -> None
        
        Inserts a logical AND between matches added since previous
        add_disjunction() or add_conjunction() and the next
        add_disjunction() or add_conjunction().
        
        See man:sd_journal_add_disjunction(3) for explanation.
        """
        pass

    def add_disjunction(self): # real signature unknown; restored from __doc__
        """
        add_disjunction() -> None
        
        Inserts a logical OR between matches added since previous
        add_disjunction() or add_conjunction() and the next
        add_disjunction() or add_conjunction().
        
        See man:sd_journal_add_disjunction(3) for explanation.
        """
        pass

    def add_match(self, match): # real signature unknown; restored from __doc__
        """
        add_match(match) -> None
        
        Add a match to filter journal log entries. All matches of different
        fields are combined with logical AND, and matches of the same field
        are automatically combined with logical OR.
        Match is a string of the form "FIELD=value".
        """
        pass

    def close(self): # real signature unknown; restored from __doc__
        """
        close() -> None
        
        Free resources allocated by this Reader object.
        This method invokes sd_journal_close().
        See man:sd_journal_close(3).
        """
        pass

    def fileno(self): # real signature unknown; restored from __doc__
        """
        fileno() -> int
        
        Get a file descriptor to poll for changes in the journal.
        This method invokes sd_journal_get_fd().
        See man:sd_journal_get_fd(3).
        """
        return 0

    def flush_matches(self): # real signature unknown; restored from __doc__
        """
        flush_matches() -> None
        
        Clear all current match filters.
        """
        pass

    def get_catalog(self): # real signature unknown; restored from __doc__
        """
        get_catalog() -> str
        
        Retrieve a message catalog entry for the current journal entry.
        Will throw IndexError if the entry has no MESSAGE_ID
        and KeyError is the id is specified, but hasn't been found
        in the catalog.
        
        Wraps man:sd_journal_get_catalog(3).
        """
        return ""

    def get_events(self): # real signature unknown; restored from __doc__
        """
        get_events() -> int
        
        Returns a mask of poll() events to wait for on the file
        descriptor returned by .fileno().
        
        See man:sd_journal_get_events(3) for further discussion.
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
        See man:sd_journal_get_timeout(3) for further discussion.
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

    def get_usage(self): # real signature unknown; restored from __doc__
        """
        get_usage() -> int
        
        Returns the total disk space currently used by journal
        files (in bytes). If `SD_JOURNAL_LOCAL_ONLY` was
        passed when opening the journal this value will only reflect
        the size of journal files of the local host, otherwise
        of all hosts.
        
        This method invokes sd_journal_get_usage().
        See man:sd_journal_get_usage(3).
        """
        return 0

    def process(self): # real signature unknown; restored from __doc__
        """
        process() -> state change (integer)
        
        Process events and reset the readable state of the file
        descriptor returned by .fileno().
        
        Will return constants: NOP if no change; APPEND if new
        entries have been added to the end of the journal; and
        INVALIDATE if journal files have been added or removed.
        
        See man:sd_journal_process(3) for further discussion.
        """
        pass

    def query_unique(self, field): # real signature unknown; restored from __doc__
        """
        query_unique(field) -> a set of values
        
        Return a set of unique values appearing in journal for the
        given `field`. Note this does not respect any journal matches.
        """
        pass

    def reliable_fd(self): # real signature unknown; restored from __doc__
        """
        reliable_fd() -> bool
        
        Returns True iff the journal can be polled reliably.
        This method invokes sd_journal_reliable_fd().
        See man:sd_journal_reliable_fd(3).
        """
        return False

    def seek_cursor(self, cursor): # real signature unknown; restored from __doc__
        """
        seek_cursor(cursor) -> None
        
        Seek to journal entry by given unique reference `cursor`.
        """
        pass

    def seek_head(self): # real signature unknown; restored from __doc__
        """
        seek_head() -> None
        
        Jump to the beginning of the journal.
        This method invokes sd_journal_seek_head().
        See man:sd_journal_seek_head(3).
        """
        pass

    def seek_monotonic(self, monotonic, bootid=None): # real signature unknown; restored from __doc__
        """
        seek_monotonic(monotonic[, bootid]) -> None
        
        Seek to nearest matching journal entry to `monotonic`. Argument
        `monotonic` is an timestamp from boot in microseconds.
        Argument `bootid` is a string representing which boot the
        monotonic time is reference to. Defaults to current bootid.
        """
        pass

    def seek_realtime(self, realtime): # real signature unknown; restored from __doc__
        """
        seek_realtime(realtime) -> None
        
        Seek to nearest matching journal entry to `realtime`. Argument
        `realtime` in specified in seconds.
        """
        pass

    def seek_tail(self): # real signature unknown; restored from __doc__
        """
        seek_tail() -> None
        
        Jump to the end of the journal.
        This method invokes sd_journal_seek_tail().
        See man:sd_journal_seek_tail(3).
        """
        pass

    def test_cursor(self, p_str): # real signature unknown; restored from __doc__
        """
        test_cursor(str) -> bool
        
        Test whether the cursor string matches current journal entry.
        
        Wraps sd_journal_test_cursor(). See man:sd_journal_test_cursor(3).
        """
        return False

    def wait(self, timeout=None): # real signature unknown; restored from __doc__
        """
        wait([timeout]) -> state change (integer)
        
        Wait for a change in the journal. Argument `timeout` specifies
        the maximum number of microseconds to wait before returning
        regardless of wheter the journal has changed. If `timeout` is -1,
        then block forever.
        
        Will return constants: NOP if no change; APPEND if new
        entries have been added to the end of the journal; and
        INVALIDATE if journal files have been added or removed.
        
        See man:sd_journal_wait(3) for further discussion.
        """
        pass

    def _get(self, *args, **kwargs): # real signature unknown
        """
        get(str) -> str
        
        Return data associated with this key in current log entry.
        Throws KeyError is the data is not available.
        """
        pass

    def _get_all(self): # real signature unknown; restored from __doc__
        """
        _get_all() -> dict
        
        Return dictionary of the current log entry.
        """
        return {}

    def _get_cursor(self): # real signature unknown; restored from __doc__
        """
        get_cursor() -> str
        
        Return a cursor string for the current journal entry.
        
        Wraps sd_journal_get_cursor(). See man:sd_journal_get_cursor(3).
        """
        pass

    def _get_monotonic(self, *args, **kwargs): # real signature unknown
        """
        get_monotonic() -> (timestamp, bootid)
        
        Return the monotonic timestamp for the current journal entry
        as a tuple of time in microseconds and bootid.
        
        Wraps sd_journal_get_monotonic_usec().
        See man:sd_journal_get_monotonic_usec(3).
        """
        pass

    def _get_realtime(self, *args, **kwargs): # real signature unknown
        """
        get_realtime() -> int
        
        Return the realtime timestamp for the current journal entry
        in microseconds.
        
        Wraps sd_journal_get_realtime_usec().
        See man:sd_journal_get_realtime_usec(3).
        """
        pass

    def _next(self, *args, **kwargs): # real signature unknown
        """
        next([skip]) -> bool
        
        Go to the next log entry. Optional skip value means to go to
        the `skip`\-th log entry.
        Returns False if at end of file, True otherwise.
        """
        pass

    def _previous(self, *args, **kwargs): # real signature unknown
        """
        previous([skip]) -> bool
        
        Go to the previous log entry. Optional skip value means to 
        go to the `skip`\-th previous log entry.
        Returns False if at start of file, True otherwise.
        """
        pass

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
        Closes the journal.
        """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    closed = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """True iff journal is closed"""

    data_threshold = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Threshold for field size truncation in bytes.

Fields longer than this will be truncated to the threshold size.
Defaults to 64Kb."""



# variables with complex values

__loader__ = None # (!) real value is ''

__spec__ = None # (!) real value is ''

