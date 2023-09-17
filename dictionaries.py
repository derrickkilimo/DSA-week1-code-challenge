import string

def word_frequency(sentence):
    words = sentence.split()
    frequency = {}
    
    for word in words:
        word = word.strip(string.punctuation).lower()
        frequency[word] = frequency.get(word, 0) + 1
    
    return frequency