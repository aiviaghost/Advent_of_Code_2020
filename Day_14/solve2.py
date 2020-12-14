bin_strings = []

def gen_bin(curr, n):
	if len(curr) < n:
		gen_bin(curr + "0", n)
		gen_bin(curr + "1", n)
	else:
		bin_strings.append(curr)

def bin_exp(base, exp):
	res = 1
	while (exp > 0):
		if (exp & 1) == 1:
			res *= base
		base *= base
		exp >>= 1
	return res

def int_to_bin(n):
	res = "{0:b}".format(n)
	while len(res) < 36:
		res = "0" + res
	return res

def filter(mask, val):
	res = []
	for i in range(36):
		if mask[i] == "0":
			res += val[i]
		else:
			res += mask[i]
	
	x_positions = 0
	for i in range(36):
		if res[i] == "X":
			x_positions += 1
	
	adresses = []
	if len(bin_strings) != x_positions:
		bin_strings.clear()
		gen_bin("", x_positions)
		
	for seq in bin_strings:
		x_index = 0
		for j in range(36):
			if res[j] == "X":
				mask[j] = seq[x_index]
				x_index += 1
			else:
				mask[j] = res[j]
		
		tot = 0
		for i in range(36):
			if mask[i] == "1":
				tot += bin_exp(2, 35 - i)
		adresses.append(tot)
	return adresses
	
	
mem = {}
mask = ""
while (line := input()) != "":
	adress = -1
	to_write = -1
	if line.startswith("mask"):
		mask = line[len("mask = ") : ]
	else:
		adress = int_to_bin(int(line[line.find("[") + 1 : line.find("]")]))
		to_write = int(line[line.find("=") + 2 : ])
		adresses = filter(list(mask), adress)
		for ad in adresses:
			mem[ad] = to_write
	
print(sum([v for k, v in mem.items()]))
