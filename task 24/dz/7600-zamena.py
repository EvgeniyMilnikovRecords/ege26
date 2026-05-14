with open(r'..\files\24_7600.txt') as file:
    data = file.readline()


for a in 'QRS':
    for b in 'QRS':
        data = data.replace(a+b, a + ' ' + b)

data = data.split()

print(len(max(data, key=len)))