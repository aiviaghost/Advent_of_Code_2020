grid = []
while (line := input()) != "":
	grid.append(line)

w, h = len(grid[0]), len(grid)

def is_inside(x, y):
	return 0 <= x < w and 0 <= y < h

has_changed = True
while has_changed:
	changed = False
	next_grid = [[' '] * w for _ in range(h)]
	for i in range(h):
		for j in range(w):
			neighbours = 0
			for k in range(1, w):
				if is_inside(j + k, i):
					if grid[i][j + k] == '#':
						neighbours += 1
						break
					elif grid[i][j + k] == 'L':
						break
			
			for k in range(1, h):
				if is_inside(j, i + k):
					if grid[i + k][j] == '#':
						neighbours += 1
						break
					elif grid[i + k][j] == 'L':
						break
			
			for k in range(1, w):
				if is_inside(j - k, i):
					if grid[i][j - k] == '#':
						neighbours += 1
						break
					elif grid[i][j - k] == 'L':
						break
			
			for k in range(1, h):
				if is_inside(j, i - k):
					if grid[i - k][j] == '#':
						neighbours += 1
						break
					elif grid[i - k][j] == 'L':
						break
			
			for k in range(1, max(w, h)):
				if is_inside(j + k, i + k):
					if grid[i + k][j + k] == '#':
						neighbours += 1
						break
					elif grid[i + k][j + k] == 'L':
						break
			
			for k in range(1, max(w, h)):
				if is_inside(j + k, i - k):
					if grid[i - k][j + k] == '#':
						neighbours += 1
						break
					elif grid[i - k][j + k] == 'L':
						break
			
			for k in range(1, max(w, h)):
				if is_inside(j - k, i - k):
					if grid[i - k][j - k] == '#':
						neighbours += 1
						break
					elif grid[i - k][j - k] == 'L':
						break
			
			for k in range(1, max(w, h)):
				if is_inside(j - k, i + k):
					if grid[i + k][j - k] == '#':
						neighbours += 1
						break
					elif grid[i + k][j - k] == 'L':
						break

			if grid[i][j] == 'L' and neighbours == 0:
				next_grid[i][j] = '#'
				changed = True
			elif grid[i][j] == '#' and neighbours >= 5:
				next_grid[i][j] = 'L'
				changed = True
			else:
				next_grid[i][j] = grid[i][j]
	has_changed = changed
	grid = next_grid

count = 0
for i in range(h):
	for j in range(w):
		if grid[i][j] == '#':
			count += 1

print(count)
