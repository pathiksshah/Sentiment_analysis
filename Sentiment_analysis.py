punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']

### removes characters considered punctuation from everywhere in the word
def strip_punctuation(s):
    for c in punctuation_chars:
        snew=s.replace(c,'')
        s=snew
    return s

print(strip_punctuation("#Amazing"))