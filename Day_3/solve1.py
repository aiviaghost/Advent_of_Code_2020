grid = []
while (line := input()) != "":
	grid.append(line)

tot, x = 0, 0
for y in range(len(grid)):
	if grid[y][x] == "#":
		tot += 1
	x = (x + 3) % len(grid[0])

print(tot)
