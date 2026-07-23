unordered_dict = {'banana': 3, 'apple': 5, 'cherry': 1}

# Sort by key in ascending order
sorted_dict = sorted(unordered_dict.items(), key=lambda x:x[1])
print(sorted_dict)
print(dict(sorted_dict))

#List Comprehension
data=[1,2,3,4,5,6,7,8,9]
lst1=[x for x in data if x%2==0]
print(lst1)