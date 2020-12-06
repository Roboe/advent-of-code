// https://adventofcode.com/2020/day/4#part2

const every = validations => value => validations.every(v => v(value))

const isRequired = value => value !== undefined

const fixedLength = length => value => value.length === length

const VALIDATE_FIELDS = {
  byr: every([
    isRequired,
    fixedLength(4),
    value => /\d{4}/.test(value)
      && value >= '1920'
      && value <= '2002',
  ]),
  cid: value => true,
  iyr: every([
    isRequired,
    fixedLength(4),
    value => /\d{4}/.test(value)
    && value >= '2010'
    && value <= '2020',
  ]),
  eyr: every([
    isRequired,
    fixedLength(4),
    value => /\d{4}/.test(value)
    && value >= '2020'
    && value <= '2030',
  ]),
  hgt: every([
    isRequired,
    value => /\d+(cm|in)/.test(value),
    value => {
      const [, number, units] = value.match(/(\d+)(cm|in)/)
      if (units === 'cm' && (number < '150' || number > '193')) return false
      if (units === 'in' && (number < '59' || number > '76')) return false
      return true
    }
  ]),
  hcl: every([
    isRequired,
    fixedLength(7),
    value => /#[0-9a-f]{6}/.test(value),
  ]),
  ecl: every([
    isRequired,
    value => ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'].includes(value),
  ]),
  pid: every([
    isRequired,
    fixedLength(9),
    value => /\d{9}/.test(value),
  ]),
}

const parsePassport = rawPassport => {
  const entries = rawPassport
    .split(/\s/)
    .map(field => field.split(':'))
  return Object.fromEntries(entries)
}

const isValidPassport = passport => Object.entries(VALIDATE_FIELDS)
  .every(([field, validate]) => validate(passport[field]))

const countPassports = (input) => input
  .split('\n\n')
  .map(parsePassport)
  .filter(isValidPassport)
  .length

module.exports = {
  countPassports,
  VALIDATE_FIELDS,
}
