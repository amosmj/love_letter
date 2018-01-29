#!/usr/bin/env python

"""
This is my attempt at building and OOP Love Letter Simulator
Apologies to AEG who created and sell Love Letter and it's many variants
It is not my intention that this should replace buying a physical copy of
Love Letter for anyone. Instead I am doing this to improve my coding skills
and to try and test my theory that Love Letter is very nearly random
"""


import itertools
import game

print("Welcome to Love Letter Simulator")
# this following section works if a human actually
# wants to key in everything
# commenting out because I don't want to do that
# most of the time
'''
player_count = input("how many players? ")
players = []
for player in range(int(player_count)):
    player_name = input("input player name: ")
    players.append(Player(player_name))
'''
# This next line does all of the stuff above but just
# forces the players to be a fixed set
newGame = game.Game("Alice", "Bob", "Carol")
print(newGame)

while newGame.take_turn():
    print(newGame)

print("The Game is Over")
