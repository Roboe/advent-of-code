const fs = require('fs')
const path = require('path')
const { countPassports } = require('./day4.part2.js')

const input = fs.readFileSync(path.join(__dirname, 'day4.input.txt'), 'utf-8')

describe('count passports AoC 4 part 2', () => {
  it('does not count an invalid passport (invalid hgt)', () => {
    const inputMagico = `eyr:1972 cid:100
hcl:#18171d ecl:amb hgt:170 pid:123456789 iyr:2018 byr:1926`

    expect(countPassports(inputMagico)).toEqual(0)
  })
})
