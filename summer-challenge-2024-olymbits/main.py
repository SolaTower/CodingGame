import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

player_idx = int(input())
nb_games = int(input())

print(player_idx, file=sys.stderr, flush=True)
print(nb_games, file=sys.stderr, flush=True)

class GameBase:
    """GameBase"""

    def debug(self):
        output = f"{self.__doc__}\n"
        fill = max([12, max(map(len, self.__dict__.keys()))+2])
        for k, v in self.__dict__.items():
            output += f"{k}:{''.rjust(fill-len(k))}{v}\n"
        print(output, file=sys.stderr, flush=True)

    def game_is_over(self):
        return self._gpu == "GAME_OVER"

    @property
    def _gpu(self):
        return "GAME_OVER"

class HurdleGame(GameBase):
    """HurdleGame"""
    map: str
    me: int
    bg1: int
    bg2: int
    me_stun: int
    bg1_stun: int
    bg2_stun: int
    jump_spots: list = None


    @property
    def _gpu(self):
        return self.map

    def update(self):
        inputs = input().split()
        self.map = inputs[0]
        self.me = int(inputs[1])
        self.bg1 = int(inputs[2])
        self.bg2 = int(inputs[3])
        self.me_stun = int(inputs[4])
        self.bg1_stun = int(inputs[5])
        self.bg2_stun = int(inputs[6])
            


    def get_move(self) -> dict:
        """ Will return a dict of inputs with associated importance (higher importance == most efficient action)"""
        if super().game_is_over():
            return  {"RIGHT": 1, "DOWN": 1, "UP": 1, "LEFT": 1}
        max_view_pos = min([self.me+5,len(self.map)-1])
        max_move_map = self.map[self.me: max_view_pos]
        size = len(max_move_map)
        if size > 3 and max_move_map[3] == "#":
            return {"RIGHT": 1, "DOWN": 1, "UP": 3, "LEFT": 1}
        elif size > 2 and max_move_map[2] == "#":
            return {"RIGHT": 1, "DOWN": 1, "UP": 1, "LEFT": 3}
        elif size > 1 and max_move_map[1] == "#":
            return {"RIGHT": 1, "DOWN": 1, "UP": 3, "LEFT": 1}
        else:
            return {"RIGHT": 3, "DOWN": 2, "UP": 2, "LEFT": 1}


game_obj = HurdleGame()
# game loop
while True:
    next_input_priority = {"RIGHT": 0, "DOWN": 0, "UP": 0, "LEFT": 0}
    for i in range(3):
        score_info = input()
        print(score_info, file=sys.stderr, flush=True)
    for i in range(nb_games):

        game_obj.update()
        game_obj.debug()
        if i > 0:
            continue
        game_input_priority = game_obj.get_move()
        for k, v in game_input_priority.items():
            next_input_priority[k] += v
    print(game_input_priority, file=sys.stderr, flush=True)

    next_input = max(next_input_priority, key=lambda a: next_input_priority[a])
    print(next_input)
