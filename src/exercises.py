player = {"name" : "Mohamed", "score" : 100}

scores = [100, 90, 80, 70, 60,50,40,30,20,10]

high_scores = []

for s in scores:
    if s >= 50:
        high_scores.append(s)

print(high_scores)

from dataclasses import dataclass
from pydoc import text

@dataclass
class Player:
    name: str
    score: int


def top(players: list[Player]) -> Player:
    return max(players, key=lambda player: player.score)


roster = [Player("Mohamed", 100), Player("Ali", 90), Player("Ahmed", 80)]

best = top(roster)
print(best.name, best.score)


try:
    text = open("notes.txt", encoding="utf-8").read()
    print(text)
except FileNotFoundError:
    print("File not found")
