import re

def filter_to_match(word):
    word = word.lower() # All letter lowercase
    word = re.sub('(?= \(feat.)(.*?)(?<=\))', '', word)
    word = re.sub('(?= \(with)(.*?)(?<=\))', '', word)
    word = re.sub('(?= \(ft.)(.*?)(?<=\))', '', word)
    # word = re.sub(' \(feat.*[a-z0-9]+\)*', '', word)
    # word = re.sub(r"^[ (feat.]", '', word)
    # word = re.sub('[^a-z0-9]', '_', word) # Replace non-alphanumerics with '_'
    return word