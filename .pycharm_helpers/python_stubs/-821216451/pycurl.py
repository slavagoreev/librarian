# encoding: utf-8
# module pycurl
# from /usr/lib/python3/dist-packages/pycurl.cpython-35m-x86_64-linux-gnu.so
# by generator 1.145
"""
This module implements an interface to the cURL library.

Types:

Curl() -> New object.  Create a new curl object.
CurlMulti() -> New object.  Create a new curl multi object.
CurlShare() -> New object.  Create a new curl share object.

Functions:

global_init(option) -> None.  Initialize curl environment.
global_cleanup() -> None.  Cleanup curl environment.
version_info() -> tuple.  Return version information.
"""
# no imports

# Variables with simple values

ACCEPTTIMEOUT_MS = 212

ACCEPT_ENCODING = 10102

ADDRESS_SCOPE = 171

APPCONNECT_TIME = 3145761

APPEND = 50

AUTOREFERER = 58

BUFFERSIZE = 98

CAINFO = 10065
CAPATH = 10097

CLOSESOCKETFUNCTION = 20208

COMPILE_DATE = 'Mar 10 2016 17:26:29'

COMPILE_LIBCURL_VERSION_NUM = 470784

COMPILE_PY_VERSION_HEX = 50659824

CONDITION_UNMET = 2097187

CONNECTTIMEOUT = 78

CONNECTTIMEOUT_MS = 156

CONNECT_ONLY = 141
CONNECT_TIME = 3145733

CONTENT_LENGTH_DOWNLOAD = 3145743
CONTENT_LENGTH_UPLOAD = 3145744

CONTENT_TYPE = 1048594

COOKIE = 10022
COOKIEFILE = 10031
COOKIEJAR = 10082
COOKIELIST = 10135
COOKIESESSION = 96
COPYPOSTFIELDS = 10165

CRLF = 27
CRLFILE = 10169

CSELECT_ERR = 4
CSELECT_IN = 1
CSELECT_OUT = 2

CURL_HTTP_VERSION_1_0 = 1
CURL_HTTP_VERSION_1_1 = 2

CURL_HTTP_VERSION_2 = 3
CURL_HTTP_VERSION_2TLS = 4

CURL_HTTP_VERSION_2_0 = 3

CURL_HTTP_VERSION_LAST = 5
CURL_HTTP_VERSION_NONE = 0

CUSTOMREQUEST = 10036

DEBUGFUNCTION = 20094

DEFAULT_PROTOCOL = 10238

DIRLISTONLY = 48

DNS_CACHE_TIMEOUT = 92

DNS_SERVERS = 10211

DNS_USE_GLOBAL_CACHE = 91

EFFECTIVE_URL = 1048577

EGDSOCKET = 10077

ENCODING = 10102

EXPECT_100_TIMEOUT_MS = 227

E_ABORTED_BY_CALLBACK = 42

E_AGAIN = 81

E_ALREADY_COMPLETE = 99999

E_BAD_CALLING_ORDER = 44

E_BAD_CONTENT_ENCODING = 61

E_BAD_DOWNLOAD_RESUME = 36

E_BAD_FUNCTION_ARGUMENT = 43

E_BAD_PASSWORD_ENTERED = 46

E_CALL_MULTI_PERFORM = -1

E_CHUNK_FAILED = 88

E_CONV_FAILED = 75
E_CONV_REQD = 76

E_COULDNT_CONNECT = 7

E_COULDNT_RESOLVE_HOST = 6
E_COULDNT_RESOLVE_PROXY = 5

E_FAILED_INIT = 2

E_FILESIZE_EXCEEDED = 63

E_FILE_COULDNT_READ_FILE = 37

E_FTP_ACCEPT_FAILED = 10
E_FTP_ACCEPT_TIMEOUT = 12

E_FTP_ACCESS_DENIED = 9

E_FTP_BAD_DOWNLOAD_RESUME = 36

E_FTP_BAD_FILE_LIST = 87

E_FTP_CANT_GET_HOST = 15

E_FTP_CANT_RECONNECT = 16

E_FTP_COULDNT_GET_SIZE = 32

E_FTP_COULDNT_RETR_FILE = 19

E_FTP_COULDNT_SET_ASCII = 29
E_FTP_COULDNT_SET_BINARY = 17
E_FTP_COULDNT_SET_TYPE = 17

E_FTP_COULDNT_STOR_FILE = 25

E_FTP_COULDNT_USE_REST = 31

E_FTP_PARTIAL_FILE = 18

E_FTP_PORT_FAILED = 30

E_FTP_PRET_FAILED = 84

E_FTP_QUOTE_ERROR = 21

E_FTP_SSL_FAILED = 64

E_FTP_USER_PASSWORD_INCORRECT = 10

E_FTP_WEIRD_227_FORMAT = 14

E_FTP_WEIRD_PASS_REPLY = 11

E_FTP_WEIRD_PASV_REPLY = 13

E_FTP_WEIRD_SERVER_REPLY = 8

E_FTP_WEIRD_USER_REPLY = 12

E_FTP_WRITE_ERROR = 20

E_FUNCTION_NOT_FOUND = 41

E_GOT_NOTHING = 52

E_HTTP2 = 16

E_HTTP_NOT_FOUND = 22

E_HTTP_PORT_FAILED = 45

E_HTTP_POST_ERROR = 34

E_HTTP_RANGE_ERROR = 33

E_HTTP_RETURNED_ERROR = 22

E_INTERFACE_FAILED = 45

E_LDAP_CANNOT_BIND = 38

E_LDAP_INVALID_URL = 62

E_LDAP_SEARCH_FAILED = 39

E_LIBRARY_NOT_FOUND = 40

E_LOGIN_DENIED = 67

E_MALFORMAT_USER = 24

E_MULTI_ADDED_ALREADY = 7

E_MULTI_BAD_EASY_HANDLE = 2

E_MULTI_BAD_HANDLE = 1
E_MULTI_BAD_SOCKET = 5

E_MULTI_CALL_MULTI_PERFORM = -1
E_MULTI_CALL_MULTI_SOCKET = -1

E_MULTI_INTERNAL_ERROR = 4

E_MULTI_OK = 0

E_MULTI_OUT_OF_MEMORY = 3

E_MULTI_UNKNOWN_OPTION = 6

E_NOT_BUILT_IN = 4

E_NO_CONNECTION_AVAILABLE = 89

E_OK = 0

E_OPERATION_TIMEDOUT = 28
E_OPERATION_TIMEOUTED = 28

E_OUT_OF_MEMORY = 27

E_PARTIAL_FILE = 18

E_PEER_FAILED_VERIFICATION = 51

E_QUOTE_ERROR = 21

E_RANGE_ERROR = 33

E_READ_ERROR = 26

E_RECV_ERROR = 56

