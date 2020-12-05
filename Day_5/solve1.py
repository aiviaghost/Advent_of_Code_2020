max_id = -1

while (line := input()) != "":
	lower, upper, rmid = 0, 127, -1
	for i in range(7):
		rmid = (lower + upper) // 2
		if line[i] == 'F':
			upper = rmid
		else:
			lower = rmid + 1
	rmid = (lower + upper) // 2
	
	lb, rb, cmid = 0, 7, -1
	for i in range(3):
		cmid = (lb + rb) // 2
		if line[7 + i] == 'L':
			rb = cmid
		else:
			lb = cmid + 1
	cmid = (lb + rb) // 2
	
	max_id = max(8 * rmid + rb, max_id)

print(max_id)
