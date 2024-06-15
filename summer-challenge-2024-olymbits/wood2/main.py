import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

player_idx = int(input())
nb_games = int(input())

# game loop
while True:
    for i in range(3):
        score_info = input()
    for i in range(nb_games):
        inputs = input().split()
        gpu = inputs[0]+"...."
        reg_0 = int(inputs[1])
        reg_1 = int(inputs[2])
        reg_2 = int(inputs[3])
        reg_3 = int(inputs[4])
        reg_4 = int(inputs[5])
        reg_5 = int(inputs[6])
        reg_6 = int(inputs[7])
        if gpu.startswith('.'):
            if gpu[reg_0+1] == "#":
                print("UP")
            elif gpu[reg_0+2] == "#":
                print("LEFT")
            elif gpu[reg_0+3] == "#":
                print("DOWN")
            else:
                print("RIGHT")
        else:
                print("RIGHT")
