def decodeSeats(seats):
    seatNums = []
    for seat in seats:
        row = int(seat[:7].replace("B","1").replace("F","0"),2)
        col = int(seat[7:].replace("R","1").replace("L","0"),2)
        seatNums.append((row * 8) + col)
    return sorted(seatNums)

def part1(seats):
    return decodeSeats(seats)[-1]

def part2(seats):
    seatIDs = decodeSeats(seats)
    for seat in range(seatIDs[0],seatIDs[-1]):
        if seat not in seatIDs:
            return seat

seats = open("input","r").readlines()
print(part1(seats))
print(part2(seats))
