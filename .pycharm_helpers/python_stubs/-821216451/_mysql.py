# encoding: utf-8
# module _mysql
# from /usr/local/lib/python3.5/dist-packages/_mysql.cpython-35m-x86_64-linux-gnu.so
# by generator 1.145
"""
an adaptation of the MySQL C API (mostly)

You probably are better off using MySQLdb instead of using this
module directly.

In general, renaming goes from mysql_* to _mysql.*. _mysql.connect()
returns a connection object (MYSQL). Functions which expect MYSQL * as
an argument are now methods of the connection object. A number of things
return result objects (MYSQL_RES). Functions which expect MYSQL_RES * as
an argument are now methods of the result object. Deprecated functions
(as of 3.23) are NOT implemented.
"""

# imports
import _mysql_exceptions as ___mysql_exceptions


# Variables with simple values

NULL = 'NULL'

__version__ = '1.3.12'

# functions

def connect(*args, **kwargs): # real signature unknown
    """
    Returns a MYSQL connection object. Exclusive use of
    keyword parameters strongly recommended. Consult the
    MySQL C API documentation for more details.
    
    host
      string, host to connect
    
    user
      string, user to connect as
    
    passwd
      string, password to use
    
    db
      string, database to use
    
    port
      integer, TCP/IP port to connect to
    
    unix_socket
      string, location of unix_socket (UNIX-ish only)
    
    conv
      mapping, maps MySQL FIELD_TYPE.* to Python functions which
      convert a string to the appropriate Python type
    
    connect_timeout
      number of seconds to wait before the connection
      attempt fails.
    
    compress
      if set, gzip compression is enabled
    
    named_pipe
      if set, connect to server via named pipe (Windows only)
    
    init_command
      command which is run once the connection is created
    
    read_default_file
      see the MySQL documentation for mysql_options()
    
    read_default_group
      see the MySQL documentation for mysql_options()
    
    client_flag
      client flags from MySQLdb.constants.CLIENT
    
    load_infile
      int, non-zero enables LOAD LOCAL INFILE, zero disables
    """
    pass

def debug(): # real signature unknown; restored from __doc__
    """
    Does a DBUG_PUSH with the given string.
    mysql_debug() uses the Fred Fish debug library.
    To use this function, you must compile the client library to
    support debugging.
    """
    pass

def escape(obj, dict): # real signature unknown; restored from __doc__
    """
    escape(obj, dict) -- escape any special characters in object obj
    using mapping dict to provide quoting functions for each type.
    Returns a SQL literal string.
    """
    pass

def escape_dict(*args, **kwargs): # real signature unknown
    """
    escape_sequence(d, dict) -- escape any special characters in
    dictionary d using mapping dict to provide quoting functions for each type.
    Returns a dictionary of escaped items.
    """
    pass

def escape_sequence(seq, dict): # real signature unknown; restored from __doc__
    """
    escape_sequence(seq, dict) -- escape any special characters in sequence
    seq using mapping dict to provide quoting functions for each type.
    Returns a tuple of escaped items.
    """
    pass

def escape_string(s): # real signature unknown; restored from __doc__
    """
    escape_string(s) -- quote any SQL-interpreted characters in string s.
    
    Use connection.escape_string(s), if you use it at all.
    _mysql.escape_string(s) cannot handle character sets. You are
    probably better off using connection.escape(o) instead, since
    it will escape entire sequences as well as strings.
    """
    pass

def get_client_info(): # real signature unknown; restored from __doc__
    """
    get_client_info() -- Returns a string that represents
    the client library version.
    """
    pass

def server_end(*args, **kwargs): # real signature unknown
    """
    Shut down embedded server. If not using an embedded server, this
    does nothing.
    """
    pass

def server_init(*args, **kwargs): # real signature unknown
    """
    Initialize embedded server. If this client is not linked against
    the embedded server library, this function does nothing.
    
    args -- sequence of command-line arguments
    groups -- sequence of groups to use in defaults files
    """
    pass

def string_literal(obj): # real signature unknown; restored from __doc__
    """
    string_literal(obj) -- converts object obj into a SQL string literal.
    This means, any special SQL characters are escaped, and it is enclosed
    within single quotes. In other words, it performs:
    
    "'%s'" % escape_string(str(obj))
    
    Use connection.string_literal(obj), if you use it at all.
    _mysql.string_literal(obj) cannot handle character sets.
    """
    pass

