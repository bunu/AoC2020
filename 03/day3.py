from math import prod

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
    slopes = [[1,1],[3,1],[5,1],[7,1],[1,2]]
    return prod([slopeCheck(treeMap,*slope) for slope in slopes]) 

treeMap = [l.strip("\n") for l in open("input","r").readlines()]
print(part1(treeMap))
print(part2(treeMap))
