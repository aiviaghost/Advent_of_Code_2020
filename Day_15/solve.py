starting_numbers = [1,17,0,10,18,11,6]

def solve(max_iterations):
	last_index_of = { j : i for i, j in enumerate(starting_numbers) }
	last_index_before_then = {}
	seen_count = { i : 1 for i in starting_numbers }

	iterations = len(starting_numbers)
	last_spoken = starting_numbers[-1]
	while (iterations < max_iterations):
		if seen_count[last_spoken] == 1:
			last_spoken = 0
		else:
			last_spoken = last_index_of[last_spoken] - last_index_before_then[last_spoken]

		if last_spoken in seen_count:
			seen_count[last_spoken] += 1

			last_index_before_then[last_spoken] = last_index_of[last_spoken]
			last_index_of[last_spoken] = iterations
		else:
			seen_count[last_spoken] = 1
			last_index_of[last_spoken] = iterations

		iterations += 1
	
	return last_spoken
	

print(solve(2020))
print(solve(30000000))