def thread_safe(*args, **kwargs): # real signature unknown
    """ Indicates whether the client is compiled as thread-safe. """
    pass

# classes

class connection(object):
    """
    Returns a MYSQL connection object. Exclusive use of
    keyword parameters strongly recommended. Consult the
    MySQL C API documentation for more details.
    
    host
      string, host to connect
    
    user
      string, user to connect as
    
    passwd
      string, password to use
    
    db
      string, database to use
    
    port
      integer, TCP/IP port to connect to
    
    unix_socket
      string, location of unix_socket (UNIX-ish only)
    
    conv
      mapping, maps MySQL FIELD_TYPE.* to Python functions which
      convert a string to the appropriate Python type
    
    connect_timeout
      number of seconds to wait before the connection
      attempt fails.
    
    compress
      if set, gzip compression is enabled
    
    named_pipe
      if set, connect to server via named pipe (Windows only)
    
    init_command
      command which is run once the connection is created
    
    read_default_file
      see the MySQL documentation for mysql_options()
    
    read_default_group
      see the MySQL documentation for mysql_options()
    
    client_flag
      client flags from MySQLdb.constants.CLIENT
    
    load_infile
      int, non-zero enables LOAD LOCAL INFILE, zero disables
    """
    def affected_rows(self, *args, **kwargs): # real signature unknown
        """
        Return number of rows affected by the last query.
        Non-standard. Use Cursor.rowcount.
        """
        pass

    def autocommit(self, *args, **kwargs): # real signature unknown
        """ Set the autocommit mode. True values enable; False value disable. """
        pass

    def change_user(self, *args, **kwargs): # real signature unknown
        """
        Changes the user and causes the database specified by db to
        become the default (current) database on the connection
        specified by mysql. In subsequent queries, this database is
        the default for table references that do not include an
        explicit database specifier.
        
        This function was introduced in MySQL Version 3.23.3.
        
        Fails unless the connected user can be authenticated or if he
        doesn't have permission to use the database. In this case the
        user and database are not changed.
        
        The db parameter may be set to None if you don't want to have
        a default database.
        """
        pass

    def character_set_name(self, *args, **kwargs): # real signature unknown
        """
        Returns the default character set for the current connection.
        Non-standard.
        """
        pass

    def close(self, *args, **kwargs): # real signature unknown
        """ Close the connection. No further activity possible. """
        pass

    def commit(self, *args, **kwargs): # real signature unknown
        """ Commits the current transaction """
        pass

    def dump_debug_info(self, *args, **kwargs): # real signature unknown
        """
        Instructs the server to write some debug information to the
        log. The connected user must have the process privilege for
        this to work. Non-standard.
        """
        pass

    def errno(self, *args, **kwargs): # real signature unknown
        """
        Returns the error code for the most recently invoked API function
        that can succeed or fail. A return value of zero means that no error
        occurred.
        """
        pass

    def error(self, *args, **kwargs): # real signature unknown
        """
        Returns the error message for the most recently invoked API function
        that can succeed or fail. An empty string () is returned if no error
        occurred.
        """
        pass

    def escape(self, obj, dict): # real signature unknown; restored from __doc__
        """
        escape(obj, dict) -- escape any special characters in object obj
        using mapping dict to provide quoting functions for each type.
        Returns a SQL literal string.
        """
        pass

    def escape_string(self, s): # real signature unknown; restored from __doc__
        """
        escape_string(s) -- quote any SQL-interpreted characters in string s.
        
        Use connection.escape_string(s), if you use it at all.
        _mysql.escape_string(s) cannot handle character sets. You are
        probably better off using connection.escape(o) instead, since
        it will escape entire sequences as well as strings.
        """
        pass

    def field_count(self, *args, **kwargs): # real signature unknown
        """
        Returns the number of columns for the most recent query on the
        connection. Non-standard. Will probably give you bogus results
        on most cursor classes. Use Cursor.rowcount.
        """
        pass

    def fileno(self, *args, **kwargs): # real signature unknown
        """ Return underlaying fd for connection """
        pass

    def get_autocommit(self, *args, **kwargs): # real signature unknown
        """ Get the autocommit mode. True when enable; False when disable. """
        pass

    def get_character_set_info(self, *args, **kwargs): # real signature unknown
        """
        Returns a dict with information about the current character set:
        
        collation
            collation name
        name
            character set name
        comment
            comment or descriptive name
        dir
            character set directory
        mbminlen
            min. length for multibyte string
        mbmaxlen
            max. length for multibyte string
        
        Not all keys may be present, particularly dir.
        
        Non-standard.
        """
        pass

    def get_host_info(self, *args, **kwargs): # real signature unknown
        """
        Returns a string that represents the MySQL client library
        version. Non-standard.
        """
        pass

    def get_proto_info(self, *args, **kwargs): # real signature unknown
        """
        Returns an unsigned integer representing the protocol version
        used by the current connection. Non-standard.
        """
        pass

    def get_server_info(self, *args, **kwargs): # real signature unknown
        """
        Returns a string that represents the server version number.
        Non-standard.
        """
        pass

    def info(self, *args, **kwargs): # real signature unknown
        """
        Retrieves a string providing information about the most
        recently executed query. Non-standard. Use messages or
        Cursor.messages.
        """
        pass

    def insert_id(self, *args, **kwargs): # real signature unknown
        """
        Returns the ID generated for an AUTO_INCREMENT column by the previous
        query. Use this function after you have performed an INSERT query into a
        table that contains an AUTO_INCREMENT field.
        
        Note that this returns 0 if the previous query does not
        generate an AUTO_INCREMENT value. If you need to save the value for
        later, be sure to call this immediately after the query
        that generates the value.
        
        The ID is updated after INSERT and UPDATE statements that generate
        an AUTO_INCREMENT value or that set a column value to
        LAST_INSERT_ID(expr). See section 6.3.5.2 Miscellaneous Functions
        in the MySQL documentation.
        
        Also note that the value of the SQL LAST_INSERT_ID() function always
        contains the most recently generated AUTO_INCREMENT value, and is not
        reset between queries because the value of that function is maintained
        in the server.
        """
        pass

    def kill(self, *args, **kwargs): # real signature unknown
        """
        Asks the server to kill the thread specified by pid.
        Non-standard.
        """
        pass

    def next_result(self): # real signature unknown; restored from __doc__
        """
        If more query results exist, next_result() reads the next query
        results and returns the status back to application.
        
        After calling next_result() the state of the connection is as if
        you had called query() for the next query. This means that you can
        now call store_result(), warning_count(), affected_rows()
        , and so forth. 
        
        Returns 0 if there are more results; -1 if there are no more results
        
        Non-standard.
        """
        pass

    def ping(self): # real signature unknown; restored from __doc__
        """
        Checks whether or not the connection to the server is
        working. If it has gone down, an automatic reconnection is
        attempted.
        
        This function can be used by clients that remain idle for a
        long while, to check whether or not the server has closed the
        connection and reconnect if necessary.
        
        New in 1.2.2: Accepts an optional reconnect parameter. If True,
        then the client will attempt reconnection. Note that this setting
        is persistent. By default, this is on in MySQL<5.0.3, and off
        thereafter.
        
        Non-standard. You should assume that ping() performs an
        implicit rollback; use only when starting a new transaction.
        You have been warned.
        """
        pass

    def query(self, *args, **kwargs): # real signature unknown
        """
        Execute a query. store_result() or use_result() will get the
        result set, if any. Non-standard. Use cursor() to create a cursor,
        then cursor.execute().
        """
        pass

    def read_query_result(self, *args, **kwargs): # real signature unknown
        """ Read result of query sent by send_query(). """
        pass

    def rollback(self, *args, **kwargs): # real signature unknown
        """ Rolls backs the current transaction """
        pass

    def select_db(self, *args, **kwargs): # real signature unknown
        """
        Causes the database specified by db to become the default
        (current) database on the connection specified by mysql. In subsequent
        queries, this database is the default for table references that do not
        include an explicit database specifier.
        
        Fails unless the connected user can be authenticated as having
        permission to use the database.
        
        Non-standard.
        """
        pass

    def send_query(self, *args, **kwargs): # real signature unknown
        """
        Send a query. Same to query() except not wait response.
        
        Use read_query_result() before calling store_result() or use_result()
        """
        pass

    def set_character_set(self, *args, **kwargs): # real signature unknown
        """
        Sets the default character set for the current connection.
        Non-standard.
        """
        pass

    def set_server_option(self, option): # real signature unknown; restored from __doc__
        """
        set_server_option(option) -- Enables or disables an option
        for the connection.
        
        Non-standard.
        """
        pass

    def shutdown(self, *args, **kwargs): # real signature unknown
        """
        Asks the database server to shut down. The connected user must
        have shutdown privileges. Non-standard.
        """
        pass

    def sqlstate(self, *args, **kwargs): # real signature unknown
        """
        Returns a string containing the SQLSTATE error code
        for the last error. The error code consists of five characters.
        '00000' means "no error." The values are specified by ANSI SQL
        and ODBC. For a list of possible values, see section 23
        Error Handling in MySQL in the MySQL Manual.
        
        Note that not all MySQL errors are yet mapped to SQLSTATE's.
        The value 'HY000' (general error) is used for unmapped errors.
        
        Non-standard.
        """
        pass

    def stat(self, *args, **kwargs): # real signature unknown
        """
        Returns a character string containing information similar to
        that provided by the mysqladmin status command. This includes
        uptime in seconds and the number of running threads,
        questions, reloads, and open tables. Non-standard.
        """
        pass

    def store_result(self, results_stored_in_the_client): # real signature unknown; restored from __doc__
        """
        Returns a result object acquired by mysql_store_result
        (results stored in the client). If no results are available,
        None is returned. Non-standard.
        """
        pass

    def string_literal(self, obj): # real signature unknown; restored from __doc__
        """
        string_literal(obj) -- converts object obj into a SQL string literal.
        This means, any special SQL characters are escaped, and it is enclosed
        within single quotes. In other words, it performs:
        
        "'%s'" % escape_string(str(obj))
        
        Use connection.string_literal(obj), if you use it at all.
        _mysql.string_literal(obj) cannot handle character sets.
        """
        pass

    def thread_id(self, *args, **kwargs): # real signature unknown
        """
        Returns the thread ID of the current connection. This value
        can be used as an argument to kill() to kill the thread.
        
        If the connection is lost and you reconnect with ping(), the
        thread ID will change. This means you should not get the
        thread ID and store it for later. You should get it when you
        need it.
        
        Non-standard.
        """
        pass

    def use_result(self, results_stored_in_the_server): # real signature unknown; restored from __doc__
        """
        Returns a result object acquired by mysql_use_result
        (results stored in the server). If no results are available,
        None is returned. Non-standard.
        """
        pass

    def warning_count(self, *args, **kwargs): # real signature unknown
        """
        Returns the number of warnings generated during execution
        of the previous SQL statement.
        
        Non-standard.
        """
        pass

    def __delattr__(self, *args, **kwargs): # real signature unknown
        """ Implement delattr(self, name). """
        pass

    def __getattribute__(self, *args, **kwargs): # real signature unknown
        """ Return getattr(self, name). """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    def __setattr__(self, *args, **kwargs): # real signature unknown
        """ Implement setattr(self, name, value). """
        pass

    client_flag = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Client flags; refer to MySQLdb.constants.CLIENT"""

    converter = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Type conversion mapping"""

    open = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """True if connection is open"""

    port = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """TCP/IP port of the server connection"""

    server_capabilities = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Capabilities of server; consult MySQLdb.constants.CLIENT"""



class MySQLError(Exception):
    """ Exception related to operation with MySQL. """
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



class Error(___mysql_exceptions.MySQLError):
    """
    Exception that is the base class of all other error exceptions
        (not Warning).
    """
    def __init__(self, *args, **kwargs): # real signature unknown
        pass


class DatabaseError(___mysql_exceptions.Error):
    """
    Exception raised for errors that are related to the
        database.
    """
    def __init__(self, *args, **kwargs): # real signature unknown
        pass


class DataError(___mysql_exceptions.DatabaseError):
    """
    Exception raised for errors that are due to problems with the
        processed data like division by zero, numeric value out of range,
        etc.
    """
    def __init__(self, *args, **kwargs): # real signature unknown
        pass


class IntegrityError(___mysql_exceptions.DatabaseError):
    """
    Exception raised when the relational integrity of the database
        is affected, e.g. a foreign key check fails, duplicate key,
        etc.
    """
    def __init__(self, *args, **kwargs): # real signature unknown
        pass


class InterfaceError(___mysql_exceptions.Error):
    """
    Exception raised for errors that are related to the database
        interface rather than the database itself.
    """
    def __init__(self, *args, **kwargs): # real signature unknown
        pass


class InternalError(___mysql_exceptions.DatabaseError):
    """
    Exception raised when the database encounters an internal
        error, e.g. the cursor is not valid anymore, the transaction is
        out of sync, etc.
    """
    def __init__(self, *args, **kwargs): # real signature unknown
        pass


class NotSupportedError(___mysql_exceptions.DatabaseError):
    """
    Exception raised in case a method or database API was used
        which is not supported by the database, e.g. requesting a
        .rollback() on a connection that does not support transaction or
        has transactions turned off.
    """
    def __init__(self, *args, **kwargs): # real signature unknown
        pass


class OperationalError(___mysql_exceptions.DatabaseError):
    """
    Exception raised for errors that are related to the database's
        operation and not necessarily under the control of the programmer,
        e.g. an unexpected disconnect occurs, the data source name is not
        found, a transaction could not be processed, a memory allocation
        error occurred during processing, etc.
    """
    def __init__(self, *args, **kwargs): # real signature unknown
        pass


class ProgrammingError(___mysql_exceptions.DatabaseError):
    """
    Exception raised for programming errors, e.g. table not found
        or already exists, syntax error in the SQL statement, wrong number
        of parameters specified, etc.
    """
    def __init__(self, *args, **kwargs): # real signature unknown
        pass


class result(object):
    """
    result(connection, use=0, converter={}) -- Result set from a query.
    
    Creating instances of this class directly is an excellent way to
    shoot yourself in the foot. If using _mysql.connection directly,
    use connection.store_result() or connection.use_result() instead.
    If using MySQLdb.Connection, this is done by the cursor class.
    Just forget you ever saw this. Forget... FOR-GET...
    """
    def data_seek(self, n): # real signature unknown; restored from __doc__
        """ data_seek(n) -- seek to row n of result set """
        pass

    def describe(self, *args, **kwargs): # real signature unknown
        """
        Returns the sequence of 7-tuples required by the DB-API for
        the Cursor.description attribute.
        """
        pass

    def fetch_row(self, maxrows=None, how=None): # real signature unknown; restored from __doc__
        """
        fetch_row([maxrows, how]) -- Fetches up to maxrows as a tuple.
        The rows are formatted according to how:
        
            0 -- tuples (default)
            1 -- dictionaries, key=column or table.column if duplicated
            2 -- dictionaries, key=table.column
        """
        pass

    def field_flags(self, *args, **kwargs): # real signature unknown
        """ Returns a tuple of field flags, one for each column in the result. """
        pass

    def num_fields(self, *args, **kwargs): # real signature unknown
        """ Returns the number of fields (column) in the result. """
        pass

    def num_rows(self, *args, **kwargs): # real signature unknown
        """
        Returns the number of rows in the result set. Note that if
        use=1, this will not return a valid value until the entire result
        set has been read.
        """
        pass

    def row_seek(self, n): # real signature unknown; restored from __doc__
        """ row_seek(n) -- seek by offset n rows of result set """
        pass

    def row_tell(self): # real signature unknown; restored from __doc__
        """ row_tell() -- return the current row number of the result set. """
        pass

    def __delattr__(self, *args, **kwargs): # real signature unknown
        """ Implement delattr(self, name). """
        pass

    def __getattribute__(self, *args, **kwargs): # real signature unknown
        """ Return getattr(self, name). """
        pass

    def __init__(self, connection, use=0, converter={}): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    def __setattr__(self, *args, **kwargs): # real signature unknown
        """ Implement setattr(self, name, value). """
        pass

    converter = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Type conversion mapping"""

    has_next = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Has next result"""



class Warning(Warning, ___mysql_exceptions.MySQLError):
    """
    Exception raised for important warnings like data truncations
        while inserting, etc.
    """
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



# variables with complex values

version_info = (
    1,
    3,
    12,
    'final',
    0,
)

__loader__ = None # (!) real value is ''

__spec__ = None # (!) real value is ''

