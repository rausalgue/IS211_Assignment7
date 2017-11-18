#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Assignemnt Week Seven - Pig Game"""

import random
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--name", help="Name of the Player",default=None)
args = parser.parse_args()

class Dice(object):
    def __init__(self):
        self.value = None

    def roll(self):
        self.value = random.randint(1, 6)
        return self.value

class PlayerData():
    def __init__(self,name):
        self.name = name
        self.score = 0

class Game():
    def __init__(self, value1, value2):  # Assign method name
        self.player1 = value1
        self.player2 = value2
        self.playerSlot = 1

    def introducePlayers(self):
        player1 = PlayerData(self.player1)
        player2 = PlayerData(self.player2)

        return player1,player2

    def rollDice(self,playerIteration):
        print 'rolling...'
        print 'PLayer Iteration',playerIteration
        gameDice = Dice()
        roll_value = gameDice.roll()
        print 'roll value:',roll_value

def main():
    # Call the Game Class to begin Game

    print 'Welcome to Our Game'

    player_one = args.name if args.name else raw_input("Please enter name of first player: ")

    if player_one:
        player_two = args.name if args.name else raw_input("Please enter name of second player: ")

    if player_one and player_two:
        print 'Thanks for Playing', player_one,'and',player_two
        game = Game(player_one,player_two)

        player1,player2= game.introducePlayers()

        print 'Player 1:',player1.name, 'has score:',player1.score
        print 'Player 2:', player2.name, 'has score:', player2.score

        #while player1.score < 100 and player2.score < 100:

        print 'Player Slot:',game.playerSlot

        game.rollDice(game.playerSlot)

        if player1.score >= 100:
            print "player 1 wins"
            #break

        if player2.score >= 100:
            print "player 2 wins"
            #break



    print 'Game has terminated...Play Again (y/n):...'



if __name__ == '__main__':
    main()
