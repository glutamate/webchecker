import whois
from datetime import datetime

from modules.message import Message

def runcheck(domain):
    try:
        w = whois.whois(domain)
    except whois.parser.PywhoisError as e:
        return [Message("whois", Message.CHECKERROR, str(e))]

    print(w)

    timedelta = w.expiration_date -  datetime.now()
    days_to_expire = timedelta.days

    if days_to_expire< 30:
        level=Message.WARN
    else:
        level=Message.INFO
    return [Message("whois", level, f'Domain registration expires in {days_to_expire} days')]