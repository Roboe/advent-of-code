const fs = require('fs')
const path = require('path')

const input = fs.readFileSync(path.join(__dirname, 'day04.input.txt'), 'utf-8')

const countPassports = (input) => {
  return input.includes('hgt') && input.includes('byr') ? 1 : 0
}

module.exports = {
  countPassports,
}
