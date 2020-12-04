def splitPassports(passports):
    splitPassports = []
    for passport in passports:
        splitPassports.append([param.split(":") for param in passport])
    return splitPassports

def validNumber(number,low,high):
    try:
        int(number)
    except ValueError:
        return False
    else:
        return (int(number) >= low and int(number) <= high)

def validbyr(param):
    return validNumber(param,1920,2002)

def validiyr(param):
    return validNumber(param,2010,2020)

def valideyr(param):
    return validNumber(param,2020,2030)

def validhgt(param):
    number = param[0:len(param)-2]
    unit = param[len(param)-2:len(param)]
    if unit == "cm":
        return validNumber(number,150,193)
    elif unit == "in":
        return validNumber(number,59,76)
    else:
        return False

def validhcl(param):
    if param[0] != "#" and len(param) != 7:
        return False
    try:
        int(param[1:len(param)],16)
    except ValueError:
        return False
    else:
        return True

def validecl(param):
    return param in ["amb","blu","brn","gry","grn","hzl","oth"]

def validpid(param):
    if len(param) == 9:
        try:
            int(param)
        except ValueError:
            return False
        else:
            return True
    return False

def default(param):
    return True

def validParamNumber(passports):
    validList = []
    for passport in passports:
        if(len(passport) == 8):
           validList.append(passport)
        elif(len(passport) == 7):
            if not "cid" in [param[0] for param in passport]:
                validList.append(passport)
    return validList

def validContents(passports):
    validList = []
    switch = {
        "byr": validbyr,
        "iyr": validiyr,
        "eyr": valideyr,
        "hgt": validhgt,
        "hcl": validhcl,
        "ecl": validecl,
        "pid": validpid,
    }
    for passport in passports:
        valid = True
        for param in passport:
            func = switch.get(param[0], default)
            if not func(param[1]):
                valid = False
                break
        if valid:
            validList.append(passport)
    return validList

def part1(passports):
    passports = validParamNumber(passports)    
    return len(passports)

def part2(passports):
    validPassports = validParamNumber(passports)
    validPassports = validContents(validPassports)
    return len(validPassports)

passports = splitPassports([ l.replace("\n", " ").strip(" ").split(" ") for l in open("input","r").read().split("\n\n")])
print(part1(passports))
print(part2(passports))
