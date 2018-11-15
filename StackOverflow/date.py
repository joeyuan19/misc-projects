import datetime
import re

current_date_format = "%d/%m/%Y"
new_date_format = "%d/%b/%Y"

def main():
    with open('date.txt','r') as f:
        with open('new_date.txt','w') as f2:
            f2.write(re.sub(r'\d{2}/\d{2}/\d{4}',fix_date,f.read()))

def fix_date(rem):
    date_string = rem.group()
    return datetime.datetime.strptime(date_string, current_date_format).strftime(new_date_format)

main()

