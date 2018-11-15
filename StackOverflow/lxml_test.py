import urllib2
from lxml import etree
import urllib2
from lxml import etree


#import requests

def wgetUrl(target):
    try:
        req = urllib2.Request(target)
        req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3 Gecko/2008092417 Firefox/3.0.3')
        response = urllib2.urlopen(req)
        outtxt = response.read()
        response.close()
    except:
        return ''

    return outtxt


# analogous function xpath(...).extract() for lxml etree nodes
def extract_text(elem):        
    if elem is None:
        print None
    else:
        return ''.join(i for i in elem.itertext())

url = 'http://www.forexfactory.com/calendar.php?day='
date = 'dec1.2011'

data = wgetUrl(url + date)
node = etree.HTML(data)


for row in node.findall(r'.//div[@id="flexBox_flex_calendar_mainCal"]//table/tr[contains(@class,"calendar")]'):
    print "================" 
    print extract_text(row.find(r'.//td[@class="time"]'))
    print extract_text(row.find(r'.//td[@class="currency"]'))
    td = row.find(r'.//td[@class="impact"]/span')
    if td is not None and 'title' in td.attrib:
        print td.attrib['title']
    print extract_text(row.find(r'.//td[@class="event"]/span'))
    print extract_text(row.find(r'.//td[@class="actual"]'))
    print extract_text(row.find(r'.//td[@class="forecast"]'))
    print extract_text(row.find(r'.//td[@class="previous"]'))
    print "================"
