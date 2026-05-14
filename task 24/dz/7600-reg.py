from re import finditer

with open(r'..\files\24_7600.txt') as file:
    data = file.readline()


pattern = r'(?:(?![QRS]{2})[A-Z])+[A-Z]?'


matches = [match.group() for match in finditer(pattern, data)]


print(len(max(matches, key=len)))