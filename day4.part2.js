const REQUIRED_FIELDS = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']


const isValidPassport = passport => {
  for (const field of REQUIRED_FIELDS) {
    if (!passport.includes(field)) return false
    if (field === 'hgt' && !/\d+(cm|in)/.test(passport)) return false
  }
  return true
}

const countPassports = (input) => {
  const passports = input.split('\n\n')

  return passports.filter(isValidPassport).length
}

module.exports = {
  countPassports,
}
