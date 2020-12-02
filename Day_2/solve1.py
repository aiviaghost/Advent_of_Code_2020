tot = 0

while (line := input()) != "":
	req, c, passw = line.split()
	lower, upper = map(int, req.split("-"))
	if passw.count(c[: -1]) in [i for i in range(lower, upper + 1)]:
		tot += 1

print(tot)
