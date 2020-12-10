vals = [0]
while (line := input()) != "":
	vals.append(int(line))

vals = sorted(vals)
vals.append(max(vals) + 3)

ways = [0] * len(vals)
ways[len(vals) - 1] = 1
for i in range(len(vals) - 1, -1, -1):
	for j in range(1, 4):
		if i + j < len(vals) and vals[i + j] - vals[i] < 4:
			ways[i] += ways[i + j]

print(ways[0])
