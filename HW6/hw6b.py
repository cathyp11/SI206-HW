import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter URL: ')
count = int(input('Enter count: '))
position = int(input('Enter position: '))

# Retrieve all of the anchor tags
print("Retrieving: ", url)
for i in range(count):
	html = urllib.request.urlopen(url, context=ctx).read()
	soup = BeautifulSoup(html, 'html.parser')
	tags = soup.find_all('a')
	counter = 0
	pos = position - 1
	print("Retrieving: ", tags[pos].get('href'))
	url = tags[pos].get('href')
	i += 1
