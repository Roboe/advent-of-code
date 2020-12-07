// https://adventofcode.com/2020/day/6

const fs = require('fs')
const path = require('path')

const input = fs.readFileSync(
    path.join(__dirname, 'day06.input.txt'),
    'utf-8',
).trimEnd()

const exampleInput = `abc

a
b
c

ab
ac

a
a
a
a

b`

const countReplies = (reply, answers) =>
    answers.match(new RegExp(reply, 'g')).length

const countGroupAnswers = groupAnswers => {
    const participants = groupAnswers.split('\n').length
    const allAnswers = groupAnswers.replace(/\s/g, '')
    const differentReplies = [...new Set(allAnswers)]

    return differentReplies
        .filter(reply => countReplies(reply, allAnswers) === participants)
        .length
}

const sumAllGroupsAnswers = input => {
    const groupsAnwers = input.split('\n\n')
    const groupCounts = groupsAnwers.map(countGroupAnswers)
    return groupCounts.reduce((acc, answers) => acc + answers)
}


describe('AoC 7', () => {
    it('count group answers (two lines)', () => {
        const groupAnswers = `ab
ac`
        expect(countGroupAnswers(groupAnswers)).toBe(1)
    })
    it('count group answers (three lines)', () => {
        const groupAnswers = `a
b
c`
        expect(countGroupAnswers(groupAnswers)).toBe(0)
    })

    it('sum counts of example input', () => {
        expect(sumAllGroupsAnswers(exampleInput)).toBe(6)
    })

    it('solves AoC 6 part 2', () => {
        expect(sumAllGroupsAnswers(input)).toBe(3427)
    })
})
