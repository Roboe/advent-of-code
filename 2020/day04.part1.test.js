const fs = require('fs')
const path = require('path')
const { countPassports } = require('./day04.part1.js')

const input = fs.readFileSync(path.join(__dirname, 'day04.input.txt'), 'utf-8')

describe('count passports AoC 4 part 1', () => {
  it('counts a single valid passport', () => {
    const inputMagico = `ecl:gry pid:860033327 eyr:2020 hcl:#fffffd
byr:1937 iyr:2017 cid:147 hgt:183cm`

    expect(countPassports(inputMagico)).toEqual(1)
  })

  it('does not count invalid passports (missing hgt)', () => {
    const inputMagico = `iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884
hcl:#cfa07d byr:1929`

    expect(countPassports(inputMagico)).toEqual(0)
  })

  it('does not count invalid passports (missing ecl)', () => {
    const inputMagico = `pid:860033327 eyr:2020 hcl:#fffffd
byr:1937 iyr:2017 cid:147 hgt:183cm`

    expect(countPassports(inputMagico)).toEqual(0)
  })


  it('does not count invalid passports (missing byr)', () => {
    const inputMagico = `hcl:#cfa07d eyr:2025 pid:166559648
iyr:2011 ecl:brn hgt:59in`

    expect(countPassports(inputMagico)).toEqual(0)
  })

  it('counts two valid passports', () => {
    const inputMagico = `ecl:gry pid:860033327 eyr:2020 hcl:#fffffd
byr:1937 iyr:2017 cid:147 hgt:183cm

hcl:#ae17e1 iyr:2013
eyr:2024
ecl:brn pid:760753108 byr:1931
hgt:179cm`

    expect(countPassports(inputMagico)).toEqual(2)
  })

  it('counts two valid passports with one invalid', () => {
    const inputMagico = `ecl:gry pid:860033327 eyr:2020 hcl:#fffffd
byr:1937 iyr:2017 cid:147 hgt:183cm

hcl:#cfa07d eyr:2025 pid:166559648
iyr:2011 ecl:brn hgt:59in

hcl:#ae17e1 iyr:2013
eyr:2024
ecl:brn pid:760753108 byr:1931
hgt:179cm`

    expect(countPassports(inputMagico)).toEqual(2)
  })

  it('solves AoC 4 input', () => {
    expect(countPassports(input)).toEqual(222)
  })

})
