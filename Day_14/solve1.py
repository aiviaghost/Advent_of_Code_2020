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
	res = ""
	for i in range(36):
		if mask[i] != "X":
			res += mask[i]
		else:
			res += val[i]
	tot = 0
	for i in range(36):
		if res[i] == "1":
			tot += bin_exp(2, 35 - i)
	return tot
	
mem = {}
mask = ""
while (line := input()) != "":
	adress = -1
	to_write = -1
	if line.startswith("mask"):
		mask = line[len("mask = ") : ]
	else:
		adress = int(line[line.find("[") + 1 : line.find("]")])
		to_write = int_to_bin(int(line[line.find("=") + 2 : ]))
		mem[adress] = filter(mask, to_write)
	
	
print(sum([v for k, v in mem.items()]))
