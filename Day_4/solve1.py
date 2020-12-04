tot = 0

data = ""
while (line := input()) != "-1":
	data += line
	while line != "":
		line = input()
		data += " " + line
	
	data = data.replace("\n", "")
	data = data.strip()

	fields = []
	stuff = data.split()
	for s in stuff:
		fields.append(s.split(":")[0])
	
	count = 0
	for field in ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]:
		if field in fields:
			count += 1
	
	if count == 7:
		tot += 1
	
	data = ""

print(tot)
