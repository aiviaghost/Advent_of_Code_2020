tot = 0

while (line := input()) != "":
	req, c, passw = line.split()
	i, j = map(int, req.split("-"))
	if passw[i - 1] == c[: -1] and passw[j - 1] != c[: - 1]:
		tot += 1
	elif passw[i - 1] != c[: -1] and passw[j - 1] == c[: - 1]:
		tot += 1

print(tot)
