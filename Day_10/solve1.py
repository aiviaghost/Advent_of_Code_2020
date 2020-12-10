vals = [0]
while (line := input()) != "":
	vals.append(int(line))

vals = sorted(vals)
vals.append(max(vals) + 3)

d1, d3 = 0, 0

for i in range(len(vals) - 1):
	if (vals[i + 1] - vals[i] == 1):
		d1 += 1
	elif vals[i + 1] - vals[i] == 3:
		d3 += 1

print(d1 * d3)
