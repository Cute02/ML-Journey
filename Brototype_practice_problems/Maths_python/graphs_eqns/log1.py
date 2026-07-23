"""
 my_log(x, base) from scratch. Since you can't use math.log, use this trick:
 repeatedly divide x by base, counting how many times until x drops to 1 or below.
 That count approximates log_base(x). Test it on x=100, base=10 — should give roughly 2.
"""

def my_log(x, base):
    count=0
    while x >1:
       x = x/base
       count+=1
    return count

print(my_log(100, 10))
        