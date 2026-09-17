b = 0
try:
    a = 10/b
    print("try completed")
except ZeroDivisionError:
    print("OOPS didn't u study in school that u cant divide a number with zero")
finally:
    print("All the best...")
