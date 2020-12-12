import os

dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, "day_04.data")

def eye_colour_valid(eye_colour):
    print(f"eye: {eye_colour}")
    return eye_colour in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']

def birth_year_valid(birth_year):
    print(f"birth: {birth_year}")
    try:
        year = int(birth_year)
        return year >= 1920 and year <= 2002
    except ValueError:
        return False

def issue_year_valid(issue_year):
    print(f"issue: {issue_year}")
    try:
        year = int(issue_year)
        return year >= 2010 and year <= 2020
    except ValueError:
        return False

def height_valid(height):
    try:
        if height.endswith('cm'):
            number = int(height.strip('cm'))
            return number >= 150 and number <= 193
        if token.endswith('in'):
            number = int(height.strip('in'))
            return number >= 59 and number <= 76
    except ValueError:
        return False
    return False

def passport_id_valid(passport_id):
    if not len(passport_id) == 9:
        return False

    try:
        int(passport_id)
        return True
    except ValueError:
        return False

def hair_colour_valid(hair_colour):
    if not len(hair_colour) == 7:
        return False

    if not hair_colour[0] == '#':
        return False

    colour_code = hair_colour[1:7]
    for colour in colour_code:
        if colour >= 'a' and colour <= 'f':
            continue
        if colour >= '0' and colour <= '9':
            continue
        return False
    
    return True

def expiration_year_valid(exp_year):
    print(f"exp year: {exp_year}")
    try:
        year = int(exp_year)
        return year >= 2020 and year <= 2030
    except ValueError:
        return False

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
        tokens = passport.split(' ')
        tokens = list(map(lambda x: x[0:3], tokens))

        passport_valid = 'byr' in tokens and 'iyr' in tokens and 'eyr' in tokens and 'hgt' in tokens and 'hcl' in tokens and 'ecl' in tokens and 'pid' in tokens

        if not passport_valid:
            print(f"Not enough tokens: {passport}")
            continue

        tokens = passport.split(' ')
        fields_valid = True

        for token in tokens:
            # birth year
            if token[0:3] == 'byr':
                fields_valid = fields_valid and birth_year_valid(token.split(':')[1])

            # issue year
            if token[0:3] == 'iyr':
                fields_valid = fields_valid and issue_year_valid(token.split(':')[1])

            # expiration year
            if token[0:3] == 'eyr':
                fields_valid = fields_valid and expiration_year_valid(token.split(':')[1])

            # height
            if token[0:3] == 'hgt':
                fields_valid = fields_valid and height_valid(token.split(':')[1])

            # hair colour
            if token[0:3] == 'hcl':
                fields_valid = fields_valid and hair_colour_valid(token.split(':')[1])

            # eye colour
            if token[0:3] == 'ecl':
                fields_valid = fields_valid and eye_colour_valid(token.split(':')[1])

            # passport ID
            if token[0:3] == 'pid':
                fields_valid = fields_valid and passport_id_valid(token.split(':')[1])

        if fields_valid:
            valid_passports += 1

    print(f"valid passports: {valid_passports}")
