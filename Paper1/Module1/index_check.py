def first_unique_char(str1):
    seen={}
    for i in str1:
        if seen[i]==str1.index(i):
            seen.pop()


