import statistics

data = [85, 90, 75, 90, 95, 80, 100]

data_mean = statistics.mean(data)
data_median = statistics.median(data)
data_mode = statistics.mode(data)
data_stdev = statistics.stdev(data)

print(f"Our Data Set: {data}\n")
print(f"Mean (Average):     {data_mean:.3f}")
print(f"Median (Middle):    {data_median}")
print(f"Mode (Most Common): {data_mode}")
print(f"Standard Deviation: {data_stdev:.3f}")
