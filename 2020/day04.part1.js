const fs = require('fs')
const path = require('path')

const REQUIRED_FIELDS = ['hgt', 'byr', 'ecl']

const input = fs.readFileSync(path.join(__dirname, 'day04.input.txt'), 'utf-8')

const isValidPassport = passport => {
  for (const field of REQUIRED_FIELDS) {
    if (!passport.includes(field)) return false
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
