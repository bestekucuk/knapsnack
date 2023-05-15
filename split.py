with open("ks_200_0", "r") as file:
    lines = file.readlines()

updated_lines = []
for line in lines:
    numbers = line.split()
    updated_line = " ".join(numbers) + "\n"
    updated_lines.append(updated_line)

with open("ks_200_0_", "w") as file:
    file.writelines(updated_lines)
