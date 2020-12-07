ids = []
adj = {}
while (line := input()) != "":
	id = line[ : line.find("contain") - 1]
	if id[-1] == 's':
		id = id[ : -1]
	ids.append(id)
	stuff = []
	contained = line[line.find("contain") + len("contain") + 1 : ].split(", ")
	for thing in contained:
		if thing == "no other bags.":
			break
		temp_thing = thing[thing.find(" ") + 1 : ]
		count = int(thing[ : thing.find(" ")])
		if temp_thing[-2 : ] == "s.":
			temp_thing = temp_thing[ : -2]
		elif temp_thing[-1] == 's':
			temp_thing = temp_thing[ : -1]
		elif temp_thing[-1] == '.':
			temp_thing = temp_thing[ : -1]
		stuff.append((temp_thing, count))
	
	adj[id] = stuff

def dfs(curr, extra):
	if len(adj[curr]) == 0:
		return 1
	
	total = 0
	for next in adj[curr]:
		if extra:
			total += next[1]
		total += next[1] * dfs(next[0], extra)
	
	return total

tot = dfs("shiny gold bag", True) - dfs("shiny gold bag", False)

print(tot)
