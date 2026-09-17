def find_pairs(nums, target):
    seen = set()
    pairs = []
    for x in nums:
        if target-x in seen:
            pairs.append((target-x, x))
        else:
            seen.add(x)
    return pairs


print(find_pairs([2, 7, 11, 15, -2, 9], 9))
