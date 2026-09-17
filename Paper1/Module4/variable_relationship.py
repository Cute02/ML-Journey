def direction_pairs(pairs):
    if pairs[0][1]<pairs[-1][1]:
        return "positive"
    return "negative"
print(direction_pairs([(4,3), (5,4), (6,6), (7,7), (8,9)]))