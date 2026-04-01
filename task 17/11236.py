from math import prod

with open(r'.\files\17_11236.txt') as file:
    data = [int(i) for i in file]

min_2 = min(i for i in data if 10 <= abs(i) <= 99) ** 2
max_1 = max(i for i in data if 1000 <= abs(i) <= 9999 and abs(i) % 10 == 1)

ans = []
for nums in zip(data, data[1:], data[2:]):
    u1 = sum(i > min_2 for i in nums) == 2
    u2 = prod(map(abs, nums)) % abs(max_1) == 0
    if u1 and u2:
        ans.append(sum(map(abs, nums)))
print(len(ans), max(ans))
