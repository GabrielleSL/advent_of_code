import re

with open("input.txt", "r") as file:
    line = file.read().replace("\n", " ")

ans1 = 0
ans2 = 0

valid = re.findall(r"mul\(\d{1,3},\d{1,3}\)", line)
ans1 = sum(int(a) * int(b) for a, b in [re.findall(r"\d+", mult) for mult in valid])

new_line = re.sub(r"don't\(\)(.*?)(do\(\)|$)", ' ', line)
valid2 = re.findall(r"mul\(\d{1,3},\d{1,3}\)", new_line)
ans2 = sum(int(a) * int(b) for a, b in [re.findall(r"\d+", mult) for mult in valid2])


print("PART 1:", ans1)

print("PART 2:", ans2)
