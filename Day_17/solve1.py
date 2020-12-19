n = 20

grid = [[[0] * n for _ in range(n)] for _ in range(n)]

init = []
for _ in range(8):
	init.append(input())

for i in range(8):
	for j in range(8):
		if init[i][j] == "#":
			grid[10][6 + i][6 + j] = 1

def is_inside(x, y, z):
	return 0 <= x < n and 0 <= y < n and 0 <= z < n

for _ in range(6):
	new_grid = [[[0] * n for _ in range(n)] for _ in range(n)]
	for i in range(n):
		for j in range(n):
			for k in range(n):
				neighbours = 0
				for ii in range(-1, 2):
					for jj in range(-1, 2):
						for kk in range(-1, 2):
							if is_inside(i + ii, j + jj, k + kk) and (ii != 0 or jj != 0 or kk != 0) and grid[i + ii][j + jj][k + kk] == 1:
								neighbours += 1
				
				if grid[i][j][k] == 1 and (neighbours == 2 or neighbours == 3):
					new_grid[i][j][k] = 1
				elif grid[i][j][k] == 1 and neighbours != 2 and neighbours != 3:
					new_grid[i][j][k] = 0
				elif grid[i][j][k] == 0 and neighbours == 3:
					new_grid[i][j][k] = 1

	grid = new_grid

tot = 0
for i in range(n):
	for j in range(n):
		for k in range(n):
			tot += grid[i][j][k]

print(tot)
