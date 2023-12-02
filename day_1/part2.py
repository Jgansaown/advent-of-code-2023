
part2_example = """\
two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen
"""


str_digits = ['zero', 'one', 'two', 'three',
              'four', 'five', 'six', 'seven', 'eight', 'nine']
"""
o -> n -> e
t -> w -> o
    -> h -> r -> e -> e
f -> o -> u -> r
    -> i -> v -> e
s -> i -> x
    -> e -> v -> e -> n
e -> i -> g -> h -> t
n -> i -> n -> e
"""

prefix = {}
for digit, str_digit in enumerate(str_digits):
    for i in range(1, len(str_digit)):
        prefix[str_digit[:i]] = -1
    prefix[str_digit] = digit
for i in range(10):
    prefix[str(i)] = i
print(prefix)


def find_digit(line: str, start: int) -> int:
    n = 1

    while start+n <= len(line) and line[start:start+n] in prefix and prefix[line[start:start+n]] == -1:
        n += 1

    if line[start:start+n] in prefix and prefix[line[start:start+n]] >= 0:
        return prefix[line[start:start+n]]
    return -1


if __name__ == '__main__':
    ans = 0

    # oneight -> 1 & 8

    # lines = part2_example.splitlines()
    # for line in lines:
    #     # print(line)
    #     first = -1
    #     last = -1

    #     for i in range(len(line)):
    #         digit = find_digit(line, i)
    #         if digit > -1:
    #             if first == -1:
    #                 first = digit
    #                 last = digit
    #             else:
    #                 last = digit
    #     ans += first * 10 + last

    with open('day_1/input.txt', 'r') as f:
        for line in f:
            first = -1
            last = -1
            for i in range(len(line)):
                digit = find_digit(line, i)
                if digit > -1:
                    if first == -1:
                        first = digit
                        last = digit
                    else:
                        last = digit
            ans += first * 10 + last

    print(ans)
