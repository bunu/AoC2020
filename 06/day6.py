def part1(groups):
    sets = [set(list(group.replace("\n",""))) for group in groups]
    return  sum([len(s) for s in sets])

def part2(groups):
    sets = [set.intersection(*[set(list(i)) for i in group.split("\n")]) for group in groups]
    return  sum([len(s) for s in sets])

groups = open("input","r").read().strip(" ").split("\n\n")
print(part1(groups))
print(part2(groups))
