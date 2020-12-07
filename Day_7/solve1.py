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
		if temp_thing[-2 : ] == "s.":
			stuff.append(temp_thing[ : -2])
		elif temp_thing[-1] == 's':
			stuff.append(temp_thing[ : -1])
		elif temp_thing[-1] == '.':
			stuff.append(temp_thing[ : -1])
		else:
			stuff.append(temp_thing)
	adj[id] = stuff

def dfs(vis, curr):
	if curr in vis:
		return False
	
	if curr == "shiny gold bag":
		return True

	vis.add(curr)
	for next in adj[curr]:
		if dfs(vis, next):
			return True
	
	return False

tot = 0
for id in ids:
	vis = set()
	if dfs(vis, id):
		tot += 1

print(tot - 1)
