"""
 Write find_direction_change(pairs) that loops through consecutive pairs and returns the index where the y-values
 stop increasing and start decreasing (or vice versa) — i.e., detects where a trend "breaks." 
 Test it on Q3's dataset: [(15,20), (20,35), (25,55), (30,80), (35,60)].
 Think through the approach first:

 Loop through consecutive pairs of points (compare point i and point i+1's y-values) to figure out if each 
 step is going up or down.
 Keep track of the previous direction.
 The moment the current step's direction differs from the previous one, that's your "break" — return that index.
"""

def find_direction_change(pairs):
    previous_direction = None
    for i in range(len(pairs) - 1):
        if pairs[i+1][1] > pairs[i][1]:
            current_direction = "up"
        else:
            current_direction = "down"

        if previous_direction is not None and current_direction != previous_direction:
            return i  # index where the break happens

        previous_direction = current_direction

    return None  # no direction change found

data = [(15,20), (20,35), (25,55), (30,80), (35,60)]
print(find_direction_change(data))

        