import whois
from datetime import datetime
from sys import argv,exit
from message import Message
domain = argv[1]
try:
    w = whois.whois(domain)
except whois.parser.PywhoisError as e:
    print(e)
    exit(1)

print(w)

timedelta = w.expiration_date -  datetime.now()
days_to_expire = timedelta.days
print("days_to_expire",days_to_expire)
if days_to_expire< 30:
    level=Message.WARN
else:
    level=Message.INFO
m = Message("whois", level, f'Domain registration expires in {days_to_expire} days')
print(m)
print(dict(m))