#!/usr/bin/env python3
import random
import string

state_of_play = ["0"]*100
remaining_choices = set(range(100))

target = None

def coord_to_index(coords):
    letter = coords[0].upper()
    return string.ascii_uppercase.index(letter)*10 + int(coords[1]) - 1

def index_to_coord(index):
    letter = string.ascii_uppercase[index % 10]
    return letter + str((index // 10) + 1)

def take_a_punt():
    choice = random.choice(list(remaining_choices))
    print(index_to_coord(choice))
    remaining_choices.remove(choice)
    return choice

def did_we_hit(choice):
    global target
    result = input()
    if result == 'h':
        target = choice
    elif result == 's':
        target = None
    state_of_play[choice] = result

def ai_shot():
    valid_targets = set()
    if target > 9:
        valid_targets.add(target - 10)
    if target % 10:
        valid_targets.add(target + 1)
    if target -1 % 10:
        valid_targets.add(target - 1)
    if target < 90:
        valid_targets.add(target + 10)
    probable_targets = list(remaining_choices & valid_targets)
    if not probable_targets: return take_a_punt()
    choice = random.choice(probable_targets)
    print(index_to_coord(choice))
    remaining_choices.remove(choice)
    return choice

def play_battleships():
    while True:
        # print("target: {0}".format(target))
        if target:
            choice = ai_shot()
        else:
            choice = take_a_punt()
        did_we_hit(choice)
        # debug_print()

def debug_print():
    for i in range(0, 90, 10):
        print("".join(state_of_play[i: i + 10]))

if __name__=='__main__':
    play_battleships()
