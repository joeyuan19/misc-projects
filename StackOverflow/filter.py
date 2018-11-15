padded_names = ['albertGARBAGE', 'jamesTRASH', 'bobREFUSE', 'timRUBBISH', 'charlieWASTE']

def test(padded_name):
    names = ['albert', 'bob', 'charlie']
    return any(padded_name.find(name) >= 0 for name in names)
    

filtered_names = filter(test,padded_names)

print filtered_names


