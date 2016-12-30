from strutils import count, contains, split, strip

const vowels = {'a', 'e', 'i', 'o', 'u'}
const badStrs = ["ab", "cd", "pq", "xy"]
const inputs = readFile("in.txt").strip().split()

proc hasEnoughVowels(str: string): bool = str.count(vowels) >= 3


proc hasDoubles(str: string): bool =
    var lastChar = str[0]
    for ch in str[1..^1]:
        if ch == lastChar:
            return true
        lastChar = ch
    return false


proc containsBadStrs(str: string): bool =
    for badStr in badStrs:
        if str.contains(badStr):
            return true
    return false


proc isNice(str: string): bool =
    hasEnoughVowels(str) and hasDoubles(str) and (containsBadStrs(str) == false)


proc part1: int =
    var niceCount: int
    for input in inputs:
        if input.isNice:
            niceCount += 1
    return niceCount


proc hasDoublePairs(str: string): bool =
    for i in countup(1, str.len - 1):
        if str[i+1..^1].count(str[i-1..i]) > 0:
            return true
    return false


proc hasSandwich(str: string): bool =
    var cmpChar = str[0]
    var lastChar = str[1]
    for ch in str[2..^1]:
        if ch == cmpChar:
            return true
        cmpChar = lastChar
        lastChar = ch
    return false


proc isNice2(str: string): bool =
    hasDoublePairs(str) and hasSandwich(str)


proc part2: int =
    var niceCount: int
    for input in inputs:
        if input.isNice2:
            niceCount += 1
    return niceCount


echo "Part 1: ", part1()
echo "Part 2: ", part2()
