import re
f = open('regex_sum_37803.txt')
total = 0
for line in f:
	numbers = re.findall('([0-9]+)', line)
	if len(numbers) != 0:
		for a in numbers:
			total += int(a)
print(total)
