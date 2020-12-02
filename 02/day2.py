# Split requirment string in to its 3 parts
def parseRequirements(s):
    r1 = int(s.split(" ",)[0].split("-")[0])
    r2 = int(s.split(" ",)[0].split("-")[1])
    letter = s.split(" ",)[1]
    return r1, r2, letter

# Part 1: Verify passwords have between minl and maxl of letter and return the number of correct passwords
def part1(passwords):
    count = 0
    for p in passwords:
        minl, maxl, letter = parseRequirements(p[0])
        countl = 0
        for l in p[1].strip(" "):
            if l == letter:
                countl += 1
        if countl >= minl and countl <= maxl:
            count += 1
    return count

# Part 2: Verify passwords that have letter in either pos1 or pos2 but not both and return the number of correct passwords
def part2(passwords):
    count = 0
    for p in passwords:
        pos1, pos2, letter = parseRequirements(p[0])
        p[1] = p[1].strip(" ")
        if (p[1][pos1-1] == letter and p[1][pos2-1] != letter) or (p[1][pos1-1] != letter and p[1][pos2-1] == letter):
            count += 1
    return count

passwords = [s.strip("\n").split(":") for s in open("input","r").readlines()]
print(part1(passwords))
print(part2(passwords))
