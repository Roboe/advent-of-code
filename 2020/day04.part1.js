const fs = require('fs')
const path = require('path')

const input = fs.readFileSync(path.join(__dirname, 'day04.input.txt'), 'utf-8')

const countPassports = (input) => {
  const passports = input.split('\n\n')

  return (passports[0].includes('hgt') && passports[0].includes('byr') ? 1 : 0)
    + (passports[1] !== undefined && passports[1].includes('hgt') && passports[1].includes('byr') ? 1 : 0)
}

module.exports = {
  countPassports,
}
