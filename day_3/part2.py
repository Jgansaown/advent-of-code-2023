from pathlib import Path
from typing import Iterable, Optional, Tuple


example = """\
467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..
"""


def find_number(lines: list[str], M: int, N: int, i: int, j: int) -> Optional[Tuple[int, int, int]]:
    """Expand left and right to find number"""
    if not lines[i][j].isdigit():
        return None

    start = j
    end = j
    while 0 <= start and lines[i][start].isdigit():
        start -= 1
    while end < N and lines[i][end].isdigit():
        end += 1

    return (i, start+1, end-1)


def find_gear_ratio(lines: list[str], M: int, N: int, i: int, j: int):
    diff = [(-1, -1), (-1, 0), (-1, 1),
            (0, -1), (0, 0), (0, 1),
            (1, -1), (1, 0), (1, 1)]

    numbers = set()
    for di, dj in diff:
        if not (0 <= i+di < M and 0 <= j+dj < N):
            continue
        ret = find_number(lines, M, N, i+di, j+dj)
        if ret is not None:
            numbers.add(ret)
    # print(numbers, len(numbers))

    if len(numbers) != 2:
        return

    ratio = 1
    for row, start, end in numbers:
        ratio *= int(lines[row][start:end+1])
    return ratio


def solution(lines: Iterable[str]):
    lines = [line.strip() for line in lines]
    M, N = len(lines), len(lines[0])

    ans = 0
    for i in range(M):
        for j in range(N):
            if lines[i][j] == '*':
                ratio = find_gear_ratio(lines, M, N, i, j)
                if ratio is not None:
                    ans += ratio
    print(ans)


if __name__ == '__main__':

    solution(example.splitlines(keepends=True))

    with open(f'{Path(__file__).parent.name}/input.txt') as f:
        solution(f)
