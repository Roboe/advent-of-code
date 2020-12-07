const ADJ_CLR_BAG = /(\w+ \w+) bags/
const QTY_ADJ_CLR_BAG = /(\d+) (\w+ \w+) bags?/
const NO_OTHER_BAGS = /no other bags/

const parseContent = rawContent => rawContent
    .filter(line => !NO_OTHER_BAGS.test(line))
    .map(line => {
        const [, quantity, kind] = line.match(QTY_ADJ_CLR_BAG)
        return {
            kind,
            quantity: Number(quantity),
        }
    })

const parseRules = input => input.split(/\.\n/)
    .reduce((rules, line) => {
        if (!line) return rules

        const [rawTarget, ...rawContent] = line.split(/ contain |, /)
        const [, kind] = rawTarget.match(ADJ_CLR_BAG)
        const content = parseContent(rawContent)

        return {
            ...rules,
            [kind]: content,
        }
    }, {})

const canContain = (rules, outKind, wantedKind) => {
    const contents = rules[outKind]
    if (contents === undefined) return false

    const canContainDirectly = contents
        .find(contentEntry => contentEntry.kind === wantedKind)

    return canContainDirectly || contents
        .find(contentEntry => canContain(rules, contentEntry.kind, wantedKind))
}

const checkAvailability = (input, kind) => {
    const rules = parseRules(input)
    return Object.keys(rules)
        .filter(outKind => canContain(rules, outKind, kind))
        .length
}

module.exports = {
    parseRules,
    checkAvailability,
}
