const fs = require('fs')
const path = require('path')
const { countPassports, VALIDATE_FIELDS: validations} = require('./day04.part2.js')

const input = fs.readFileSync(path.join(__dirname, 'day04.input.txt'), 'utf-8')

const allInvalidInput = `eyr:1972 cid:100
hcl:#18171d ecl:amb hgt:170 pid:186cm iyr:2018 byr:1926

iyr:2019
hcl:#602927 eyr:1967 hgt:170cm
ecl:grn pid:012533040 byr:1946

hcl:dab227 iyr:2012
ecl:brn hgt:182cm pid:021572410 eyr:2020 byr:1992 cid:277

hgt:59cm ecl:zzz
eyr:2038 hcl:74454a iyr:2023
pid:3556412378 byr:2007`

const allValidInput = `pid:087499704 hgt:74in ecl:grn iyr:2012 eyr:2030 byr:1980
hcl:#623a2f

eyr:2029 ecl:blu cid:129 byr:1989
iyr:2014 pid:896056539 hcl:#a97842 hgt:165cm

hcl:#888785
hgt:164cm byr:2001 iyr:2015 cid:88
pid:545766238 ecl:hzl
eyr:2022

iyr:2010 hgt:158cm hcl:#b6652a ecl:blu byr:1944 eyr:2021 pid:093154719`


describe('field validation AoC part 2', () => {
  [
    { field: 'byr', valid: true , value: '2002' },
    { field: 'byr', valid: false, value: '2003' },
    { field: 'hgt', valid: true , value: '60in' },
    { field: 'hgt', valid: true , value: '190cm' },
    { field: 'hgt', valid: false, value: '190in' },
    { field: 'hgt', valid: false, value: '190' },
    { field: 'hcl', valid: true , value: '#123abc' },
    { field: 'hcl', valid: false, value: '#123abz' },
    { field: 'hcl', valid: false, value: '123abc' },
    { field: 'ecl', valid: true , value: 'brn' },
    { field: 'ecl', valid: false, value: 'wat' },
    { field: 'pid', valid: true , value: '000000001' },
    { field: 'pid', valid: false, value: '0123456789' },
  ].forEach(({ field, value, valid }) => {
    it(`correctly validates ${field} with value ${value}`, () => {
      expect(validations[field](value)).toBe(valid)
    })
  })
})

describe('count passports AoC 4 part 2', () => {
  it('does not count invalid passports', () => {
    expect(countPassports(allInvalidInput)).toEqual(0)
  })

  it('counts valid passports', () => {
    expect(countPassports(allValidInput)).toEqual(4)
  })

  it('solves AoC 4 input', () => {
    expect(countPassports(input)).toEqual(140)
  })
})
