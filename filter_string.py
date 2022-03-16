import re

def filter_string(word):
    word = word.lower() # All letter lowercase
    word = re.sub('[^a-z0-9]', '_', word) # Replace non-alphanumerics with '_'
    # ord(c) > 127 and c.isalpha()
    return word