const { countPassports } = require('./day04.part1.js')

describe('count passports', () => {
  it('counts a single valid passport', () => {
    const inputMagico = `ecl:gry pid:860033327 eyr:2020 hcl:#fffffd
byr:1937 iyr:2017 cid:147 hgt:183cm`

    expect(countPassports(inputMagico)).toEqual(1)
  })
})
