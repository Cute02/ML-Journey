"""    
*        *
**      **
* *    * *
*  *  *  *
*   **   *
*   **   *
*  *  *  *
* *    * *
**      **   
*        *
"""
n = 5
for row in range(1, n+1):
    for star in range(1, row+1):
        if star == 1 or star == row:
            print("*", end="")
        else:
            print(" ", end="")
    for space in range(1, 2*(n-row)+1):

        print(" ", end="")

    for star in range(1, row+1):
        if star == 1 or star == row:
            print("*", end="")
        else:
            print(" ", end="")

    print()

for row in range(n, 0, -1):
    for star in range(1, row+1):
        if star == 1 or star == row:
            print("*", end="")

        else:
            print(" ", end="")
    for space in range(1, 2*(n-row)+1):

        print(" ", end="")

    for star in range(1, row+1):
        if star == 1 or star == row:
            print("*", end="")
        else:
            print(" ", end="")

    print( )
