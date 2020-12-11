grid = []
while (line := input()) != "":
	grid.append(line)

w, h = len(grid[0]), len(grid)

def is_inside(x, y):
	return 0 <= x < w and 0 <= y < h

has_changed = True
while has_changed:
	has_changed = False
	next_grid = [[' '] * w for _ in range(h)]
	for i in range(h):
		for j in range(w):
			neighbours = 0
			for k in range(-1, 2):
				for l in range(-1, 2):
					if is_inside(j + l, i + k) and (k != 0 or l != 0) and grid[i + k][j + l] == "#":
						neighbours += 1

			if grid[i][j] == 'L' and neighbours == 0:
				next_grid[i][j] = '#'
				has_changed = True
			elif grid[i][j] == '#' and neighbours >= 4:
				next_grid[i][j] = 'L'
				has_changed = True
			else:
				next_grid[i][j] = grid[i][j]
	grid = next_grid

count = 0
for i in range(h):
	for j in range(w):
		if grid[i][j] == '#':
			count += 1

print(count)
