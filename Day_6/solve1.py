tot = 0

data = ""
while (line := input()) != "-1":
	data += line
	while line != "":
		line = input()
		data += line
	
	seen = set()
	for c in data:
		seen.add(c)
	
	tot += len(seen)
	data = ""

print(tot)
