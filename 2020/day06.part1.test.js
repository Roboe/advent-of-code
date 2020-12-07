const fs = require('fs')
const path = require('path')

const input = fs.readFileSync(path.join(__dirname, 'day06.input.txt'), 'utf-8')

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

const countGroupAnswers = groupAnswers =>
    new Set(groupAnswers.replace(/\s/g, '')).size

const sumAllGroupsAnswers = input => {
    const groupsAnwers = input.split('\n\n')
    const groupCounts = groupsAnwers.map(countGroupAnswers)
    return groupCounts.reduce((acc, answers) => acc + answers)
}


describe('AoC 7', () => {
    it('count group answers (two lines)', () => {
        const groupAnswers = `ab
ac`
        expect(countGroupAnswers(groupAnswers)).toBe(3)
    })
    it('count group answers (three lines)', () => {
        const groupAnswers = `a
b
c`
        expect(countGroupAnswers(groupAnswers)).toBe(3)
    })

    it('sum counts of example input', () => {
        expect(sumAllGroupsAnswers(exampleInput)).toBe(11)
    })

    it('solves AoC 6 part 1', () => {
        expect(sumAllGroupsAnswers(input)).toBe(6532)
    })
})
