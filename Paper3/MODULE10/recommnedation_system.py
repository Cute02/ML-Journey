import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

movies = ["Action A", "Action B", "Action C", "Romance A", "Romance B"]

ratings= np.array([[5, 4, 0, 0, 1],   # user 0 (we recommend for this user)
    [5, 5, 4, 0, 0],   # user 1
    [1, 0, 0, 5, 4],   # user 2
    [0, 1, 0, 4, 5]    # user 3
    ]) 

sim=cosine_similarity(ratings)

print("Similarity of user 0 to each user: ", sim[0].round(2))

others = sim[0].copy()

others[0] = -1
best =others.argmax()

print("Most similar user: ", best)

unseen = np.where(ratings[0]==0)[0]
pick = unseen[ratings[best, unseen].argmax()]
print("Recommend: ", movies[pick])
