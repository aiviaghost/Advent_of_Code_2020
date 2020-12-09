vals = []
while (line := input()) != "":
	vals.append(int(line))

target = 1504371145
target_index = vals.index(target)

for test_len in range(2, target_index):
	for i in range(target_index):
		if sum(vals[i : i + test_len + 1]) == target:
			print(min(vals[i : i + test_len + 1]) + max(vals[i : i + test_len + 1]))
			exit(0)
