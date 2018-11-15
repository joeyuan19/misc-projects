import urllib2
import bs4
import re

def scrape_crimes(html,write_headers):
    soup =  bs4.BeautifulSoup(html)
    table = soup.find_all('table',class_=('cbResultSetTable',))
    if len(table) > 0:
        table = table[0]
    with open('crime_data.csv', 'a') as f:
        trs = table.find_all('tr')
        if write_headers:
            for th in trs[0].find_all('th'):
                f.write(th.get_text(strip=True).encode('utf-8')+',')
            f.write('\n')
        for tr in trs:
            tds = tr.find_all('td')
            if len(tds) > 0:
                for td in tds:
                    f.write(td.get_text(strip=True).encode('utf-8')+',')
                f.write('\n')

# clear the table
open('crime_data.csv','w').close()

for i in range(1,11):
    page = urllib2.urlopen("http://b3.caspio.com/dp.asp?appSession=627360156923294&RecordID=&PageID=2&PrevPageID=2&CPIpage="+str(i)+"&CPISortType=&CPIorderBy=")
    scrape_crimes(''.join(i for i in page),i==1)
