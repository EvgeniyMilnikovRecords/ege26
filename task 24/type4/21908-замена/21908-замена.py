from string import printable

with open(r'..\files\21908.txt') as file:
    data = file.readline().lower()

for i in printable[14:]:
    data = data.replace(i, ' ')

data = data.split()
ans = 0
for line in data:
    line = line.rstrip('13579bd').lstrip('0')
    ans = max(ans, len(line))

print(ans)
