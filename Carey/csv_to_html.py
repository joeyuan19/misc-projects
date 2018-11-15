import csv
import sys

reload(sys)
sys.setdefaultencoding('utf8')

def to_html(reader):
    html = '<html>\n\t<head></head>\n\t<body>\n\t\t<table>\n'
    for row in reader:
        html += '\t\t\t<tr>\n'
        for cell in row:
            html += '\t\t\t\t<td>'+cell+'</td>\n'
        html += '\t\t\t</tr>\n'
    html = html[:-1]
    html += '\n\t\t<table>\n\t</body>\n</html>'
    return html

with open(sys.argv[1],'r') as f:
    csv_r = csv.reader(f,delimiter='\t')
    with open(sys.argv[1].rstrip('csv')+'html','w') as fw:
        fw.write(to_html(csv_r))
