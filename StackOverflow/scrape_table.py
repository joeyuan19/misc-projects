import urllib

from bs4 import BeautifulSoup


params = {
    "type":"team-detail",
    "league":"ncb",
    "stat_id":"3083",
    "season_id":"312",
    "cat_type":"2",
    "view":"stats_v1",
    "is_previous":"0",
    "date":"04/06/2015"
}

content = urllib.request.urlopen("http://www.teamrankings.com/ajax/league/v3/stats_controller.php",data=urllib.parse.urlencode(params)).read()
soup = BeautifulSoup(content)

table = soup.find("table", attrs={'class':'sortable'})

data = []
rows = table.findAll("tr")
for tr in rows:
    cols = tr.findAll("td")
    for td in cols:
        text = ''.join(td.find(text=True))
        data.append(text)

print(data)
