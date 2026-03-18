def sp(line):
    words = line.split(" ")
    return "-".join(words)

line = input()
print(sp(line))