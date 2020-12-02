
input_file = "day_01_input.txt"
expenses = []

with open(input_file,'r') as infile:
	for number in infile:
		expenses.append(int(number,10))

for value1 in expenses:
	for value2 in expenses:
		if (value1+value2) == 2020:
			print("value1: {:d}, value2: {:d}, product: {:d}".format(value1,value2,value1*value2))