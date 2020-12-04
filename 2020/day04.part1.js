const fs = require('fs')
const path = require('path')

const input = fs.readFileSync(path.join(__dirname, 'day04.input.txt'), 'utf-8')

const isValidPassport = passport => passport.includes('hgt') && passport.includes('byr')

const countPassports = (input) => {
  const passports = input.split('\n\n')

  return (isValidPassport(passports[0]) ? 1 : 0)
    + (passports[1] !== undefined && isValidPassport(passports[1]) ? 1 : 0)
}

module.exports = {
  countPassports,
}
