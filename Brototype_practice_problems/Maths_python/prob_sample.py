def probability(data, total, threshold):
    favorable=0
    print(total)
    for i in data:
        if i>threshold:
            favorable+=1
    return favorable/total

scores = [45, 62, 78, 40, 55, 90, 33, 67, 51, 82, 39, 71, 60, 48, 95]
length=len(scores)
print("Probablity of students getting scores more than 50: ", probability(scores, length, 50))