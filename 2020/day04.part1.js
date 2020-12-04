const fs = require('fs')
const path = require('path')

const input = fs.readFileSync(path.join(__dirname, 'day04.input.txt'), 'utf-8')

const countPassports = () => {
  return 1
}

module.exports = {
  countPassports,
}
