with open("day1/input.txt", 'r') as f:
    nums = [[int(num) for num in group.split("\n") if num != ""]  for group in f.read().split("\n\n")]

part1 = max(map(sum, nums))
part2 = sum(sorted(map(sum, nums), reverse=True)[:3])

print(part1, part2)