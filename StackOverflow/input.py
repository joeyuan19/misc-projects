input = raw_input("Please provide your title and name: ").split()
if len(input) > 1:   # at least two entries provided
    title = input[0] # the first is the title
    name = input[1]  # the second is the name
elif len(input) > 0: # one input provided
    title = ""        # Or another default
    name = input[0]  # assign to name
print title,name
