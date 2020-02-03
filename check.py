
from sys import argv
import modules.whois
import modules.ssl

domain = argv[1]

ms = modules.whois.runcheck(domain) + modules.ssl.runcheck(domain)
#ms = modules.ssl.runcheck(domain)
print(ms)