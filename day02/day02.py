import re

def parseLine(line):
	line = line.rstrip()
	rules = re.split(r'\s+|:\s|-',line)
	rules[0] = int(rules[0],10)
	rules[1] = int(rules[1],10)
	return rules

def validPartOne(rules):
	(min,max,char,password) = rules
	instances = password.count(char)
	if (min <= instances) and (instances <= max):
		return True
	else:
		return False

def validPartTwo(rules):
	(p1,p2,char,password) = rules
	pw_ary = re.split(r'',password) #note: pw_ary[0] and pw_ary[:-1] are ""
	if (((pw_ary[p1] == char) and (not (pw_ary[p2] == char))) or 
		(not (pw_ary[p1] == char) and (pw_ary[p2] == char))):
		return True
	else:
		return False

def test():
	test1 = "1-3 a: abcde\n"
	test2 = "1-3 b: cdefg\n"
	test3 = "2-9 c: ccccccccc\n"
	print(test1, validPartOne(parseLine(test1)))
	print(test2, validPartOne(parseLine(test2)))
	print(test3, validPartOne(parseLine(test3)))
	print(test1, validPartTwo(parseLine(test1)))
	print(test2, validPartTwo(parseLine(test2)))
	print(test3, validPartTwo(parseLine(test3)))

if __name__ == "__main__":
	
	valid_passwords_part_one = 0
	valid_passwords_part_two = 0
	filename = "input.txt"
	with open(filename,'r') as infile:
		for line in infile:
			if(validPartOne(parseLine(line))):
				valid_passwords_part_one+=1
			if(validPartTwo(parseLine(line))):
				valid_passwords_part_two+=1
	print("part 1 valid: ", valid_passwords_part_one)
	print("part 2 valid: ", valid_passwords_part_two)
	