E_REMOTE_ACCESS_DENIED = 9

E_REMOTE_DISK_FULL = 70

E_REMOTE_FILE_EXISTS = 73

E_REMOTE_FILE_NOT_FOUND = 78

E_RTSP_CSEQ_ERROR = 85

E_RTSP_SESSION_ERROR = 86

E_SEND_ERROR = 55

E_SEND_FAIL_REWIND = 65

E_SHARE_IN_USE = 57

E_SSH = 79

E_SSL_CACERT = 60

E_SSL_CACERT_BADFILE = 77

E_SSL_CERTPROBLEM = 58
E_SSL_CIPHER = 59

E_SSL_CONNECT_ERROR = 35

E_SSL_CRL_BADFILE = 82

E_SSL_ENGINE_INITFAILED = 66
E_SSL_ENGINE_NOTFOUND = 53
E_SSL_ENGINE_SETFAILED = 54

E_SSL_INVALIDCERTSTATUS = 91

E_SSL_ISSUER_ERROR = 83

E_SSL_PEER_CERTIFICATE = 51

E_SSL_PINNEDPUBKEYNOTMATCH = 90

E_SSL_SHUTDOWN_FAILED = 80

E_TELNET_OPTION_SYNTAX = 49

E_TFTP_DISKFULL = 70
E_TFTP_EXISTS = 73
E_TFTP_ILLEGAL = 71
E_TFTP_NOSUCHUSER = 74
E_TFTP_NOTFOUND = 68
E_TFTP_PERM = 69
E_TFTP_UNKNOWNID = 72

E_TOO_MANY_REDIRECTS = 47

E_UNKNOWN_OPTION = 48

E_UNKNOWN_TELNET_OPTION = 48

E_UNSUPPORTED_PROTOCOL = 1

E_UPLOAD_FAILED = 25

E_URL_MALFORMAT = 3

E_URL_MALFORMAT_USER = 4

E_USE_SSL_FAILED = 64

E_WRITE_ERROR = 23

FAILONERROR = 45

FILE = 10001

FOLLOWLOCATION = 52

FORBID_REUSE = 75

FORM_BUFFER = 11
FORM_BUFFERPTR = 12
FORM_CONTENTS = 4
FORM_CONTENTTYPE = 14
FORM_FILE = 10
FORM_FILENAME = 16

FRESH_CONNECT = 74

FTPAPPEND = 50

FTPAUTH_DEFAULT = 0
FTPAUTH_SSL = 1
FTPAUTH_TLS = 2

FTPLISTONLY = 48

FTPMETHOD_DEFAULT = 0
FTPMETHOD_MULTICWD = 1
FTPMETHOD_NOCWD = 2
FTPMETHOD_SINGLECWD = 3

FTPPORT = 10017
FTPSSLAUTH = 129

FTPSSL_ALL = 3
FTPSSL_CONTROL = 2
FTPSSL_NONE = 0
FTPSSL_TRY = 1

FTP_ACCOUNT = 10134

FTP_ALTERNATIVE_TO_USER = 10147

FTP_CREATE_MISSING_DIRS = 110

FTP_ENTRY_PATH = 1048606

FTP_FILEMETHOD = 138

FTP_RESPONSE_TIMEOUT = 112

FTP_SKIP_PASV_IP = 137

FTP_SSL = 119

FTP_SSL_CCC = 154

FTP_USE_EPRT = 106
FTP_USE_EPSV = 85
FTP_USE_PRET = 188

GLOBAL_ACK_EINTR = 4

GLOBAL_ALL = 3
GLOBAL_DEFAULT = 3
GLOBAL_NOTHING = 0
GLOBAL_SSL = 1
GLOBAL_WIN32 = 2

GSSAPI_DELEGATION = 210

GSSAPI_DELEGATION_FLAG = 2
GSSAPI_DELEGATION_NONE = 0

GSSAPI_DELEGATION_POLICY_FLAG = 1

HEADER = 42
HEADERFUNCTION = 20079
HEADEROPT = 229

HEADER_SEPARATE = 1
HEADER_SIZE = 2097163
HEADER_UNIFIED = 0

HTTP200ALIASES = 10104
HTTPAUTH = 107

HTTPAUTH_ANY = -17
HTTPAUTH_ANYSAFE = -18
HTTPAUTH_AVAIL = 2097175
HTTPAUTH_BASIC = 1
HTTPAUTH_DIGEST = 2

HTTPAUTH_DIGEST_IE = 16

HTTPAUTH_GSSNEGOTIATE = 4
HTTPAUTH_NEGOTIATE = 4
HTTPAUTH_NONE = 0
HTTPAUTH_NTLM = 8

HTTPAUTH_NTLM_WB = 32

HTTPAUTH_ONLY = 2147483648

HTTPGET = 80
HTTPHEADER = 10023
HTTPPOST = 10024
HTTPPROXYTUNNEL = 61

HTTP_CODE = 2097154
HTTP_CONNECTCODE = 2097174

HTTP_CONTENT_DECODING = 158

HTTP_TRANSFER_DECODING = 157

HTTP_VERSION = 84

IGNORE_CONTENT_LENGTH = 136

INFILE = 10009
INFILESIZE = 30115

INFILESIZE_LARGE = 30115

INFOTYPE_DATA_IN = 3
INFOTYPE_DATA_OUT = 4

INFOTYPE_HEADER_IN = 1
INFOTYPE_HEADER_OUT = 2

INFOTYPE_SSL_DATA_IN = 5
INFOTYPE_SSL_DATA_OUT = 6

INFOTYPE_TEXT = 0

INFO_CERTINFO = 4194338
INFO_COOKIELIST = 4194332
INFO_FILETIME = 2097166

INFO_RTSP_CLIENT_CSEQ = 2097189

INFO_RTSP_CSEQ_RECV = 2097191

INFO_RTSP_SERVER_CSEQ = 2097190

INFO_RTSP_SESSION_ID = 1048612

INTERFACE = 10062

IOCMD_NOP = 0
IOCMD_RESTARTREAD = 1

IOCTLFUNCTION = 20130

IOE_FAILRESTART = 2
IOE_OK = 0
IOE_UNKNOWNCMD = 1

IPRESOLVE = 113

IPRESOLVE_V4 = 1
IPRESOLVE_V6 = 2
IPRESOLVE_WHATEVER = 0

ISSUERCERT = 10170

KEYPASSWD = 10026

KHMATCH_MISMATCH = 1
KHMATCH_MISSING = 2
KHMATCH_OK = 0

KHSTAT_DEFER = 3
KHSTAT_FINE = 1

KHSTAT_FINE_ADD_TO_FILE = 0

KHSTAT_REJECT = 2

KHTYPE_DSS = 3
KHTYPE_RSA = 2
KHTYPE_RSA1 = 1
KHTYPE_UNKNOWN = 0

