moves = []
while (line := input()) != "":
	moves.append(line)

curr_x, curr_y = 0, 0
curr_dir = 0

for move in moves:
	dir = move[0]
	if dir == 'N':
		curr_y += int(move[1 : ])
	elif dir == 'S':
		curr_y -= int(move[1 : ])
	elif dir == 'W':
		curr_x -= int(move[1 : ])
	elif dir == 'E':
		curr_x += int(move[1 : ])
	elif dir == 'L':
		curr_dir += int(move[1 : ])
	elif dir == 'R':
		curr_dir += 360 - int(move[1 : ])
	else:
		dist = int(move[1 : ])
		if curr_dir % 360 == 0:
			curr_x += dist
		elif curr_dir % 360 == 90:
			curr_y += dist
		elif curr_dir % 360 == 180:
			curr_x -= dist
		else:
			curr_y -= dist

print(abs(curr_x) + abs(curr_y))
