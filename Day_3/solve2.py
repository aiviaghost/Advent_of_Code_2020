grid = []
while (line := input()) != "":
	grid.append(line)

tot = 1
for p in [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]:
	temp = 0
	x = 0
	for y in range(0, len(grid), p[1]):
		if grid[y][x] == "#":
			temp += 1
		x = (x + p[0]) % len(grid[0])
	tot *= temp

print(tot)
