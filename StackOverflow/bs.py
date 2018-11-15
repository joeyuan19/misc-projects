import requests
from bs4 import BeautifulSoup

#Return the results in dictionary form 
#{'Brown': 56.0126582278481, 'Whitman': 43.9873417721519}

html = requests.get("https://www.realclearpolitics.com/epolls/2010/governor/ca/california_governor_whitman_vs_brown-1113.html").text

soup = BeautifulSoup(html, 'html.parser')

#Scrape the percentage Numbers
table = soup.find_all('table')[0]
table_row = table.find_all('tr')[1]
table_data = table_row.find_all('td')[3:5]

#Scrape the Names
table_row_governors = table.find_all('tr')[0]
table_data_governors = table_row_governors.find_all('th')[3:5]
table_data_governors

table_data = [data.string for data in table_data]
table_data_governors = [data.string for data in table_data_governors]

dictionary = dict(zip(table_data_governors,table_data))
print(dictionary)
