import urllib.request, urllib.error, urllib.parse
import base64

URL = 'http://localhost/basic.html' 
passwd = '550charpass50charpass50charpass50charpass50charpass0charpass'
#passwd = 'senthil'
request = urllib.request.Request(URL)
#base64.MAXBINSIZE=1000000
base64string = base64.b64encode('%s:%s' %('senthil',passwd))[:-1]
#base64string = base64.encodestring('%s:%s' %('senthil',passwd))[:-1]
request.add_header('WWW-Authenticate', 'Basic realm=Realm')
request.add_header("Authorization","Basic %s" % base64string)
obj = urllib.request.urlopen(request)
print(obj.read())
