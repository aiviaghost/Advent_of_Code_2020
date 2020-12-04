tot = 0

data = ""
while (line := input()) != "-1":
	data += line
	while line != "":
		line = input()
		data += " " + line
	
	data = data.replace("\n", "")
	data = data.strip()

	fields = {}
	stuff = data.split()
	for s in stuff:
		a, b = s.split(":")
		fields[a] = b
	
	count = 0
	for field in ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]:
		if field in fields.keys():
			if field == "byr" and int(fields[field]) in [i for i in range(1920, 2003)]:
				count += 1
			elif field == "iyr" and int(fields[field]) in [i for i in range(2010, 2021)]:
				count += 1
			elif field == "eyr" and int(fields[field]) in [i for i in range(2020, 2031)]:
				count += 1
			elif field == "hgt":
				if fields[field][-2 : ] == "cm" and int(fields[field][ : -2]) in [i for i in range(150, 194)]:
					count += 1
				elif fields[field][-2 : ] == "in" and int(fields[field][ : -2]) in [i for i in range(59, 77)]:
					count += 1
			elif field == "hcl" and fields[field][0] == '#' and len(fields[field]) == 7:
				valid = True
				for c in fields[field][1 :]:
					if c not in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "a", "b", "c", "d" ,"e", "f"]:
						valid = False
						break
				if valid:
					count += 1
			elif field == "ecl" and fields[field] in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:
				count += 1
			elif field == "pid" and len(fields[field]) == 9:
				valid = True
				for c in fields[field]:
					if c not in [str(i) for i in range(10)]:
						valid = False
						break
				if valid:
					count += 1

	if count == 7:
		tot += 1
	
	data = ""

print(tot)
