def solve_cryptarithm(words, result):
    letters = set("".join(words) + result)
    if len(letters) > 10:
        return []
    leading = {word[0] for word in words + [result]}
    ordered_letters = sorted(letters, key=lambda letter: letter not in leading)
    solutions = []

    def value(word, mapping):
        return sum(mapping[letter] * 10 ** index
                   for index, letter in enumerate(reversed(word)))

    def search(index, mapping, used):
        if index == len(ordered_letters):
            if sum(value(word, mapping) for word in words) == value(result, mapping):
                solutions.append(mapping.copy())
            return
        letter = ordered_letters[index]
        for digit in range(10):
            if digit in used or (digit == 0 and letter in leading):
                continue
            mapping[letter] = digit
            search(index + 1, mapping, used | {digit})
            del mapping[letter]

    search(0, {}, set())
    return solutions


count = int(input("Enter number of addend words: "))
words = [input("Enter addend word " + str(index + 1) + ": ").strip().upper()
         for index in range(count)]
result = input("Enter result word: ").strip().upper()
solutions = solve_cryptarithm(words, result)

if not solutions:
    print("No solution exists.")
else:
    print("Solutions found:", len(solutions))
    for mapping in solutions[:5]:
        print("Mapping:", mapping)
        print(" + ".join(str(sum(mapping[letter] * 10 ** power
                                for power, letter in enumerate(reversed(word))))
                         for word in words))
        print("=", sum(mapping[letter] * 10 ** power
                        for power, letter in enumerate(reversed(result))))
