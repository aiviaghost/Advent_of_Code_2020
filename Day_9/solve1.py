def contains_pair(vals, k):
	seen = set()
	for val in vals:
		if k - val in seen:
			return True
		seen.add(val)
	return False

vals = []
while (line := input()) != "":
	vals.append(int(line))

ans = -1
for i in range(25, len(vals)):
	if not contains_pair(vals[i - 25 : i], vals[i]):
		ans = vals[i]
		break

print(ans)
