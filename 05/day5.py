def decodeSeats(seats):
    seatNums = [int(seat.translate(seat.maketrans("FBLR","0101")),2) for seat in seats]
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
