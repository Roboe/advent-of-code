const fs = require('fs')

const input = fs.readFileSync('./day01.input.txt')
  .toString()
  .split('\n')
  .map(el => Number(el))


const findLastNumber = (quantity, numbers, precedent) => numbers
  .find(number => precedent + number === quantity)

const checkPair = (quantity, numbers) => {
  const [first, ...rest] = numbers
  const second = findLastNumber(quantity, numbers, first)

  return second
    ? [first, second]
    : checkPair(quantity, rest)
}

const checkTrio = (quantity, numbers) => {
  const [first, ...rest] = numbers
  const possibleSecond = rest.filter(number => number + first < quantity)
  const trio = possibleSecond
    .reduce((acc, second) => {
      const third = findLastNumber(
        quantity,
        numbers.filter(num => num !== second),
        first + second,
      )

      return third
      ? [first, second, third]
      : acc
  }, undefined)

  return trio
    ? trio
    : checkTrio(quantity, rest)
}

const multiply = (...numbers) => numbers
  .reduce((accumulator, number) => accumulator * number)

const outputPart1 = checkPair(2020, input)
console.log(
  'Part1: ',
  outputPart1,
  multiply(...outputPart1),
)

const outputPart2 = checkTrio(2020, input)
console.log(
  'Part2: ',
  outputPart2,
  multiply(...outputPart2),
)
