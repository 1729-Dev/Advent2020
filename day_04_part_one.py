import os

dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, "day_04.data")

with open(filename) as f:
    lines = f.readlines()
    lines = list(map(lambda x: (x.strip()), lines))
    
    passports = []
    passport = ''

    for line in lines:
        if len(line) > 0:
            passport += ' ' + line
            continue;
        
        passports.append(passport)
        passport = ''

    passports.append(passport)

    valid_passports = 0

    for passport in passports:     
        print(f"passport: {passport}")
        tokens = passport.split(' ')
        tokens = list(map(lambda x: x[0:3], tokens))
        print(f"tokens: {tokens}")

        passport_valid = 'byr' in tokens and 'iyr' in tokens and 'eyr' in tokens and 'hgt' in tokens and 'hcl' in tokens and 'ecl' in tokens and 'pid' in tokens
        if passport_valid:
            valid_passports += 1

    print(f"valid passports: {valid_passports}")