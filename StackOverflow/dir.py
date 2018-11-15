
d = [{'directories': {   'dirname': [   'D:\\directory1\\subdir1','D:\\directory2\\subdir2']}},
{'directories': {   'dirname': 'D:\\directory1\\subdir1'}}]


rules = []

    for v in args["directories"]["dirname"]:
        ules.append(os.path.join(v, "*", "*"))
