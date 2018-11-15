def txt_to_dict(txt):
    data = {}
    lines = txt.split('\n')
    i = 0
    while i < len(lines):
        try:
            key,val = lines[i].split(':')
        except:
            print "Invalid row format"
            i += 1
            continue
        key = key.strip()
        val = val.strip()
        if len(val) == 0:
            i += 1
            sub = ""
            while lines[i].startswith('\t') or lines[i].startswith('    '):
                  sub += lines[i] + '\n'
                  i += 1
            data[key] = txt_to_dict(sub)
        else:
            data[key] = val
            i += 1
    return data

with open('test.txt','r') as f:
    content = ''.join(i for i in f)

print txt_to_dict(content)
