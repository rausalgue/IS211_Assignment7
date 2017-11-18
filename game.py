#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Assignemnt Week Seven - Pig Game"""

import random
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--name", help="Name of the Player",default=None)
args = parser.parse_args()

upper_limit = 20

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

    def introducePlayers(self):
        player1 = PlayerData(self.player1)
        player2 = PlayerData(self.player2)

        return player1,player2

    def rollDice(self,player):
        print 'Rolling [.].[.].[.]'
        print 'Player Data',player.name,'Current Score:',player.score

        gameDice = Dice()

        current_roll_value = 0

        print 'Score',player.score
        temp_player_score = player.score
        print 'Temp Score', temp_player_score

        while True:
            roll_value = gameDice.roll()
            current_roll_value = current_roll_value + roll_value

            if roll_value == 1:
                print 'Sorry',player.name,'you rolled a 1'
                return
            else:
                temp_player_score += roll_value

                if temp_player_score >= upper_limit:
                    player.score += current_roll_value
                else:
                    print 'Congrats',player.name,'you rolled:',roll_value,'your temp score is',temp_player_score
                    print 'What would you like to do?'
                    answer = raw_input("Roll(r) or Hold(h): ")
                    if answer == 'h':
                        player.score += current_roll_value
                        break
                    else:
                        continue
        return

def main():
    # Call the Game Class to begin Game

    print 'Welcome to Our Game'

    player_one = args.name if args.name else raw_input("Please enter name of first player: ")

    if player_one:
        player_two = args.name if args.name else raw_input("Please enter name of second player: ")

    if player_one and player_two:
        game = Game(player_one,player_two)

        player1,player2= game.introducePlayers()

        while player1.score < upper_limit and player2.score < upper_limit:
            roll = game.rollDice(player1)

            if player1.score >= upper_limit:
                print "player 1 wins"
                break
            roll = game.rollDice(player2)

            if player2.score >= upper_limit:
                print "player 2 wins"
                break

        print 'Final Results'
        print 'Player:',player1.name,'Score:',player1.score
        print 'Player:', player2.name, 'Score:', player2.score



    print 'Game has terminated...Play Again (y/n):...'

if __name__ == '__main__':
    main()