KRB4LEVEL = 10063
KRBLEVEL = 10063

LASTSOCKET = 2097181

LOCALPORT = 139
LOCALPORTRANGE = 140

LOCAL_IP = 1048617
LOCAL_PORT = 2097194

LOCK_DATA_COOKIE = 2
LOCK_DATA_DNS = 3

LOCK_DATA_SSL_SESSION = 4

LOGIN_OPTIONS = 10224

LOW_SPEED_LIMIT = 19
LOW_SPEED_TIME = 20

MAIL_AUTH = 10217
MAIL_FROM = 10186
MAIL_RCPT = 10187

MAXCONNECTS = 71
MAXFILESIZE = 30117

MAXFILESIZE_LARGE = 30117

MAXREDIRS = 68

MAX_RECV_SPEED_LARGE = 30146

MAX_SEND_SPEED_LARGE = 30145

M_CHUNK_LENGTH_PENALTY_SIZE = 30010

M_CONTENT_LENGTH_PENALTY_SIZE = 30009

M_MAXCONNECTS = 6

M_MAX_HOST_CONNECTIONS = 7

M_MAX_PIPELINE_LENGTH = 8

M_MAX_TOTAL_CONNECTIONS = 13

M_PIPELINING = 3

M_PIPELINING_SERVER_BL = 10012

M_PIPELINING_SITE_BL = 10011

M_SOCKETFUNCTION = 20001
M_TIMERFUNCTION = 20004

NAMELOOKUP_TIME = 3145732

NETRC = 51

NETRC_FILE = 10118
NETRC_IGNORED = 0
NETRC_OPTIONAL = 1
NETRC_REQUIRED = 2

NEW_DIRECTORY_PERMS = 160

NEW_FILE_PERMS = 159

NOBODY = 44
NOPROGRESS = 43
NOPROXY = 10177
NOSIGNAL = 99

NUM_CONNECTS = 2097178

OPENSOCKETFUNCTION = 20163

OPT_CERTINFO = 172
OPT_FILETIME = 69

OS_ERRNO = 2097177

PASSWORD = 10174

PATH_AS_IS = 234

PAUSE_ALL = 5
PAUSE_CONT = 0
PAUSE_RECV = 1
PAUSE_SEND = 4

PINNEDPUBLICKEY = 10230
PIPEWAIT = 237

PIPE_HTTP1 = 1
PIPE_MULTIPLEX = 2
PIPE_NOTHING = 0

POLL_IN = 1
POLL_INOUT = 3
POLL_NONE = 0
POLL_OUT = 2
POLL_REMOVE = 4

PORT = 3
POST = 47
POST301 = 161
POSTFIELDS = 10015
POSTFIELDSIZE = 30120

POSTFIELDSIZE_LARGE = 30120

POSTQUOTE = 10039
POSTREDIR = 161

PREQUOTE = 10093

PRETRANSFER_TIME = 3145734

PRIMARY_IP = 1048608
PRIMARY_PORT = 2097192

PROGRESSFUNCTION = 20056
PROTOCOLS = 181

PROTO_ALL = -1
PROTO_DICT = 512
PROTO_FILE = 1024
PROTO_FTP = 4
PROTO_FTPS = 8
PROTO_GOPHER = 33554432
PROTO_HTTP = 1
PROTO_HTTPS = 2
PROTO_IMAP = 4096
PROTO_IMAPS = 8192
PROTO_LDAP = 128
PROTO_LDAPS = 256
PROTO_POP3 = 16384
PROTO_POP3S = 32768
PROTO_RTMP = 524288
PROTO_RTMPE = 2097152
PROTO_RTMPS = 8388608
PROTO_RTMPT = 1048576
PROTO_RTMPTE = 4194304
PROTO_RTMPTS = 16777216
PROTO_RTSP = 262144
PROTO_SCP = 16
PROTO_SFTP = 32
PROTO_SMB = 67108864
PROTO_SMBS = 134217728
PROTO_SMTP = 65536
PROTO_SMTPS = 131072
PROTO_TELNET = 64
PROTO_TFTP = 2048

PROXY = 10004
PROXYAUTH = 111

PROXYAUTH_AVAIL = 2097176

PROXYHEADER = 10228
PROXYPASSWORD = 10176
PROXYPORT = 59
PROXYTYPE = 101

PROXYTYPE_HTTP = 0

PROXYTYPE_HTTP_1_0 = 1

PROXYTYPE_SOCKS4 = 4
PROXYTYPE_SOCKS4A = 6
PROXYTYPE_SOCKS5 = 5

PROXYTYPE_SOCKS5_HOSTNAME = 7

PROXYUSERNAME = 10175
PROXYUSERPWD = 10006

PROXY_SERVICE_NAME = 10235

PROXY_TRANSFER_MODE = 166

PUT = 54

QUOTE = 10028

RANDOM_FILE = 10076

RANGE = 10007

READDATA = 10009
READFUNCTION = 20012

READFUNC_ABORT = 268435456
READFUNC_PAUSE = 268435457

REDIRECT_COUNT = 2097172
REDIRECT_TIME = 3145747
REDIRECT_URL = 1048607

REDIR_POST_301 = 1
REDIR_POST_302 = 2
REDIR_POST_303 = 4
REDIR_POST_ALL = 7

REDIR_PROTOCOLS = 182

REFERER = 10016

REQUEST_SIZE = 2097164

RESOLVE = 10203

RESPONSE_CODE = 2097154

RESUME_FROM = 30116

RESUME_FROM_LARGE = 30116

SASL_IR = 218

SEEKFUNCTION = 20167

SEEKFUNC_CANTSEEK = 2
SEEKFUNC_FAIL = 1
SEEKFUNC_OK = 0

SERVICE_NAME = 10236

SHARE = 10100
SH_SHARE = 1
SH_UNSHARE = 2

SIZE_DOWNLOAD = 3145736
SIZE_UPLOAD = 3145735

SOCKET_TIMEOUT = -1

SOCKOPTFUNCTION = 20148

SOCKOPT_ALREADY_CONNECTED = 2

SOCKOPT_ERROR = 1
SOCKOPT_OK = 0

SOCKS5_GSSAPI_NEC = 180
SOCKS5_GSSAPI_SERVICE = 10179

SOCKTYPE_ACCEPT = 1
SOCKTYPE_IPCXN = 0

SPEED_DOWNLOAD = 3145737
SPEED_UPLOAD = 3145738

SSH_AUTH_ANY = -1
SSH_AUTH_DEFAULT = -1
SSH_AUTH_HOST = 4
SSH_AUTH_KEYBOARD = 8
SSH_AUTH_NONE = 0
SSH_AUTH_PASSWORD = 2
SSH_AUTH_PUBLICKEY = 1
SSH_AUTH_TYPES = 151

SSH_HOST_PUBLIC_KEY_MD5 = 10162

