import sys
import pycurl
import time


class ContentCallback:
        def __init__(self):
                self.contents = ''

        def content_callback(self, buf):
                self.contents = self.contents + buf

def get(urlhere):
	t = ContentCallback()
	curlObj = pycurl.Curl()
	curlObj.setopt(curlObj.URL, urlhere)
	curlObj.setopt(curlObj.WRITEFUNCTION, t.content_callback)
	curlObj.perform()
	curlObj.close()
	return t.contents


def get_avail(page):
    quote_start = page.find('<span class="num-backers mr1">')#ensure start and end are same as yours (view page source)
    quote_end = page.find('</span>', quote_start)
    quote=page[(quote_start+len('<span class="num-backers mr1">')):quote_end]
	#print "|"+quote+"|"#Uncomment to check exact phrase
    return quote

x=y=skip=printed=0
while(x==0):
	page=get('https://www.kickstarter.com/projects/597507018/pebble-time-awesome-smartwatch-no-compromises')#change to project url
	num_avail=get_avail(page)
	print printed,num_avail
	printed=printed+1
	if(num_avail!='\n10,000 backers\n'):#change phrase here if necessary (see line 27)
			print y,'BUY BUY BUY\n\n'
			y=y+1
			skip=1
	else:
		skip=y=0#if there is space, fetch page without delay
	if skip==0:
		time.sleep(10) # delays for 10 seconds, feel free to change
