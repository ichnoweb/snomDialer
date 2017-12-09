import urllib2
import sys

numberToDial = sys.argv[1]

# Required if you need to prefix your external numbers with 0
zeroPrefixed = 0
try:
    zeroPrefixed = numberToDial.index('00')
except Exception:
    zeroPrefixed = 0

# Up to three numbers are used for internal connections
if len(numberToDial) > 3 and zeroPrefixed != 0:
    numberToDial = '0' + numberToDial

hostname = ''
username = ''
password = ''

manager = urllib2.HTTPPasswordMgrWithDefaultRealm()
manager.add_password(None, hostname, username, password)
handler = urllib2.HTTPBasicAuthHandler(manager)

opener = urllib2.build_opener(handler)
urllib2.install_opener(opener)

headers = {'Accept': 'text/html'}
req = urllib2.Request(hostname + '/command.htm?number=' + numberToDial, None, headers)

print "Dialing: " + numberToDial

res = urllib2.urlopen(req)