SSH_KEYFUNCTION = 20184
SSH_KNOWNHOSTS = 10183

SSH_PRIVATE_KEYFILE = 10153

SSH_PUBLIC_KEYFILE = 10152

SSLCERT = 10025
SSLCERTPASSWD = 10026
SSLCERTTYPE = 10086
SSLENGINE = 10089

SSLENGINE_DEFAULT = 90

SSLKEY = 10087
SSLKEYPASSWD = 10026
SSLKEYTYPE = 10088

SSLOPT_ALLOW_BEAST = 1

SSLOPT_NO_REVOKE = 2

SSLVERSION = 32

SSLVERSION_DEFAULT = 0
SSLVERSION_SSLv2 = 2
SSLVERSION_SSLv3 = 3
SSLVERSION_TLSv1 = 1

SSLVERSION_TLSv1_0 = 4
SSLVERSION_TLSv1_1 = 5
SSLVERSION_TLSv1_2 = 6

SSL_CIPHER_LIST = 10083

SSL_ENABLE_ALPN = 226
SSL_ENABLE_NPN = 225

SSL_ENGINES = 4194331
SSL_FALSESTART = 233
SSL_OPTIONS = 216

SSL_SESSIONID_CACHE = 150

SSL_VERIFYHOST = 81
SSL_VERIFYPEER = 64
SSL_VERIFYRESULT = 2097165
SSL_VERIFYSTATUS = 232

STARTTRANSFER_TIME = 3145745

STDERR = 10037

TCP_KEEPALIVE = 213
TCP_KEEPIDLE = 214
TCP_KEEPINTVL = 215
TCP_NODELAY = 121

TELNETOPTIONS = 10070

TFTP_BLKSIZE = 178

TIMECONDITION = 33

TIMECONDITION_IFMODSINCE = 1
TIMECONDITION_IFUNMODSINCE = 2
TIMECONDITION_LASTMOD = 3
TIMECONDITION_NONE = 0

TIMEOUT = 13

TIMEOUT_MS = 155

TIMEVALUE = 34

TLSAUTH_PASSWORD = 10205
TLSAUTH_TYPE = 10206
TLSAUTH_USERNAME = 10204

TOTAL_TIME = 3145731

TRANSFERTEXT = 53

TRANSFER_ENCODING = 207

UNIX_SOCKET_PATH = 10231

UNRESTRICTED_AUTH = 105

UPLOAD = 46

URL = 10002

USERAGENT = 10018
USERNAME = 10173
USERPWD = 10005

USESSL_ALL = 3
USESSL_CONTROL = 2
USESSL_NONE = 0
USESSL_TRY = 1

USE_SSL = 119

VERBOSE = 41

version = 'PycURL/7.43.0 libcurl/7.47.0 GnuTLS/3.4.10 zlib/1.2.8 libidn/1.32 librtmp/2.3'

VERSION_ASYNCHDNS = 128
VERSION_CONV = 4096
VERSION_CURLDEBUG = 8192
VERSION_DEBUG = 64
VERSION_GSSAPI = 131072
VERSION_GSSNEGOTIATE = 32
VERSION_HTTP2 = 65536
VERSION_IDN = 1024
VERSION_IPV6 = 1
VERSION_KERBEROS4 = 2
VERSION_KERBEROS5 = 262144
VERSION_LARGEFILE = 512
VERSION_LIBZ = 8
VERSION_NTLM = 16

VERSION_NTLM_WB = 32768

VERSION_PSL = 1048576
VERSION_SPNEGO = 256
VERSION_SSL = 4
VERSION_SSPI = 2048

VERSION_TLSAUTH_SRP = 16384

VERSION_UNIX_SOCKETS = 524288

WILDCARDMATCH = 197

WRITEDATA = 10001
WRITEFUNCTION = 20011

WRITEFUNC_PAUSE = 268435457

WRITEHEADER = 10029

XFERINFOFUNCTION = 20219

XOAUTH2_BEARER = 10220

# functions

def global_cleanup(): # real signature unknown; restored from __doc__
    """
    global_cleanup() -> None
    
    Cleanup curl environment.
    
    Corresponds to `curl_global_cleanup`_ in libcurl.
    
    .. _curl_global_cleanup: http://curl.haxx.se/libcurl/c/curl_global_cleanup.html
    """
    pass

def global_init(option): # real signature unknown; restored from __doc__
    """
    global_init(option) -> None
    
    Initialize curl environment.
    
    *option* is one of the constants pycurl.GLOBAL_SSL, pycurl.GLOBAL_WIN32,
    pycurl.GLOBAL_ALL, pycurl.GLOBAL_NOTHING, pycurl.GLOBAL_DEFAULT.
    
    Corresponds to `curl_global_init`_ in libcurl.
    
    .. _curl_global_init: http://curl.haxx.se/libcurl/c/curl_global_init.html
    """
    pass

def version_info(): # real signature unknown; restored from __doc__
    """
    version_info() -> tuple
    
    Returns a 12-tuple with the version info.
    
    Corresponds to `curl_version_info`_ in libcurl. Returns a tuple of
    information which is similar to the ``curl_version_info_data`` struct
    returned by ``curl_version_info()`` in libcurl.
    
    Example usage::
    
        >>> import pycurl
        >>> pycurl.version_info()
        (3, '7.33.0', 467200, 'amd64-portbld-freebsd9.1', 33436, 'OpenSSL/0.9.8x',
        0, '1.2.7', ('dict', 'file', 'ftp', 'ftps', 'gopher', 'http', 'https',
        'imap', 'imaps', 'pop3', 'pop3s', 'rtsp', 'smtp', 'smtps', 'telnet',
        'tftp'), None, 0, None)
    
    .. _curl_version_info: http://curl.haxx.se/libcurl/c/curl_version_info.html
    """
    return ()

# classes

