def slopeCheck(treeMap, xMov, yMov):
    xPos = 0
    yPos = 0
    trees = 0
    mapWidth = len(treeMap[0])
    mapLength = len(treeMap)
    while yPos < mapLength:
        if treeMap[yPos][xPos % mapWidth] == '#':
            trees += 1
        xPos += xMov
        yPos += yMov
    return trees

def part1(treeMap):
    return slopeCheck(treeMap,3,1)

def part2(treeMap):
    return slopeCheck(treeMap,1,1) * slopeCheck(treeMap,3,1) * slopeCheck(treeMap,5,1) * slopeCheck(treeMap,7,1) * slopeCheck(treeMap,1,2)

treeMap = [l.strip("\n") for l in open("input","r").readlines()]
print(part1(treeMap))
print(part2(treeMap))
