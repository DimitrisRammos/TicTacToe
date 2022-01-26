from cProfile import run
from cgitb import grey
import imp
import math
from random import random
from time import sleep
from turtle import Screen, width
from xml.dom.minidom import Element
import pygame
import random
from tic import *


#if the game is tie
#check it
def tie_game( board):
    for i in range(3):
        List = board[i]
        for j in range(3):
            element, pos = List[j]
            if element == None:
                return False
    return True

#check if i have winner
#return 100 if the winner is the O
#return -100 if the winner is ths X
#return 0 if the game is tie-game
def check_for_win( board):
    
    #check first line
    List = board[0]
    i0, pos1 = List[0]
    i1, pos2 = List[1]
    i2, pos3 = List[2]
    
    if( i0 == "X" and i1 == "X" and i2 == "X"):
        return -100

    elif( i0 == "O" and i1 == "O" and i2 == "O"):
        return 100

    #check second line
    List = board[1]
    i0, pos1 = List[0]
    i1, pos2 = List[1]
    i2, pos3 = List[2]

    if( i0 == "X" and i1 == "X" and i2 == "X"):
        return -100
    
    elif( i0 == "O" and i1 == "O" and i2 == "O"):
        return 100

    #check third line
    List = board[2]
    i0, pos1 = List[0]
    i1, pos2 = List[1]
    i2, pos3 = List[2]
    if( i0 == "X" and i1 == "X" and i2 == "X"):
        return -100
    
    elif( i0 == "O" and i1 == "O" and i2 == "O"):
        return 100
    
    
    List_1 = board[0]
    i0_1, pos1_1 = List_1[0]
    i1_1, pos2_1 = List_1[1]
    i2_1, pos3_1 = List_1[2]
    
    List_2 = board[1]
    i0_2, pos1_2 = List_2[0]
    i1_2, pos2_2 = List_2[1]
    i2_2, pos3_2 = List_2[2]
    
    List_3 = board[2]
    i0_3, pos1_3 = List_3[0]
    i1_3, pos2_3 = List_3[1]
    i2_3, pos3_3 = List_3[2]


    #check first katheti-line
    if( i0_1 == "X" and i0_2 == "X" and i0_3 == "X"):
        return -100
    
    elif( i0_1 == "O" and i0_2 == "O" and i0_3 == "O"):
        return 100
    
    #check second katheti-line
    if(i1_1 == "X" and i1_2 == "X" and i1_3 == "X"):
        return -100
        
    elif( i1_1 == "O" and i1_2 == "O" and i1_3 == "O"):
        return 100
        
    #check third katheti-line
    if( i2_1 == "X" and i2_2 == "X" and i2_3 == "X"):
        return -100
        
    elif( i2_1 == "O" and i2_2 == "O" and i2_3 == "O"):
        return 100
    
    
    #check the first side-line
    if( i0_1 == "X" and i1_2 == "X" and i2_3 == "X"):
        return -100
    
    elif( i0_1 == "O" and i1_2 == "O" and i2_3 == "O"):
        return 100
    
    #check the second side-line
    if( i2_1 == "X" and i1_2 == "X" and i0_3 == "X"):
        return -100
    
    elif( i2_1 == "O" and i1_2 == "O" and i0_3 == "O"):
        return 100
    
    return 0        

#minimax algorithmic fot the playe
def minimax( board, depth, Max_player):
    
    score = check_for_win( board)
    #if the max win(O player)
    if score == 100:
        return score
    #if the max lose
    if score == -100:
        return score
    
    #if i have tie-game
    if tie_game( board) == True:
        return 0
    
    #The algorithick
    if( Max_player):
        best = -math.inf
        for i in range(3):
            List = board[i]
            for j in range(3):
                element, pos = List[j]
                if element == None:
                    
                    element = "O"
                    List[j] = (element, pos)
                    board[i] = List
                    
                    best = max( best, minimax( board, depth+1, not Max_player))
                    
                    element = None
                    List[j] = (element,pos)
                    board[i] = List
    
        return best
    else:
        best = math.inf
        for i in range(3):
            List = board[i]
            for j in range(3):
                element, pos = List[j]
                if element == None:
                    
                    element = "X"
                    List[j] = (element, pos)
                    board[i] = List
                    
                    best = min( best, minimax( board, depth+1, not Max_player))
                    
                    element = None
                    List[j] = (element,pos)
                    board[i] = List
    
        return best
  
#start the algorithmic for all squares and call the minimax algoritmic      
def BestMove( board):
    best = -math.inf
    bestmove = (-1,-1)
    for i in range(3):
        List = board[i]
        for j in range(3):
            element, pos = List[j]
            if element == None:
                
                element = "O"
                List[j] = (element, pos)
                board[i] = List
                
                evaluate_price = minimax( board, 0, False)
                
                element = None
                List[j] = (element,pos)
                board[i] = List
                
                if evaluate_price > best:
                    best = evaluate_price
                    bestmove = (i,j)                
                
    return bestmove

#for easy game
#Th computer-machine play with rand but
#if computer can to take the win with one move then play the best move
def RandMove( board):
    
    for i in range(3):
        List = board[i]
        for j in range(3):
            element, pos = List[j]
            if element == None:
                element = "O"
                List[j] = (element, pos)
                board[i] = List
                
                score = check_for_win( board)
                
                
                element = None
                List[j] = (element,pos)
                board[i] = List
                
                if score == 100:
                    move = (i,j)
                    return move 
                
    
    move = (-1,-1)
    running = True
    while running == True:
        
        x = random.randrange(0,3)
        y = random.randrange(0,3)
        
        List = board[x]
        element, pos = List[y]
        if element == None:
            move = (x,y)
            running = False
            
    return move
