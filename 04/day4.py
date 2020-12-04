def splitPassports(passports):
    splitPassports = []
    for passport in passports:
        splitPassports.append([param.split(":") for param in passport])
    return splitPassports

def validNumber(param,low,high):
    try:
        int(param)
    except ValueError:
        return false
    else:
        return (int(param) >= low and int(param) <= high)

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
    if unit == "in":
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
    switch = {
        "amb":True,
        "blu":True,
        "brn":True,
        "gry":True,
        "grn":True,
        "hzl":True,
        "oth":True,
    }
    return switch.get(param,False)

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
        if(len(passport) == 7):
            containsCID = False
            for p in passport:
                if p[0] == "cid":
                    containsCID = True
            if not containsCID:
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

passports = splitPassports([ l.replace("\n", " ").split(" ") for l in open("input","r").read().split("\n\n")])
print(part1(passports))
print(part2(passports))
