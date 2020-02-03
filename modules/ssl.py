import socket
import ssl
from datetime import datetime
from urllib.parse import urlparse
from modules.message import Message

def ssl_expiry_datetime(hostname: str):
    ssl_date_fmt = r'%b %d %H:%M:%S %Y %Z'

    context = ssl.create_default_context()
    conn = context.wrap_socket(
        socket.socket(socket.AF_INET),
        server_hostname=hostname,
    )
    conn.settimeout(10.0)

    conn.connect((hostname, 443))
    ssl_info = conn.getpeercert()
    #print(ssl_info)
    # parse the string from the certificate into a Python datetime object
    return datetime.strptime(ssl_info['notAfter'], ssl_date_fmt)

def ssl_valid_time_remaining(hostname: str):
    """Get the number of days left in a cert's lifetime."""
    expires = ssl_expiry_datetime(hostname)
    
    return expires - datetime.utcnow()

def runcheck(domain):
    hostname=urlparse(domain).netloc
    td = ssl_valid_time_remaining(hostname)
    days_to_expire = td.days
    if days_to_expire< 14:
        level=Message.WARN
    elif days_to_expire< 30:
        level=Message.NOTICE
    else:
        level=Message.INFO
    return [Message("ssl", level, f'HTTPS certificate expires in {days_to_expire} days')]