class Curl(object):
    """
    Curl() -> New Curl object
    
    Creates a new :ref:`curlobject` which corresponds to a
    ``CURL`` handle in libcurl. Curl objects automatically set
    CURLOPT_VERBOSE to 0, CURLOPT_NOPROGRESS to 1, provide a default
    CURLOPT_USERAGENT and setup CURLOPT_ERRORBUFFER to point to a
    private error buffer.
    
    Implicitly calls :py:func:`pycurl.global_init` if the latter has not yet been called.
    """
    def close(self): # real signature unknown; restored from __doc__
        """
        close() -> None
        
        Close handle and end curl session.
        
        Corresponds to `curl_easy_cleanup`_ in libcurl. This method is
        automatically called by pycurl when a Curl object no longer has any
        references to it, but can also be called explicitly.
        
        .. _curl_easy_cleanup:
            http://curl.haxx.se/libcurl/c/curl_easy_cleanup.html
        """
        pass

    def errstr(self): # real signature unknown; restored from __doc__
        """
        errstr() -> string
        
        Return the internal libcurl error buffer of this handle as a string.
        
        Return value is a ``str`` instance on all Python versions.
        """
        return ""

    def getinfo(self, info): # real signature unknown; restored from __doc__
        """
        getinfo(info) -> Result
        
        Extract and return information from a curl session.
        
        Corresponds to `curl_easy_getinfo`_ in libcurl, where *option* is
        the same as the ``CURLINFO_*`` constants in libcurl, except that the
        ``CURLINFO_`` prefix has been removed. (See below for exceptions.)
        *Result* contains an integer, float or string, depending on which
        option is given. The ``getinfo`` method should not be called unless
        ``perform`` has been called and finished.
        
        In order to distinguish between similarly-named CURLOPT and CURLINFO
        constants, some have ``OPT_`` and ``INFO_`` prefixes. These are
        ``INFO_FILETIME``, ``OPT_FILETIME``, ``INFO_COOKIELIST`` (but ``setopt`` uses
        ``COOKIELIST``!), ``INFO_CERTINFO``, and ``OPT_CERTINFO``.
        
        The value returned by ``getinfo(INFO_CERTINFO)`` is a list with one element
        per certificate in the chain, starting with the leaf; each element is a
        sequence of *(key, value)* tuples.
        
        Example usage::
        
            import pycurl
            c = pycurl.Curl()
            c.setopt(pycurl.URL, "http://sf.net")
            c.setopt(pycurl.FOLLOWLOCATION, 1)
            c.perform()
            print c.getinfo(pycurl.HTTP_CODE), c.getinfo(pycurl.EFFECTIVE_URL)
            ...
            --> 200 "http://sourceforge.net/"
        
        
        Raises pycurl.error exception upon failure.
        
        .. _curl_easy_getinfo:
            http://curl.haxx.se/libcurl/c/curl_easy_getinfo.html
        """
        pass

    def pause(self, bitmask): # real signature unknown; restored from __doc__
        """
        pause(bitmask) -> None
        
        Pause or unpause a curl handle. Bitmask should be a value such as
        PAUSE_RECV or PAUSE_CONT.
        
        Corresponds to `curl_easy_pause`_ in libcurl. The argument should be
        derived from the ``PAUSE_RECV``, ``PAUSE_SEND``, ``PAUSE_ALL`` and
        ``PAUSE_CONT`` constants.
        
        Raises pycurl.error exception upon failure.
        
        .. _curl_easy_pause: http://curl.haxx.se/libcurl/c/curl_easy_pause.html
        """
        pass

    def perform(self): # real signature unknown; restored from __doc__
        """
        perform() -> None
        
        Perform a file transfer.
        
        Corresponds to `curl_easy_perform`_ in libcurl.
        
        Raises pycurl.error exception upon failure.
        
        .. _curl_easy_perform:
            http://curl.haxx.se/libcurl/c/curl_easy_perform.html
        """
        pass

    def reset(self): # real signature unknown; restored from __doc__
        """
        reset() -> None
        
        Reset all options set on curl handle to default values, but preserves
        live connections, session ID cache, DNS cache, cookies, and shares.
        
        Corresponds to `curl_easy_reset`_ in libcurl.
        
        .. _curl_easy_reset: http://curl.haxx.se/libcurl/c/curl_easy_reset.html
        """
        pass

    def setopt(self, option, value): # real signature unknown; restored from __doc__
        """
        setopt(option, value) -> None
        
        Set curl session option. Corresponds to `curl_easy_setopt`_ in libcurl.
        
        *option* specifies which option to set. PycURL defines constants
        corresponding to ``CURLOPT_*`` constants in libcurl, except that
        the ``CURLOPT_`` prefix is removed. For example, ``CURLOPT_URL`` is
        exposed in PycURL as ``pycurl.URL``. For convenience, ``CURLOPT_*``
        constants are also exposed on the Curl objects themselves::
        
            import pycurl
            c = pycurl.Curl()
            c.setopt(pycurl.URL, "http://www.python.org/")
            # Same as:
            c.setopt(c.URL, "http://www.python.org/")
        
        In order to distinguish between similarly-named CURLOPT and CURLINFO
        constants, some have CURLOPT constants have ``OPT_`` prefixes.
        These are ``OPT_FILETIME`` and ``OPT_CERTINFO``.
        As an exception to the exception, ``COOKIELIST`` does not have an ``OPT_``
        prefix but the corresponding CURLINFO option is ``INFO_COOKIELIST``.
        
        *value* specifies the value to set the option to. Different options accept
        values of different types:
        
        - Options specified by `curl_easy_setopt`_ as accepting ``1`` or an
          integer value accept Python integers, long integers (on Python 2.x) and
          booleans::
        
            c.setopt(pycurl.FOLLOWLOCATION, True)
            c.setopt(pycurl.FOLLOWLOCATION, 1)
            # Python 2.x only:
            c.setopt(pycurl.FOLLOWLOCATION, 1L)
        
        - Options specified as accepting strings by ``curl_easy_setopt`` accept
          byte strings (``str`` on Python 2, ``bytes`` on Python 3) and
          Unicode strings with ASCII code points only.
          For more information, please refer to :ref:`unicode`. Example::
        
            c.setopt(pycurl.URL, "http://www.python.org/")
            c.setopt(pycurl.URL, u"http://www.python.org/")
            # Python 3.x only:
            c.setopt(pycurl.URL, b"http://www.python.org/")
        
        - ``HTTP200ALIASES``, ``HTTPHEADER``, ``POSTQUOTE``, ``PREQUOTE``,
          ``PROXYHEADER`` and
          ``QUOTE`` accept a list or tuple of strings. The same rules apply to these
          strings as do to string option values. Example::
        
            c.setopt(pycurl.HTTPHEADER, ["Accept:"])
            c.setopt(pycurl.HTTPHEADER, ("Accept:",))
        
        - ``READDATA`` accepts a file object or any Python object which has
          a ``read`` method. On Python 2, a file object will be passed directly
          to libcurl and may result in greater transfer efficiency, unless
          PycURL has been compiled with ``AVOID_STDIO`` option.
          On Python 3 and on Python 2 when the value is not a true file object,
          ``READDATA`` is emulated in PycURL via ``READFUNCTION``.
          The file should generally be opened in binary mode. Example::
        
            f = open('file.txt', 'rb')
            c.setopt(c.READDATA, f)
        
        - ``WRITEDATA`` and ``WRITEHEADER`` accept a file object or any Python
          object which has a ``write`` method. On Python 2, a file object will
          be passed directly to libcurl and may result in greater transfer efficiency,
          unless PycURL has been compiled with ``AVOID_STDIO`` option.
          On Python 3 and on Python 2 when the value is not a true file object,
          ``WRITEDATA`` is emulated in PycURL via ``WRITEFUNCTION``.
          The file should generally be opened in binary mode. Example::
        
            f = open('/dev/null', 'wb')
            c.setopt(c.WRITEDATA, f)
        
        - ``*FUNCTION`` options accept a function. Supported callbacks are documented
          in :ref:`callbacks`. Example::
        
            # Python 2
            import StringIO
            b = StringIO.StringIO()
            c.setopt(pycurl.WRITEFUNCTION, b.write)
        
        - ``SHARE`` option accepts a :ref:`curlshareobject`.
        
        It is possible to set integer options - and only them - that PycURL does
        not know about by using the numeric value of the option constant directly.
        For example, ``pycurl.VERBOSE`` has the value 42, and may be set as follows::
        
            c.setopt(42, 1)
        
        *setopt* can reset some options to their default value, performing the job of
        :py:meth:`pycurl.Curl.unsetopt`, if ``None`` is passed
        for the option value. The following two calls are equivalent::
        
            c.setopt(c.URL, None)
            c.unsetopt(c.URL)
        
        Raises TypeError when the option value is not of a type accepted by the
        respective option, and pycurl.error exception when libcurl rejects the
        option or its value.
        
        .. _curl_easy_setopt: http://curl.haxx.se/libcurl/c/curl_easy_setopt.html
        """
        pass

    def setopt_string(self, option, value): # real signature unknown; restored from __doc__
        """
        setopt_string(option, value) -> None
        
        Set curl session option to a string value.
        
        This method allows setting string options that are not officially supported
        by PycURL, for example because they did not exist when the version of PycURL
        being used was released.
        :py:meth:`pycurl.Curl.setopt` should be used for setting options that
        PycURL knows about.
        
        **Warning:** No checking is performed that *option* does, in fact,
        expect a string value. Using this method incorrectly can crash the program
        and may lead to a security vulnerability.
        Furthermore, it is on the application to ensure that the *value* object
        does not get garbage collected while libcurl is using it.
        libcurl copies most string options but not all; one option whose value
        is not copied by libcurl is `CURLOPT_POSTFIELDS`_.
        
        *option* would generally need to be given as an integer literal rather than
        a symbolic constant.
        
        *value* can be a binary string or a Unicode string using ASCII code points,
        same as with string options given to PycURL elsewhere.
        
        Example setting URL via ``setopt_string``::
        
            import pycurl
            c = pycurl.Curl()
            c.setopt_string(10002, "http://www.python.org/")
        
        .. _CURLOPT_POSTFIELDS: http://curl.haxx.se/libcurl/c/CURLOPT_POSTFIELDS.html
        """
        pass

    def unsetopt(self, option): # real signature unknown; restored from __doc__
        """
        unsetopt(option) -> None
        
        Reset curl session option to its default value.
        
        Only some curl options may be reset via this method.
        
        libcurl does not provide a general way to reset a single option to its default value;
        :py:meth:`pycurl.Curl.reset` resets all options to their default values,
        otherwise :py:meth:`pycurl.Curl.setopt` must be called with whatever value
        is the default. For convenience, PycURL provides this unsetopt method
        to reset some of the options to their default values.
        
        Raises pycurl.error exception on failure.
        
        ``c.unsetopt(option)`` is equivalent to ``c.setopt(option, None)``.
        """
        pass

    def __delattr__(self, *args, **kwargs): # real signature unknown
        """ Implement delattr(self, name). """
        pass

    def __getattribute__(self, *args, **kwargs): # real signature unknown
        """ Return getattr(self, name). """
        pass

    def __getstate__(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __setattr__(self, *args, **kwargs): # real signature unknown
        """ Implement setattr(self, name, value). """
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        pass


class CurlMulti(object):
    """
    CurlMulti() -> New CurlMulti object
    
    Creates a new :ref:`curlmultiobject` which corresponds to
    a ``CURLM`` handle in libcurl.
    """
    def add_handle(self, Curl_object): # real signature unknown; restored from __doc__
        """
        add_handle(Curl object) -> None
        
        Corresponds to `curl_multi_add_handle`_ in libcurl. This method adds an
        existing and valid Curl object to the CurlMulti object.
        
        IMPORTANT NOTE: add_handle does not implicitly add a Python reference to the
        Curl object (and thus does not increase the reference count on the Curl
        object).
        
        .. _curl_multi_add_handle:
            http://curl.haxx.se/libcurl/c/curl_multi_add_handle.html
        """
        pass

    def assign(self, sockfd, p_object): # real signature unknown; restored from __doc__
        """
        assign(sockfd, object) -> None
        
        Creates an association in the multi handle between the given socket and
        a private object in the application.
        Corresponds to `curl_multi_assign`_ in libcurl.
        
        .. _curl_multi_assign: http://curl.haxx.se/libcurl/c/curl_multi_assign.html
        """
        pass

    def close(self): # real signature unknown; restored from __doc__
        """
        close() -> None
        
        Corresponds to `curl_multi_cleanup`_ in libcurl. This method is
        automatically called by pycurl when a CurlMulti object no longer has any
        references to it, but can also be called explicitly.
        
        .. _curl_multi_cleanup:
            http://curl.haxx.se/libcurl/c/curl_multi_cleanup.html
        """
        pass

    def fdset(self): # real signature unknown; restored from __doc__
        """
        fdset() -> tuple of lists with active file descriptors, readable, writeable, exceptions
        
        Returns a tuple of three lists that can be passed to the select.select() method.
        
        Corresponds to `curl_multi_fdset`_ in libcurl. This method extracts the
        file descriptor information from a CurlMulti object. The returned lists can
        be used with the ``select`` module to poll for events.
        
        Example usage::
        
            import pycurl
            c = pycurl.Curl()
            c.setopt(pycurl.URL, "http://curl.haxx.se")
            m = pycurl.CurlMulti()
            m.add_handle(c)
            while 1:
                ret, num_handles = m.perform()
                if ret != pycurl.E_CALL_MULTI_PERFORM: break
            while num_handles:
                apply(select.select, m.fdset() + (1,))
                while 1:
                    ret, num_handles = m.perform()
                    if ret != pycurl.E_CALL_MULTI_PERFORM: break
        
        .. _curl_multi_fdset:
            http://curl.haxx.se/libcurl/c/curl_multi_fdset.html
        """
        return ()

    def info_read(self, max_objects=None): # real signature unknown; restored from __doc__
        """
        info_read([max_objects]) -> tuple(number of queued messages, a list of successful objects, a list of failed objects)
        
        Returns a tuple (number of queued handles, [curl objects]).
        
        Corresponds to the `curl_multi_info_read`_ function in libcurl. This
        method extracts at most *max* messages from the multi stack and returns them
        in two lists. The first list contains the handles which completed
        successfully and the second list contains a tuple *(curl object, curl error
        number, curl error message)* for each failed curl object. The number of
        queued messages after this method has been called is also returned.
        
        .. _curl_multi_info_read:
            http://curl.haxx.se/libcurl/c/curl_multi_info_read.html
        """
        return ()

    def perform(self): # real signature unknown; restored from __doc__
        """
        perform() -> tuple of status and the number of active Curl objects
        
        Corresponds to `curl_multi_perform`_ in libcurl.
        
        .. _curl_multi_perform:
            http://curl.haxx.se/libcurl/c/curl_multi_perform.html
        """
        return ()

    def remove_handle(self, Curl_object): # real signature unknown; restored from __doc__
        """
        remove_handle(Curl object) -> None
        
        Corresponds to `curl_multi_remove_handle`_ in libcurl. This method
        removes an existing and valid Curl object from the CurlMulti object.
        
        IMPORTANT NOTE: remove_handle does not implicitly remove a Python reference
        from the Curl object (and thus does not decrease the reference count on the
        Curl object).
        
        .. _curl_multi_remove_handle:
            http://curl.haxx.se/libcurl/c/curl_multi_remove_handle.html
        """
        pass

    def select(self, timeout=None): # real signature unknown; restored from __doc__
        """
        select([timeout]) -> number of ready file descriptors or -1 on timeout
        
        Returns result from doing a select() on the curl multi file descriptor
        with the given timeout.
        
        This is a convenience function which simplifies the combined use of
        ``fdset()`` and the ``select`` module.
        
        Example usage::
        
            import pycurl
            c = pycurl.Curl()
            c.setopt(pycurl.URL, "http://curl.haxx.se")
            m = pycurl.CurlMulti()
            m.add_handle(c)
            while 1:
                ret, num_handles = m.perform()
                if ret != pycurl.E_CALL_MULTI_PERFORM: break
            while num_handles:
                ret = m.select(1.0)
                if ret == -1:  continue
                while 1:
                    ret, num_handles = m.perform()
                    if ret != pycurl.E_CALL_MULTI_PERFORM: break
        """
        return 0

    def setopt(self, option, value): # real signature unknown; restored from __doc__
        """
        setopt(option, value) -> None
        
        Set curl multi option. Corresponds to `curl_multi_setopt`_ in libcurl.
        
        *option* specifies which option to set. PycURL defines constants
        corresponding to ``CURLMOPT_*`` constants in libcurl, except that
        the ``CURLMOPT_`` prefix is replaced with ``M_`` prefix.
        For example, ``CURLMOPT_PIPELINING`` is
        exposed in PycURL as ``pycurl.M_PIPELINING``. For convenience, ``CURLMOPT_*``
        constants are also exposed on CurlMulti objects::
        
            import pycurl
            m = pycurl.CurlMulti()
            m.setopt(pycurl.M_PIPELINING, 1)
            # Same as:
            m.setopt(m.M_PIPELINING, 1)
        
        *value* specifies the value to set the option to. Different options accept
        values of different types:
        
        - Options specified by `curl_multi_setopt`_ as accepting ``1`` or an
          integer value accept Python integers, long integers (on Python 2.x) and
          booleans::
        
            m.setopt(pycurl.M_PIPELINING, True)
            m.setopt(pycurl.M_PIPELINING, 1)
            # Python 2.x only:
            m.setopt(pycurl.M_PIPELINING, 1L)
        
        - ``*FUNCTION`` options accept a function. Supported callbacks are
          ``CURLMOPT_SOCKETFUNCTION`` AND ``CURLMOPT_TIMERFUNCTION``. Please refer to
          the PycURL test suite for examples on using the callbacks.
        
        Raises TypeError when the option value is not of a type accepted by the
        respective option, and pycurl.error exception when libcurl rejects the
        option or its value.
        
        .. _curl_multi_setopt: http://curl.haxx.se/libcurl/c/curl_multi_setopt.html
        """
        pass

    def socket_action(self, sockfd, ev_bitmask): # real signature unknown; restored from __doc__
        """
        socket_action(sockfd, ev_bitmask) -> tuple
        
        Returns result from doing a socket_action() on the curl multi file descriptor
        with the given timeout.
        Corresponds to `curl_multi_socket_action`_ in libcurl.
        
        .. _curl_multi_socket_action: http://curl.haxx.se/libcurl/c/curl_multi_socket_action.html
        """
        return ()

    def socket_all(self): # real signature unknown; restored from __doc__
        """
        socket_all() -> Tuple.
        
        Returns result from doing a socket_all() on the curl multi file descriptor
        with the given timeout.
        """
        pass

    def timeout(self): # real signature unknown; restored from __doc__
        """
        timeout() -> int
        
        Returns how long to wait for action before proceeding.
        Corresponds to `curl_multi_timeout`_ in libcurl.
        
        .. _curl_multi_timeout: http://curl.haxx.se/libcurl/c/curl_multi_timeout.html
        """
        return 0

    def __delattr__(self, *args, **kwargs): # real signature unknown
        """ Implement delattr(self, name). """
        pass

    def __getattribute__(self, *args, **kwargs): # real signature unknown
        """ Return getattr(self, name). """
        pass

    def __getstate__(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __setattr__(self, *args, **kwargs): # real signature unknown
        """ Implement setattr(self, name, value). """
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        pass


class CurlShare(object):
    """
    CurlShare() -> New CurlShare object
    
    Creates a new :ref:`curlshareobject` which corresponds to a
    ``CURLSH`` handle in libcurl. CurlShare objects is what you pass as an
    argument to the SHARE option on :ref:`Curl objects <curlobject>`.
    """
    def close(self): # real signature unknown; restored from __doc__
        """
        close() -> None
        
        Close shared handle.
        
        Corresponds to `curl_share_cleanup`_ in libcurl. This method is
        automatically called by pycurl when a CurlShare object no longer has
        any references to it, but can also be called explicitly.
        
        .. _curl_share_cleanup:
            http://curl.haxx.se/libcurl/c/curl_share_cleanup.html
        """
        pass

    def setopt(self, option, value): # real signature unknown; restored from __doc__
        """
        setopt(option, value) -> None
        
        Set curl share option.
        
        Corresponds to `curl_share_setopt`_ in libcurl, where *option* is
        specified with the ``CURLSHOPT_*`` constants in libcurl, except that the
        ``CURLSHOPT_`` prefix has been changed to ``SH_``. Currently, *value* must be
        either ``LOCK_DATA_COOKIE`` or ``LOCK_DATA_DNS``.
        
        Example usage::
        
            import pycurl
            curl = pycurl.Curl()
            s = pycurl.CurlShare()
            s.setopt(pycurl.SH_SHARE, pycurl.LOCK_DATA_COOKIE)
            s.setopt(pycurl.SH_SHARE, pycurl.LOCK_DATA_DNS)
            curl.setopt(pycurl.URL, 'http://curl.haxx.se')
            curl.setopt(pycurl.SHARE, s)
            curl.perform()
            curl.close()
        
        Raises pycurl.error exception upon failure.
        
        .. _curl_share_setopt:
            http://curl.haxx.se/libcurl/c/curl_share_setopt.html
        """
        pass

    def __delattr__(self, *args, **kwargs): # real signature unknown
        """ Implement delattr(self, name). """
        pass

    def __getattribute__(self, *args, **kwargs): # real signature unknown
        """ Return getattr(self, name). """
        pass

    def __getstate__(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __setattr__(self, *args, **kwargs): # real signature unknown
        """ Implement setattr(self, name, value). """
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        pass


class CurlSockAddr(tuple):
    """ CurlSockAddr(family, socktype, protocol, addr) """
    def _asdict(self): # reliably restored by inspect
        """ Return a new OrderedDict which maps field names to their values. """
        pass

    @classmethod
    def _make(cls, *args, **kwargs): # real signature unknown
        """ Make a new CurlSockAddr object from a sequence or iterable """
        pass

    def _replace(_self, **kwds): # reliably restored by inspect
        """ Return a new CurlSockAddr object replacing specified fields with new values """
        pass

    def __getnewargs__(self): # reliably restored by inspect
        """ Return self as a plain tuple.  Used by copy and pickle. """
        pass

    def __init__(self, family, socktype, protocol, addr): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(_cls, family, socktype, protocol, addr): # reliably restored by inspect
        """ Create new instance of CurlSockAddr(family, socktype, protocol, addr) """
        pass

    def __repr__(self): # reliably restored by inspect
        """ Return a nicely formatted representation string """
        pass

    addr = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Alias for field number 3"""

    family = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Alias for field number 0"""

    protocol = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Alias for field number 2"""

    socktype = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Alias for field number 1"""


    _fields = (
        'family',
        'socktype',
        'protocol',
        'addr',
    )
    _source = "from builtins import property as _property, tuple as _tuple\nfrom operator import itemgetter as _itemgetter\nfrom collections import OrderedDict\n\nclass CurlSockAddr(tuple):\n    'CurlSockAddr(family, socktype, protocol, addr)'\n\n    __slots__ = ()\n\n    _fields = ('family', 'socktype', 'protocol', 'addr')\n\n    def __new__(_cls, family, socktype, protocol, addr):\n        'Create new instance of CurlSockAddr(family, socktype, protocol, addr)'\n        return _tuple.__new__(_cls, (family, socktype, protocol, addr))\n\n    @classmethod\n    def _make(cls, iterable, new=tuple.__new__, len=len):\n        'Make a new CurlSockAddr object from a sequence or iterable'\n        result = new(cls, iterable)\n        if len(result) != 4:\n            raise TypeError('Expected 4 arguments, got %d' % len(result))\n        return result\n\n    def _replace(_self, **kwds):\n        'Return a new CurlSockAddr object replacing specified fields with new values'\n        result = _self._make(map(kwds.pop, ('family', 'socktype', 'protocol', 'addr'), _self))\n        if kwds:\n            raise ValueError('Got unexpected field names: %r' % list(kwds))\n        return result\n\n    def __repr__(self):\n        'Return a nicely formatted representation string'\n        return self.__class__.__name__ + '(family=%r, socktype=%r, protocol=%r, addr=%r)' % self\n\n    def _asdict(self):\n        'Return a new OrderedDict which maps field names to their values.'\n        return OrderedDict(zip(self._fields, self))\n\n    def __getnewargs__(self):\n        'Return self as a plain tuple.  Used by copy and pickle.'\n        return tuple(self)\n\n    family = _property(_itemgetter(0), doc='Alias for field number 0')\n\n    socktype = _property(_itemgetter(1), doc='Alias for field number 1')\n\n    protocol = _property(_itemgetter(2), doc='Alias for field number 2')\n\n    addr = _property(_itemgetter(3), doc='Alias for field number 3')\n\n"
    __slots__ = ()


class error(Exception):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



class KhKey(tuple):
    """ KhKey(key, keytype) """
    def _asdict(self): # reliably restored by inspect
        """ Return a new OrderedDict which maps field names to their values. """
        pass

    @classmethod
    def _make(cls, *args, **kwargs): # real signature unknown
        """ Make a new KhKey object from a sequence or iterable """
        pass

    def _replace(_self, **kwds): # reliably restored by inspect
        """ Return a new KhKey object replacing specified fields with new values """
        pass

    def __getnewargs__(self): # reliably restored by inspect
        """ Return self as a plain tuple.  Used by copy and pickle. """
        pass

    def __init__(self, key, keytype): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(_cls, key, keytype): # reliably restored by inspect
        """ Create new instance of KhKey(key, keytype) """
        pass

    def __repr__(self): # reliably restored by inspect
        """ Return a nicely formatted representation string """
        pass

    key = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Alias for field number 0"""

    keytype = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Alias for field number 1"""


    _fields = (
        'key',
        'keytype',
    )
    _source = "from builtins import property as _property, tuple as _tuple\nfrom operator import itemgetter as _itemgetter\nfrom collections import OrderedDict\n\nclass KhKey(tuple):\n    'KhKey(key, keytype)'\n\n    __slots__ = ()\n\n    _fields = ('key', 'keytype')\n\n    def __new__(_cls, key, keytype):\n        'Create new instance of KhKey(key, keytype)'\n        return _tuple.__new__(_cls, (key, keytype))\n\n    @classmethod\n    def _make(cls, iterable, new=tuple.__new__, len=len):\n        'Make a new KhKey object from a sequence or iterable'\n        result = new(cls, iterable)\n        if len(result) != 2:\n            raise TypeError('Expected 2 arguments, got %d' % len(result))\n        return result\n\n    def _replace(_self, **kwds):\n        'Return a new KhKey object replacing specified fields with new values'\n        result = _self._make(map(kwds.pop, ('key', 'keytype'), _self))\n        if kwds:\n            raise ValueError('Got unexpected field names: %r' % list(kwds))\n        return result\n\n    def __repr__(self):\n        'Return a nicely formatted representation string'\n        return self.__class__.__name__ + '(key=%r, keytype=%r)' % self\n\n    def _asdict(self):\n        'Return a new OrderedDict which maps field names to their values.'\n        return OrderedDict(zip(self._fields, self))\n\n    def __getnewargs__(self):\n        'Return self as a plain tuple.  Used by copy and pickle.'\n        return tuple(self)\n\n    key = _property(_itemgetter(0), doc='Alias for field number 0')\n\n    keytype = _property(_itemgetter(1), doc='Alias for field number 1')\n\n"
    __slots__ = ()


# variables with complex values

__loader__ = None # (!) real value is ''

__spec__ = None # (!) real value is ''

