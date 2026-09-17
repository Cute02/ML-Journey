"""
Two fair dice are rolled. Without using any library, 
write code to calculate the probability that the sum equals 7.
"""
sample_space=[]
prob_count=0
for i in range(1,7):
    for j in range(1, 7):
        sample_space.append(((i,j)))
for i in sample_space:
    if i[0]+i[1]==7:
        prob_count+=1

print("P(two die thrown and sum equals to 7) = ", prob_count/36)
