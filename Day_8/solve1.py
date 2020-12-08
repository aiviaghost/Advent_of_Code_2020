accumulator = 0

instructions = []
while (inst := input()) != "":
	instructions.append(inst)

vis = [-1] * len(instructions)

pointer = 0
while vis[pointer] == -1:
	vis[pointer] = 1
	val = instructions[pointer][instructions[pointer].find(" ") + 1 : ]
	if val[0] == '+':
		val = val[1 : ]
	if instructions[pointer].startswith("acc"):
		accumulator += int(val)
		pointer += 1
	elif instructions[pointer].startswith("jmp"):
		pointer += int(val)
	else:
		pointer += 1

print(accumulator)
