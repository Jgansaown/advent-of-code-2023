from pathlib import Path
from typing import Iterable


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


def is_part_number(lines, m, n, row, start, end):
    for x in range(row-1, row+1+1):
        for y in range(start-1, end+1+1):
            if not (0 <= x < m and 0 <= y < n):  # out of bound
                continue
            if x == row and start <= y <= end:  # skip digits
                continue
            if lines[x][y] != '.':
                return True
    return False


def solution(lines: Iterable[str]):
    lines = [line.strip() for line in lines]
    M, N = len(lines), len(lines[0])

    numbers = []
    for i in range(M):
        j = 0
        while j < N:
            while j < N and not lines[i][j].isdigit():
                j += 1
            start = j
            while j < N and lines[i][j].isdigit():
                j += 1
            end = j

            if 0 <= start < end <= N and is_part_number(lines, M, N, i, start, end-1):
                numbers.append(int(lines[i][start:end]))
    print(sum(numbers))


if __name__ == '__main__':

    solution(example.splitlines(keepends=True))

    with open(f'{Path(__file__).parent.name}/input.txt') as f:
        solution(f)
