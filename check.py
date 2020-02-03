
from sys import argv
#from message import Message
import modules.whois
domain = argv[1]

ms = modules.whois.runcheck(domain)
print(ms)