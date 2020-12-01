# Part 1: Find two numbers that sum to 2020 and return the product
def doubleSearch(numbers):
    for n1 in numbers:
        for n2 in numbers:
            if (n1 + n2) == 2020:
                return(n1*n2)

# Part 2: Find three numbers that sum to 2020 and return the product
def tripleSearch(numbers):
    for n1 in numbers:
        for n2 in numbers:
            for n3 in numbers:
                if (n1 + n2 + n3) == 2020:
                    return(n1*n2*n3)

numbers = [int(s) for s in open("input","r").readlines()]
print(doubleSearch(numbers))
print(tripleSearch(numbers))
