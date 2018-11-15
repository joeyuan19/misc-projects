from random import randint, shuffle


def format_result(str1,str2):
	L = 8
	return str1 + ''.join(" " for i in range(L-len(str1) ) ) + " -> " + str2 + ''.join(" " for i in range(L - len(str2)))

def reassign_name(results,name,match):
	for i in results:
		if results[i] != match:
			results[name] = results[i]
			results[i] = match
			break

names = [
	"Art",
	"Phyllis",
	"Timmer",
	"Kate",
	"Caleb",
	"Matt",
	"Cat",
	"Scott",
	"Duane",
	"Daniel",
	"Joe"
]
restricted = {
	"Art":["Phyllis"],
	"Phyllis":["Art"],
	"Timmer":[],
	"Kate":["Scott"],
	"Scott":["Kate"],
	"Matt":["Cat"],
	"Cat":["Matt"],
	"Caleb":["Joe"],
	"Joe":["Caleb"],
	"Daniel":["Duane"],
	"Duane":["Daniel"]
}

itr = 0
c = [i for i in names]
results = {}

while len(c) > 0:
	name = names[itr]
	itr += 1
	if len(c) == 1 and c[0] == name:
		reassign_name(results,name,c[0])
	else:
		r = randint(0,len(c)-1)
		while c[r] == name or c[r] in restricted[name]:
			r = randint(0,len(c)-1)
	result = c.pop(r)
	results[name] = result

for i in results:
	print format_result(i,results[i])

print
print "SECOND ROUND"
print

itr = 0
names = names + ["Mitchell","Brenda","Aaron","Sarah","Sam"]
c = []
c = [i for i in names]
results = {
	"Matt":"Caleb",
	"Art":"Duane",
	"Timmer":"Art",
	"Caleb":"Phyllis",
	"Cat":"Timmer",
	"Duane":"Matt",
	"Daniel":"Joe",
	"Scott":"Cat",
	"Joe":"Kate",
	"Phyllis":"Scott",
	"Kate":"Daniel",
}
for i in ["Mitchell","Brenda","Aaron","Sarah","Sam"]:
	if i == "Mitchell":
		restricted[i] = ["Brenda"]
	if i == "Brenda":
		restricted[i] = ["Mitchell"]
	else:
		restricted[i] = []
	results[i] = ''
second_results = {}

while len(c) > 0:
	name = names[itr]
	itr += 1
	if len(c) == 1 and c[0] == name:
		reassign_name(results,name,c[0])
	else:
		r = randint(0,len(c)-1)
		while c[r] == name or c[r] in restricted[name] or results[name] == c[r]:
			r = randint(0,len(c)-1)
	result = c.pop(r)
	results[name] = result

for i in results:
	print format_result(i,results[i])

	


	


