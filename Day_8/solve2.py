global_instructions = []
while (inst := input()) != "":
	global_instructions.append(inst)

for i in range(len(global_instructions)):
	instructions = global_instructions.copy()
	if instructions[i].startswith("jmp"):
		instructions[i] = "nop" + instructions[i][instructions[i].find(" ") : ]
	elif instructions[i].startswith("nop"):
		instructions[i] = "jmp" + instructions[i][instructions[i].find(" ") : ]
	else:
		continue

	accumulator = 0
	vis = [-1] * len(global_instructions)
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
		
		if pointer == len(global_instructions):
			print(accumulator)
			exit(0)
