vals = []
number = int(input())
while number != -1:
	vals.append(number)
	number = int(input())

seen = set()
for i in range(len(vals)):
	for j in range(len(vals)):
		for k in range(len(vals)):
			if i != j != k and vals[i] + vals[j] + vals[k] == 2020:
				print(vals[i] * vals[j] * vals[k])

# 259521570
