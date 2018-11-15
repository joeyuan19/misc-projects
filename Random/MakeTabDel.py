


class payrollEntry:
	def __init__(self, date,price,name,category=None):
		self.date = date
		self.price = price
		self.name = name

	def get_result(self):
		return self.date + '\t' + self.name + '\t' + self.price

info = []

for i in range(5):
	date = raw_input("Whats the date?\n")
	price = raw_input("Whats the price?\n")
	name = raw_input("Whats the name?\n")
	category = raw_input("Whats the Category?\n")
	info.append(payrollEntry(date,price,name,category))
	print


for i in info:
	print i.get_result()

