moves = []
while (line := input()) != "":
	moves.append(line)

curr_x, curr_y = 0, 0
px, py = 10, 1
curr_dir = 0

for move in moves:
	dir = move[0]
	if dir == 'N':
		py += int(move[1 : ])
	elif dir == 'S':
		py -= int(move[1 : ])
	elif dir == 'W':
		px -= int(move[1 : ])
	elif dir == 'E':
		px += int(move[1 : ])
	elif dir == 'L':
		iterations = -1
		if int(move[1 : ]) == 90:
			iterations = 1
		elif int(move[1 : ]) == 180:
			iterations = 2
		elif int(move[1 : ]) == 270:
			iterations = 3
		else:
			iterations = 4
		
		for _ in range(iterations):
			tx = px
			px = -py
			py = tx
	elif dir == 'R':
		iterations = -1
		if int(move[1 : ]) == 90:
			iterations = 1
		elif int(move[1 : ]) == 180:
			iterations = 2
		elif int(move[1 : ]) == 270:
			iterations = 3
		else:
			iterations = 4
		
		for _ in range(iterations):
			tx = px
			px = py
			py = -tx
	else:
		curr_x += int(move[1: ]) * px
		curr_y += int(move[1: ]) * py

print(abs(curr_x) + abs(curr_y))
