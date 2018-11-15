import matplotlib.pyplot as plt
import csv

def pad(n,pad_length=3):
    s = str(n)
    return '0'*max(0,pad_length-len(s)) + s

class SampleData(object):
    def __init__(self,fname):
        with open(fname,'r') as f:
            csv_r = csv.reader(f)
            headers = []
            line1 = None
            line2 = None
            data = []
            for row in csv_r:
                if line1 is None:
                    line1 = row
                elif line2 is None:
                    line2 = row
                    for i,h in enumerate(line2):
                        j = 0
                        while line1[i-j] == "":
                            j += 1
                        headers.append(line1[i-j]+" "+line2[i])
                else:
                    entry = {}
                    for header,item in zip(headers,row):
                        entry[header] = self.parse(item)
                    data.append(entry)
        self.data = data
        self.headers = headers

    def parse(self,item):
        if item.endswith('%'):
            return float(item.rstrip('%'))/100
        elif item.startswith('JS-'):
            return int(item.lstrip('JS-'))
        else:
            try:
                return float(item)
            except:
                return item

    def graph(self,x_header,y_header,*args,**kwargs):
        if x_header not in self.headers:
            raise NoSuchDataException(x_header)
        elif y_header not in self.headers:
            raise NoSuchDataException(y_header)
        else:
            x,y = [],[]
            for entry in self.data:
                try:
                    x.append(entry[x_header])
                    y.append(entry[y_header])
                except:
                    pass
            if x_header == 'Sample Number':
                xticks = ['JS-'+pad(_x) for _x in x]
                plt.xticks(x,xticks)
            if y_header == 'Sample Number':
                yticks = ['JS-'+pad(_y) for _y in y]
                plt.yticks(y,yticks)
            plt.plot(x,y,*args,**kwargs)
            plt.show()
            

d = SampleData('Good InAs_Al Samples - Sheet1.csv')
d.graph('As','Resistance [300K 4pt averages on roughly 3x3 to 5x5 mm^2] Room (kOhm)','bo',linestyle='dashed')



