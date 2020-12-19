field_reqs = []
while (line := input()) != "":
	req1_min, req1_max = map(int, line[line.find(":") + 2 : line.find(" or")].split("-"))
	req2_min, req2_max = map(int, line[line.find("or ") + 3 : ].split("-"))
	field_reqs.append((range(req1_min, req1_max + 1), range(req2_min, req2_max + 1), line[ : line.find(":")]))

input()
my_ticket = input()
for _ in range(2):
	input()

valid_tickets = []
valid_tickets.append([int(i) for i in my_ticket.split(",")])
while (line := input()) != "":
	ticket = [int(i) for i in line.split(",")]
	for field in ticket:
		valid = False
		for req1, req2 in field_reqs:
			if field in req1 or field in req2:
				valid = True
				break
		if valid:
			valid_tickets.append(ticket)

