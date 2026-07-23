"""
A bag has 5 red balls and 3 blue balls. Without replacement, one ball is drawn 
and it's red. Without using any library, calculate the probability that 
the second ball drawn is also red.
"""

red=5
blue=3
total=red +blue
red_after=red-1
total_after=total-1
prob_second_red=red_after/total_after
print("Probality of getting second red ball is ", prob_second_red)
