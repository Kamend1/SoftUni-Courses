from project.player import Player
from project.team import Team

p = Player("Paul", 3, 3, 3, 3)
t = Team("Test", 100)

print(t.add_player(p))
print(t.remove_player("Paul"))
