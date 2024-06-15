import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

player_idx = int(input())
nb_games = int(input())

print(player_idx, file=sys.stderr, flush=True)
print(nb_games, file=sys.stderr, flush=True)
class Map:
    map: str
    me: int
    bg1: int
    bg2: int
    me_stun: int
    bg1_stun: int
    bg2_stun: int
    jump_spots: list = None

    def update(self):
        inputs = input().split()
        self.map = inputs[0]
        self.me = int(inputs[1])
        self.bg1 = int(inputs[2])
        self.bg2 = int(inputs[3])
        self.me_stun = int(inputs[4])
        self.bg1_stun = int(inputs[5])
        self.bg2_stun = int(inputs[6])
            

    def debug(self):
        print(self, file=sys.stderr, flush=True)

    def get_move(self):
        max_view_pos = min([self.me+5,len(self.map)-1])
        max_move_map = self.map[self.me: max_view_pos]
        size = len(max_move_map)
        if size > 3 and max_move_map[3] == "#":
            action = 3
        elif size > 2 and max_move_map[2] == "#":
            action = 2
        elif size > 1 and max_move_map[1] == "#":
            action = 1
        else:
            action = 4
        return action

    def __str__(self):
        return f"""
            map: {self.map},
            me: {self.me},
            bg1: {self.bg1},
            bg2: {self.bg2},
            me_stun: {self.me},
            bg1_stun: {self.bg1},
            bg2_stun: {self.bg2},
""" 

game_obj = Map()
# game loop
while True:
    game_loop_actions = []
    for i in range(3):
        score_info = input()
        print(score_info, file=sys.stderr, flush=True)
    for i in range(nb_games):
        game_obj.update()
        game_obj.debug()
        game_loop_actions.append(game_obj.get_move())
    print({
        1: "UP",
        2: "LEFT",
        3: "DOWN",
        4: "RIGHT"
    }[min(game_loop_actions)])
