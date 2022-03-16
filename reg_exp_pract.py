from filter_to_match import filter_to_match

a = ['10 Freaky Girls (with 21 Savage)', '100 (feat. Drake)', 'You Don\'t Own Me (feat. G-Eazy) - Candyland Remix']

b = [filter_to_match(i) for i in a]
print(b)