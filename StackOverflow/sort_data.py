

x = [u'\r\nAt I-55 - Construction work.', u'\r\nAt Willow Ave - Accident.', u'\r\nAt Wolf Rd/Exit 16 - Accident.', u'\r\nBetween 55th St and Plainfield Rd - Roadwork.', u'\r\nBetween County Farm Rd and Windermere Dr - Roadwork.', u'\r\nBetween Geneva Rd and St Charles Rd - Roadwork.', u'\r\nBetween Jeans Rd and Knoll Wood Rd - Roadwork.', u'\r\nBetween Knoll Wood Rd and Jeans Rd - Roadwork.', u'\r\nBetween Lavergne Ave and Roy Ave - Construction work.', u'\r\nBetween Roy Ave and Lavergne Ave - Construction work.', u'\r\nBetween St Charles Rd and Geneva Rd - Roadwork.', u'\r\nBetween Windermere Dr and County Farm Rd - Roadwork.']

for i in sorted(x,key=lambda s: s[s.rfind('-')+1:]):
    print i

