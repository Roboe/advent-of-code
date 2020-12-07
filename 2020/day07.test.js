const fs = require('fs')
const path = require('path')
const { checkAvailability, parseRules } = require('./day07.js')

const input = fs.readFileSync(path.join(__dirname, 'day07.input.txt'), 'utf-8')

const exampleInput = `light red bags contain 1 bright white bag, 2 muted yellow bags.
dark orange bags contain 3 bright white bags, 4 muted yellow bags.
bright white bags contain 1 shiny gold bag.
muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
dark olive bags contain 3 faded blue bags, 4 dotted black bags.
vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
faded blue bags contain no other bags.
dotted black bags contain no other bags.`

describe('AoC 7', () => {
    it('parses input', () => {
        const output = {
            "light red": [
                { kind: "bright white", quantity: 1 },
                { kind: "muted yellow", quantity: 2 },
            ],
            "dark orange": [
                { kind: "bright white", quantity: 3 },
                { kind: "muted yellow", quantity: 4 },
            ],
            "bright white": [
                { kind: "shiny gold", quantity: 1 },
            ],
            "muted yellow": [
                { kind: "shiny gold", quantity: 2 },
                { kind: "faded blue", quantity: 9 },
            ],
            "shiny gold": [
                { kind: "dark olive", quantity: 1 },
                { kind: "vibrant plum", quantity: 2 },
            ],
            "dark olive": [
                { kind: "faded blue", quantity: 3 },
                { kind: "dotted black", quantity: 4 },
            ],
            "vibrant plum": [
                { kind: "faded blue", quantity: 5 },
                { kind: "dotted black", quantity: 6 },
            ],
            "faded blue": [],
            "dotted black": [],
        }
        expect(parseRules(exampleInput)).toEqual(output)
    })

    it('counts how much bags can hold a single shiny gold bag', () => {
        expect(checkAvailability(exampleInput, 'shiny gold')).toBe(4)
    })

    it('solves AoC 7 part 1 input', () => {
        expect(checkAvailability(input, 'shiny gold')).toEqual(274)
    })
})
