import whois
from datetime import datetime
from sys import argv,exit

domain = argv[1]
try:
    w = whois.whois(domain)
except whois.parser.PywhoisError as e:
    print(e)
    exit(1)

print(w)
