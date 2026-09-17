data = [7, 14, 2, 7, 19, 11, 2, 5, 20, 1]
frequencies = {}
for item in data:
    frequencies[item] = frequencies.get(item, 0)+1
max_count = max(frequencies.values())
modes = [key for key, count in frequencies.items() if max_count == count]
if len(modes) == len(frequencies):
    print("No mode")
else:
    print(modes)
