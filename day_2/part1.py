from pathlib import Path
from typing import Iterable


example = """\
Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green
"""

def game_possible(bag, rounds: str):
    rounds = [
        [color.split(' ') for color in rounds.split(', ')]
        for rounds in rounds.split('; ')
    ]

    for grabbed in rounds:
        for count, color in grabbed:
            if int(count) > bag[color]:
                return False
    return True


def solution(lines: Iterable[str]):
    ans = 0

    # only 12 red cubes, 13 green cubes, and 14 blue cubes
    # bag = [12, 13, 14]  # red, green, blue
    bag = {'red': 12, 'green': 13, 'blue': 14}

    for i, line in enumerate(lines):
        game, rest = line.strip().split(': ', maxsplit=1)
        
        if game_possible(bag, rest):
            ans += i + 1

    print(ans)

if __name__ == '__main__':

    solution(example.splitlines(keepends=True))

    with open(f'{Path(__file__).parent.name}/input.txt') as f:
        solution(f)
