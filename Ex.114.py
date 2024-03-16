import urllib
import urllib.request

try:
    site = urllib.request.urlopen('https://www.pudim.com.br/')
except urllib.error.URLError:
    print('o site não está acessível.')
else:
    print('Está funcionando')
    print(site.read())