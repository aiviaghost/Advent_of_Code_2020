input()

pairs = [((int(j) - i) % int(j), int(j)) for i, j in enumerate(input().split(",")) if j != "x"]

for p in pairs:
    print(p)

# I am a little busy today so... https://www.dcode.fr/chinese-remainder
