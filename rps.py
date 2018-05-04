# -*- coding: utf-8 -*-
"""
Created on Wed May  2 22:06:37 2018

@author: Imani
"""
allowed_moves = ['rock','paper','scissors']
player1 = input ('Player 1 enter move: ');
player2 = input ('Player 2 enter move: ');

if player1 == player2:
    print("player 1? " + player1)
    print("player 2? " + player2)
    print ('Its a draw')
elif player1=='rock':
    if  player2=='paper':
        print("player 1? " + player1)
        print("player 2? " + player2)
        print('Player 2 wins')
        
elif player1=='paper':
    if  player2=='scissors':
        print("player 1? " + player1)
        print("player 2? " + player2)
        print('Player 2 wins')
        
elif player1=='rock':
    if  player2=='scissors':
        print("player 1? " + player1)
        print("player 2? " + player2)
        print('Player 1 wins')
        
elif player1=='paper':
    if  player2=='rock':
        print("player 1? " + player1)
        print("player 2? " + player2)
        print('Player 1 wins')
        
elif player1=='scissors':
    if  player2=='paper':
        print("player 1? " + player1)
        print("player 2? " + player2)
        print('Player 1 wins')
        
elif player1=='scissors':
    if  player2=='rock':
        print("player 1? " + player1)
        print("player 2? " + player2)
        print('Player 2 wins') 
        
elif player1 or player2 != allowed_moves:
    print('This is not a valid move')
        

    