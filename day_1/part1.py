part1_example = """\
1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet
"""


def get_number(line: str):
    # find first and last digit
    first = -1
    last = -1
    for c in line:
        d = ord(c) - ord('0')
        if 0 <= d <= 9:  # is digit
            if first == -1 and last == -1:
                first = d
                last = d
            else:
                last = d
            # print(d, end='')
    # print()
    # print(first, last)
    return first * 10 + last


if __name__ == '__main__':
    ans = 0

    # lines = part1_example.splitlines()
    # for line in lines:
    #     ans += get_number(line)

    with open('day_1/input', 'r') as f:
        for line in f:
            ans += get_number(line)

    print(ans)
