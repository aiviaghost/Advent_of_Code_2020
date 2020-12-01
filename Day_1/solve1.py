vals = []
while (number := int(input())) != -1:
	vals.append(number)

seen = set()
for val in vals:
	if 2020 - val in seen:
		print(val * (2020 - val))
	seen.add(val)

# 987339
