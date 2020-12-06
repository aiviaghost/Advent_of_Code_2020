tot = 0

data = []
while (line := input()) != "-1":
	data.append((line, set()))
	while True:
		line = input()
		if line == "":
			break
		data.append((line, set()))
	
	for p in data:
		for c in p[0]:
			p[1].add(c)
	
	if len(data) > 1:
		seen = data[0][1].intersection(data[1][1])
		for i in range(2, len(data)):
			seen = seen.intersection(data[i][1])
		tot += len(seen)
	else:
		tot += len(data[0][1])
	
	data.clear()

print(tot)
