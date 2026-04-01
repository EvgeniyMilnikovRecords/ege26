with open(r'.\files\17_2997.txt') as file:
    data = [int(i) for i in file]
ans = []
nums = [int(str(abs(i))[1]) for i in data if 100 <= abs(i) <= 999]
most = max((nums.count(i), i) for i in range(10))[1]
for nums in zip(data, data[1:]):
    if any(abs(i) % 10 == most for i in nums):
        ans.append(sum(nums))

print(len(ans), max(ans))
