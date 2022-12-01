import fileinput

elves = []
current_elf_calorie_count = 0
line_count = 0

for line in fileinput.input():
    line_count += 1
    text = line.rstrip()

    if text:
        numeric_value = int(text)
        current_elf_calorie_count += numeric_value
        continue

    elves.append(current_elf_calorie_count)
    current_elf_calorie_count = 0
    
# print(f"{line_count} lines")

max_calories = max(elves)
print(max_calories)