import re

def parse(data):
    lines = data.split('\n')  # get the lines by splitting on the newline char
    lines = [line[len("Tue Feb 24 17:51:10.835 SRV02    NOTICE  "):]  for  line in lines]  # remove the number of characters equal to the logging info
    out = []
    header = ''
    for line in lines:
        if line.startswith('   '):
            if line.strip().startswith('hist'):
                out.append(header + ";" + extract_hist_data(line))  # outsource the specific extracting to a function for ease of readability
        else:                      # header/samples line
            if all(i in line for i in ("samples", "avg", "min", "max")):  # if the line contains all these keywords
                out.append(header + ";" + extract_stat_data(line))  # outsource the specific extracting to a function for ease of readability
            else:  # Treat as a header
                header = line
    return '\n'.join(out)

def extract_hist_data(line):
    data = re.findall(r'(hist\[\s*?\d+\]).*?(\d+\.\d+).*?(\d+)',line)
    if len(data) > 0:
        data = data[0]
    else:
        return ""
    return ';'.join(i for i in data)

def extract_stat_data(line):
    data = re.findall(r'(samples).*?(\d+).*?(avg).*?(\d+\.\d+).*?(min).*?(\d+\.\d+).*?(max).*?(\d+\.\d+)',line)
    if len(data) > 0:
        data = data[0]
    else:
        return ""
    return ';'.join(i for i in data)

def parse_log_file(log_file_path):
    with open(log_file_path,'r') as f:
        content = ''.join(i for i in f)
    return parse(content)

print parse_log_file('test.log')
