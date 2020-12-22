field_reqs = []
while (line := input()) != "":
	req1_min, req1_max = map(int, line[line.find(":") + 2 : line.find(" or")].split("-"))
	req2_min, req2_max = map(int, line[line.find("or ") + 3 : ].split("-"))
	field_reqs.append((range(req1_min, req1_max + 1), range(req2_min, req2_max + 1), line[ : line.find(":")]))

input()
my_ticket = [int(i) for i in input().split(",")]
for _ in range(2):
	input()

valid_tickets = []
while (line := input()) != "":
	ticket = [int(i) for i in line.split(",")]
	valid_ticket = True
	for field in ticket:
		valid_field = False
		for req1, req2, name in field_reqs:
			if field in req1 or field in req2:
				valid_field = True
				break
		if not valid_field:
			valid_ticket = False
			break
	if valid_ticket:
		valid_tickets.append(ticket)

N = len(field_reqs)
used = set()
already_set = [-1] * N

while len(used) < N:
	for field_id, field in enumerate(field_reqs):
		if field_id in used:
			continue
		
		valid_columns = []
		for col in range(N):
			if already_set[col] == -1:
				valid_col = True
				for row in range(len(valid_tickets)):
					if valid_tickets[row][col] not in field[0] and valid_tickets[row][col] not in field[1]:
						valid_col = False
						break
				if valid_col:
					valid_columns.append(col)
		
		if len(valid_columns) == 1:
			already_set[valid_columns[0]] = field_id
			used.add(field_id)

answer = 1
for i in range(N):
	if field_reqs[already_set[i]][2].startswith("departure"):
		answer *= my_ticket[i]

print(answer)
