def word_frequency(text):
    punctuation = "!@#$%^&*(,).<>:;\'\?\""
    new_text = "".join(
        char for char in text if char not in punctuation).lower()
    new_dict = {}
    for ch in new_text.split():
        if ch in new_dict:
            new_dict[ch] = new_dict[ch]+1
        else:
            new_dict[ch] = 1
    return new_dict


print(word_frequency("The cat sat on the mat. The cat ran."))
