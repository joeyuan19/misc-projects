np = 68962
nte = 34273
shares = np + nte

price = 11.039
fx = 6.279
us_price = price/fx
ron_gross = 1139611.17
comm = 1709.42
eng_net = 181223.40

old_np = 122680.33
old_nte = 60970.14
old_total = old_np+old_nte

print "shares",shares
print
print "old",old_total
print "new",eng_net
print "diff",old_total-eng_net
print
print "us price",us_price
print "us amt",us_price*shares
print "net amt",us_price*shares-comm
print
print "new",eng_net*(old_np/old_total)
print "nte",eng_net*(old_nte/old_total)
print "total",eng_net
print
print "new comm",(comm/fx)*(old_np/old_total)
print "nte comm",(comm/fx)*(old_nte/old_total)
print "total comm",(comm/fx)
